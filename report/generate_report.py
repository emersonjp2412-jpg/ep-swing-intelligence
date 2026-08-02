"""
report/generate_report.py
--------------------------
Builds a branded, automated PDF report straight from the database + trained
model — no manual copy-pasting. Run this after etl/clean.py and
model/train_model.py.

Run with: python3 report/generate_report.py
"""

import json
import sqlite3
from datetime import datetime
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "ep_swing_intel.db"
MODEL_DIR = ROOT / "model"
REPORT_DIR = Path(__file__).resolve().parent
OUT_PDF = REPORT_DIR / "EP_Swing_Intelligence_Report.pdf"

NAVY = "#0B1B33"
NAVY2 = "#12233F"
GOLD = "#D4A53A"
OFFWHITE = "#F5F3EC"
GRAY = "#9AA5B8"


def load_everything():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(
        """SELECT s.*, p.player_name, p.team, p.position, m.predicted_xwoba, m.residual
           FROM player_season_summary s
           JOIN players p ON p.player_id = s.player_id
           LEFT JOIN model_predictions m ON m.player_id = s.player_id""",
        conn,
    )
    conn.close()
    with open(MODEL_DIR / "metrics.json") as f:
        metrics = json.load(f)
    return df, metrics


def make_charts(df, metrics):
    plt.rcParams.update({
        "figure.facecolor": NAVY2, "axes.facecolor": NAVY2,
        "axes.edgecolor": GRAY, "axes.labelcolor": OFFWHITE,
        "xtick.color": GRAY, "ytick.color": GRAY, "text.color": OFFWHITE,
        "font.size": 9,
    })

    fig1, ax1 = plt.subplots(figsize=(5.6, 3.4))
    sc = ax1.scatter(df["avg_bat_speed"], df["avg_xwoba_est"], c=df["barrel_pct"],
                      cmap="YlOrBr", s=18, alpha=0.85, edgecolors="none")
    ax1.set_xlabel("Bat Speed (mph)")
    ax1.set_ylabel("xwOBA (est.)")
    ax1.set_title("Bat Speed vs xwOBA (color = Barrel%)", color=OFFWHITE)
    cbar = fig1.colorbar(sc, ax=ax1)
    cbar.ax.yaxis.set_tick_params(color=GRAY)
    plt.tight_layout()
    fig1.savefig(REPORT_DIR / "chart_scatter.png", dpi=150, facecolor=NAVY2)
    plt.close(fig1)

    fig2, ax2 = plt.subplots(figsize=(5.6, 3.4))
    ax2.scatter(df["avg_xwoba_est"], df["predicted_xwoba"], s=16, alpha=0.8, color=GOLD)
    lims = [df["avg_xwoba_est"].min(), df["avg_xwoba_est"].max()]
    ax2.plot(lims, lims, "--", color=OFFWHITE, linewidth=1)
    ax2.set_xlabel("xwOBA real")
    ax2.set_ylabel("xwOBA predicho")
    ax2.set_title("Modelo: predicho vs. real", color=OFFWHITE)
    plt.tight_layout()
    fig2.savefig(REPORT_DIR / "chart_pred.png", dpi=150, facecolor=NAVY2)
    plt.close(fig2)

    fig3, ax3 = plt.subplots(figsize=(5.6, 3.0))
    feats = metrics["xwoba_model"]["feature_importance"]
    names = list(feats.keys())
    vals = list(feats.values())
    ax3.barh(names, vals, color=GOLD)
    ax3.set_title("Importancia de variables — modelo xwOBA", color=OFFWHITE)
    plt.tight_layout()
    fig3.savefig(REPORT_DIR / "chart_importance.png", dpi=150, facecolor=NAVY2)
    plt.close(fig3)


def build_html(df, metrics):
    top10 = df.sort_values("avg_xwoba_est", ascending=False).head(10)
    rows_html = "".join(
        f"""<tr>
            <td>{r.player_name}</td><td>{r.team}</td><td>{r.position}</td>
            <td>{r.avg_bat_speed:.1f}</td><td>{r.barrel_pct:.1f}%</td>
            <td>{r.avg_xwoba_est:.3f}</td><td>{r.predicted_xwoba:.3f}</td>
        </tr>"""
        for r in top10.itertuples()
    )

    generated = datetime.now().strftime("%d de %B de %Y, %H:%M")
    xwoba_m = metrics["xwoba_model"]
    barrel_m = metrics["barrel_model"]

    html = f"""
    <html><head><meta charset="utf-8"><style>
        @page {{ size: Letter; margin: 1.6cm; }}
        body {{ font-family: 'Helvetica', Arial, sans-serif; background: {NAVY}; color: {OFFWHITE}; }}
        h1 {{ color: {GOLD}; font-size: 20px; margin-bottom: 2px; line-height: 1.3; }}
        h2 {{ color: {GOLD}; font-size: 14px; border-bottom: 1px solid rgba(212,165,58,0.35);
              padding-bottom: 4px; margin-top: 22px; }}
        .eyebrow {{ color: {GRAY}; font-size: 10px; letter-spacing: 1px; text-transform: uppercase; }}
        .meta {{ color: {GRAY}; font-size: 10px; margin-top: 8px; margin-bottom: 18px; }}
        .kpi-row {{ display: flex; gap: 12px; margin: 14px 0; }}
        .kpi {{ background: {NAVY2}; border: 1px solid rgba(212,165,58,0.3); border-radius: 8px;
                padding: 10px 14px; flex: 1; }}
        .kpi .num {{ color: {GOLD}; font-size: 20px; font-weight: bold; }}
        .kpi .lbl {{ color: {GRAY}; font-size: 8.5px; text-transform: uppercase; }}
        table {{ width: 100%; border-collapse: collapse; font-size: 9.5px; margin-top: 8px; }}
        thead {{ display: table-header-group; }}
        tr {{ page-break-inside: avoid; }}
        th {{ background: {NAVY2}; color: {GOLD}; text-align: left; padding: 6px 8px;
              border-bottom: 1px solid rgba(212,165,58,0.3); }}
        td {{ padding: 5px 8px; border-bottom: 1px solid rgba(255,255,255,0.06); }}
        img {{ width: 100%; border-radius: 6px; margin-top: 6px; }}
        .two-col {{ display: flex; gap: 16px; }}
        .two-col > div {{ flex: 1; }}
        .table-block {{ page-break-inside: avoid; }}
        .footnote {{ font-size: 8px; color: {GRAY}; margin-top: 24px; line-height: 1.5; }}
    </style></head>
    <body>
        <div class="eyebrow">EP Swing Intelligence</div>
        <h1>Reporte Automático<br/>Métricas de Swing y Predicción de xwOBA</h1>
        <div class="meta">Generado automáticamente el {generated} · {len(df)} jugadores calificados (min. 40 BBE)</div>

        <div class="kpi-row">
            <div class="kpi"><div class="num">{df['avg_bat_speed'].mean():.1f}</div><div class="lbl">Bat Speed prom. (mph)</div></div>
            <div class="kpi"><div class="num">{df['barrel_pct'].mean():.1f}%</div><div class="lbl">Barrel% prom.</div></div>
            <div class="kpi"><div class="num">{df['avg_xwoba_est'].mean():.3f}</div><div class="lbl">xwOBA prom. (est.)</div></div>
            <div class="kpi"><div class="num">{xwoba_m['r2']:.2f}</div><div class="lbl">R² modelo xwOBA</div></div>
        </div>

        <h2>Modelo Predictivo</h2>
        <p style="font-size:10px;">
            XGBoost Regressor entrenado sobre {xwoba_m['n_train']} jugadores (test: {xwoba_m['n_test']}),
            prediciendo xwOBA a partir de Bat Speed, Attack Angle, Squared-Up% y Swing Length.
            R² = {xwoba_m['r2']:.2f} · MAE = {xwoba_m['mae']:.3f}. Modelo secundario (Random Forest) para
            Barrel%: R² = {barrel_m['r2']:.2f} · MAE = {barrel_m['mae']:.2f}.
        </p>
        <div class="two-col">
            <div><img src="chart_scatter.png"/></div>
            <div><img src="chart_pred.png"/></div>
        </div>

        <div style="page-break-before: always;"></div>

        <h2>Importancia de Variables</h2>
        <img src="chart_importance.png" style="width:60%;"/>

        <div class="table-block">
            <h2>Top 10 — xwOBA (estimado)</h2>
            <table>
                <thead>
                    <tr><th>Jugador</th><th>Equipo</th><th>Pos</th><th>Bat Speed</th><th>Barrel%</th><th>xwOBA real</th><th>xwOBA modelo</th></tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>

        <div class="footnote">
            Metodología: dataset simulado y calibrado contra distribuciones públicas de Baseball Savant
            (bat speed, barrel%, hard-hit%, sweet-spot; referencia real: Bat Speed 79.9mph = percentil 100,
            temporada 2026). Este entorno no tiene acceso directo a baseballsavant.mlb.com ni Kaggle;
            para producción con datos reales, sustituir data/generate_data.py por pybaseball.statcast().
            xwOBA es una aproximación simplificada con fines demostrativos, no el modelo propietario de MLB.
            Generado automáticamente por report/generate_report.py — sin edición manual.
        </div>
    </body></html>
    """
    return html


if __name__ == "__main__":
    df, metrics = load_everything()
    make_charts(df, metrics)
    html_str = build_html(df, metrics)
    HTML(string=html_str, base_url=str(REPORT_DIR)).write_pdf(str(OUT_PDF))
    print(f"PDF generado: {OUT_PDF}")
