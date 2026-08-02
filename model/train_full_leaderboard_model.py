"""
model/train_full_leaderboard_model.py
---------------------------------------
Chapter 4: analysis on Savant's FULL public "Bat Tracking Leaders" export
(data/real_sample/bat_tracking_leaders_2026.csv, top 200 hitters by swing
volume, 2026 season) -- not a curated 33/43-player sample, the complete
qualified population as published by Savant.

Two upgrades over the chapter 2/3 models:
1. n=205 instead of 33-43 -- no player-selection bias, this is the whole
   public leaderboard.
2. Target is Savant's own `batter_run_value` (their real, official offensive
   value metric), converted to a rate stat (per swing) to avoid confounding
   with playing time -- not our own xwOBA approximation.

Features: avg_bat_speed, squared_up_per_swing, swing_length -- all real,
all from the same public CSV, no transcription involved.

Run with: python3 model/train_full_leaderboard_model.py
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_predict
from sklearn.metrics import mean_absolute_error, r2_score

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "real_sample" / "bat_tracking_leaders_2026.csv"
MODEL_DIR = Path(__file__).resolve().parent
REPORT_DIR = ROOT / "report"

FEATURES = ["avg_bat_speed", "squared_up_per_swing", "swing_length"]
TARGET = "run_value_per_swing"

# EP brand colors
NAVY = "#0B1B33"
GOLD = "#D4A53A"
OFFWHITE = "#F5F3EC"
TEAL = "#3E7C8A"


def load_data():
    df = pd.read_csv(DATA_PATH, encoding="utf-8-sig")
    df[TARGET] = df["batter_run_value"] / df["swings_competitive"]
    return df


def train_and_eval(df, features, target, n_splits=10):
    X = df[features].values
    y = df[target].values

    model = LinearRegression()
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    y_pred = cross_val_predict(model, X, y, cv=kf)

    mae = mean_absolute_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    model.fit(X, y)
    coefs = dict(zip(features, model.coef_.round(5).tolist()))

    return {
        "features": features,
        "target": target,
        "n": len(df),
        "cv_folds": n_splits,
        "cv_r2": round(r2, 4),
        "cv_mae": round(mae, 5),
        "coefficients": coefs,
        "intercept": round(float(model.intercept_), 5),
    }, y_pred


def make_scatter_chart(df, y_pred, out_path):
    fig, ax = plt.subplots(figsize=(8, 6), dpi=200)
    fig.patch.set_facecolor(OFFWHITE)
    ax.set_facecolor(OFFWHITE)

    sc = ax.scatter(df["avg_bat_speed"], df["squared_up_per_swing"],
                     c=df[TARGET], cmap="RdYlBu_r", s=55, edgecolors=NAVY,
                     linewidths=0.4, zorder=3)
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label("Run value / swing (real, Savant)", fontsize=10, color=NAVY)

    ax.set_xlabel("Avg Bat Speed (mph)", fontsize=12, color=NAVY)
    ax.set_ylabel("Squared-Up % per swing", fontsize=12, color=NAVY)
    ax.set_title("EP Swing Intelligence — Capítulo 4\nLeaderboard completo de Savant (n=205), no muestra curada",
                 fontsize=12.5, fontweight="bold", color=NAVY, pad=14)
    ax.grid(linestyle="--", alpha=0.3, zorder=0)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_color(NAVY)

    plt.tight_layout()
    plt.savefig(out_path, facecolor=OFFWHITE, bbox_inches="tight")
    plt.close()


def main():
    df = load_data()
    print(f"Cargados {len(df)} jugadores del leaderboard completo de Savant (2026).\n")

    result, y_pred = train_and_eval(df, FEATURES, TARGET)
    print("=== Modelo de 3 features, población completa (n=205) ===")
    print(f"  Target: batter_run_value / swings_competitive (rate real de Savant)")
    print(f"  CV R² (10-fold): {result['cv_r2']}")
    print(f"  CV MAE:          {result['cv_mae']}")
    print(f"  Coeficientes:    {result['coefficients']}")
    print()

    # Comparison line
    print("Comparación con capítulo 3 (n=33, xwOBA propio, LOO-CV):")
    print("  Capítulo 3: R²=0.38 (target=avg_xwoba_est, aproximación propia)")
    print(f"  Capítulo 4: R²={result['cv_r2']} (target=batter_run_value real de Savant, "
          f"población completa n=205)")
    print()

    out_json = MODEL_DIR / "full_leaderboard_model_metrics.json"
    with open(out_json, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Wrote {out_json}")

    chart_path = REPORT_DIR / "chart_capitulo4_scatter.png"
    make_scatter_chart(df, y_pred, chart_path)
    print(f"Wrote {chart_path}")


if __name__ == "__main__":
    main()
