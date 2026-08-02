"""
app/app.py
----------
EP Swing Intelligence — Streamlit app.

Three tabs:
  1. Dashboard   — league-wide view (this is the Power BI equivalent: same
                    metrics, same filters, built to run end-to-end here).
  2. Jugador     — single-player deep dive vs league percentiles.
  3. Simulador   — "what-if" slider: predicted xwOBA/Barrel% from swing inputs.

Run with:  streamlit run app/app.py
"""

import sqlite3
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "ep_swing_intel.db"
MODEL_DIR = ROOT / "model"

NAVY = "#0B1B33"
NAVY2 = "#12233F"
GOLD = "#D4A53A"
OFFWHITE = "#F5F3EC"
GRAY = "#9AA5B8"

FEATURES = ["avg_bat_speed", "avg_attack_angle", "avg_squared_up_pct", "avg_swing_length"]

st.set_page_config(page_title="EP Swing Intelligence", page_icon="⚾", layout="wide")


# ---------------------------------------------------------------------------
# Data loading (cached)
# ---------------------------------------------------------------------------
@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    summary = pd.read_sql(
        """SELECT s.*, p.player_name, p.team, p.position, p.bats
           FROM player_season_summary s JOIN players p ON p.player_id = s.player_id""",
        conn,
    )
    preds = pd.read_sql("SELECT * FROM model_predictions", conn)
    conn.close()
    df = summary.merge(preds, on="player_id", how="left")
    for col in FEATURES + ["avg_xwoba_est", "barrel_pct"]:
        df[f"{col}_pctl"] = (df[col].rank(pct=True) * 100).round(0)
    return df


@st.cache_resource
def load_models():
    xwoba_model = joblib.load(MODEL_DIR / "xwoba_model.pkl")
    barrel_model = joblib.load(MODEL_DIR / "barrel_model.pkl")
    return xwoba_model, barrel_model


# ---------------------------------------------------------------------------
# Brand CSS
# ---------------------------------------------------------------------------
st.markdown(
    f"""
    <style>
    .stApp {{ background-color: {NAVY}; }}
    section[data-testid="stSidebar"] {{ background-color: {NAVY2}; }}
    h1, h2, h3, h4, p, span, label, .stMarkdown {{ color: {OFFWHITE} !important; }}
    .stMetric {{ background-color: {NAVY2}; padding: 12px; border-radius: 10px;
                 border: 1px solid rgba(212,165,58,0.25); }}
    div[data-testid="stMetricValue"] {{ color: {GOLD} !important; }}
    </style>
    """,
    unsafe_allow_html=True,
)

df = load_data()
xwoba_model, barrel_model = load_models()

st.title("⚾ EP Swing Intelligence")
st.caption(
    "SQL + Python + modelo predictivo + dashboard, de punta a punta. "
    "Datos simulados y calibrados contra distribuciones reales de MLB — ver metodología al final."
)

tab_dash, tab_player, tab_sim = st.tabs(["📊 Dashboard", "🔍 Jugador", "🎛️ Simulador"])

# ---------------------------------------------------------------------------
# TAB 1 — League dashboard (Power BI equivalent)
# ---------------------------------------------------------------------------
with tab_dash:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Jugadores", len(df))
    col2.metric("Bat Speed promedio", f"{df['avg_bat_speed'].mean():.1f} mph")
    col3.metric("Barrel% promedio", f"{df['barrel_pct'].mean():.1f}%")
    col4.metric("xwOBA promedio (est.)", f"{df['avg_xwoba_est'].mean():.3f}")

    st.divider()

    c1, c2 = st.columns(2)
    with c1:
        fig = px.scatter(
            df, x="avg_bat_speed", y="avg_xwoba_est", color="barrel_pct",
            hover_name="player_name", size="n_bbe",
            color_continuous_scale=["#182C4D", GOLD],
            labels={"avg_bat_speed": "Bat Speed (mph)", "avg_xwoba_est": "xwOBA (est.)", "barrel_pct": "Barrel%"},
            title="Bat Speed vs xwOBA (tamaño = muestra, color = Barrel%)",
        )
        fig.update_layout(plot_bgcolor=NAVY2, paper_bgcolor=NAVY, font_color=OFFWHITE)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig2 = px.scatter(
            df, x="avg_squared_up_pct", y="barrel_pct", color="avg_bat_speed",
            hover_name="player_name",
            color_continuous_scale=["#182C4D", GOLD],
            labels={"avg_squared_up_pct": "Squared-Up %", "barrel_pct": "Barrel %", "avg_bat_speed": "Bat Speed"},
            title="Squared-Up% vs Barrel% (color = Bat Speed)",
        )
        fig2.update_layout(plot_bgcolor=NAVY2, paper_bgcolor=NAVY, font_color=OFFWHITE)
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Top 15 por xwOBA (estimado)")
    top15 = df.sort_values("avg_xwoba_est", ascending=False).head(15)[
        ["player_name", "team", "position", "avg_bat_speed", "avg_attack_angle",
         "avg_squared_up_pct", "barrel_pct", "avg_xwoba_est", "predicted_xwoba"]
    ].rename(columns={
        "player_name": "Jugador", "team": "Equipo", "position": "Pos",
        "avg_bat_speed": "Bat Speed", "avg_attack_angle": "Attack Angle",
        "avg_squared_up_pct": "Squared-Up%", "barrel_pct": "Barrel%",
        "avg_xwoba_est": "xwOBA (real)", "predicted_xwoba": "xwOBA (modelo)",
    })
    st.dataframe(top15, use_container_width=True, hide_index=True)

    st.subheader("Predicho vs Real (set de prueba del modelo)")
    fig3 = px.scatter(
        df, x="actual_xwoba", y="predicted_xwoba", hover_name="player_name",
        labels={"actual_xwoba": "xwOBA real", "predicted_xwoba": "xwOBA predicho"},
    )
    fig3.add_shape(type="line", x0=df["actual_xwoba"].min(), y0=df["actual_xwoba"].min(),
                    x1=df["actual_xwoba"].max(), y1=df["actual_xwoba"].max(),
                    line=dict(color=GOLD, dash="dash"))
    fig3.update_layout(plot_bgcolor=NAVY2, paper_bgcolor=NAVY, font_color=OFFWHITE)
    st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------------------------------------------------
# TAB 2 — Player deep dive
# ---------------------------------------------------------------------------
with tab_player:
    player_name = st.selectbox("Selecciona jugador", sorted(df["player_name"].unique()))
    row = df[df["player_name"] == player_name].iloc[0]

    c1, c2 = st.columns([1, 2])
    with c1:
        st.markdown(f"### {row['player_name']}")
        st.caption(f"{row['position']} · {row['team']} · Batea {row['bats']}")
        st.metric("xwOBA (est.)", f"{row['avg_xwoba_est']:.3f}", f"{row['avg_xwoba_est_pctl']:.0f}º percentil")
        st.metric("Barrel%", f"{row['barrel_pct']:.1f}%", f"{row['barrel_pct_pctl']:.0f}º percentil")
        st.metric("Bat Speed", f"{row['avg_bat_speed']:.1f} mph", f"{row['avg_bat_speed_pctl']:.0f}º percentil")
        st.caption(f"Predicción del modelo: {row['predicted_xwoba']:.3f} xwOBA (residual {row['residual']:+.3f})")

    with c2:
        categories = ["Bat Speed", "Attack Angle", "Squared-Up%", "Swing Length"]
        values = [row[f"{c}_pctl"] for c in [f"avg_bat_speed", "avg_attack_angle", "avg_squared_up_pct", "avg_swing_length"]]
        fig4 = go.Figure()
        fig4.add_trace(go.Scatterpolar(r=values, theta=categories, fill="toself",
                                        line_color=GOLD, fillcolor="rgba(212,165,58,0.25)"))
        fig4.update_layout(
            polar=dict(bgcolor=NAVY2, radialaxis=dict(visible=True, range=[0, 100], color=GRAY)),
            paper_bgcolor=NAVY, font_color=OFFWHITE,
            title=f"Perfil de swing — percentiles vs {len(df)} jugadores",
        )
        st.plotly_chart(fig4, use_container_width=True)

# ---------------------------------------------------------------------------
# TAB 3 — What-if simulator
# ---------------------------------------------------------------------------
with tab_sim:
    st.markdown("Ajusta las métricas de swing y observa la predicción del modelo en vivo.")
    c1, c2 = st.columns(2)
    with c1:
        bat_speed = st.slider("Bat Speed (mph)", 55.0, 85.0, 71.0, 0.5)
        attack_angle = st.slider("Attack Angle (°)", -5.0, 30.0, 12.0, 0.5)
    with c2:
        squared_up = st.slider("Squared-Up %", 10.0, 45.0, 26.0, 0.5)
        swing_length = st.slider("Swing Length (ft)", 6.0, 9.0, 7.3, 0.05)

    X_sim = pd.DataFrame([[bat_speed, attack_angle, squared_up, swing_length]], columns=FEATURES)
    pred_xwoba = float(xwoba_model.predict(X_sim)[0])
    pred_barrel = float(barrel_model.predict(X_sim)[0])

    c3, c4 = st.columns(2)
    c3.metric("xwOBA predicho", f"{pred_xwoba:.3f}")
    c4.metric("Barrel% predicho", f"{pred_barrel:.1f}%")

    st.caption(
        "Útil para responder preguntas de entrenamiento tipo: si este jugador gana 2 mph de bat "
        "speed, ¿cuánto sube su xwOBA proyectado? Conecta directo con las prescripciones del EP-TSP "
        "Training Hub."
    )

st.divider()
st.caption(
    "**Metodología:** dataset simulado y calibrado contra distribuciones públicas de Baseball Savant "
    "(bat speed, barrel%, hard-hit%, sweet-spot). Este sandbox no tiene acceso a baseballsavant.mlb.com "
    "ni Kaggle; para datos reales, sustituir data/generate_data.py por una llamada a pybaseball.statcast() "
    "(ver comentarios en ese archivo). xwOBA aquí es una aproximación simplificada, no el modelo "
    "propietario de MLB."
)
