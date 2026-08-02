"""
model/train_real_model.py
---------------------------
Trains a model on the REAL 31-player dataset (data/real_player_season_summary.csv),
built by data/build_real_summary.py from hand-transcribed Savant screenshots.

This is NOT a drop-in replacement for model/train_model.py (the 4-feature
model trained on thousands of simulated batted-ball rows). It's a much
smaller, much more honest model:
  - 2 features only: avg_bat_speed, avg_squared_up_pct
    (avg_attack_angle, avg_swing_length aren't public on Savant's
     percentile pages and were not fabricated)
  - n=31 players, one real season aggregate each -- not thousands of rows
  - With this few samples relative to features, use simple linear
    regression + leave-one-out CV rather than XGBoost/RandomForest, which
    will overfit badly at this n.

Run with: python3 model/train_real_model.py
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import LeaveOneOut, cross_val_predict
from sklearn.metrics import mean_absolute_error, r2_score

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "real_player_season_summary.csv"
MODEL_DIR = Path(__file__).resolve().parent

FEATURES_2 = ["avg_bat_speed", "avg_squared_up_pct"]
FEATURES_3 = ["avg_bat_speed", "avg_squared_up_pct", "avg_swing_length"]
TARGET_XWOBA = "avg_xwoba_est"
TARGET_BARREL = "barrel_pct"


def train_and_eval(df, features, target):
    X = df[features].values
    y = df[target].values

    model = LinearRegression()
    loo = LeaveOneOut()
    # Leave-one-out CV is the right call at this n: a normal train/test split
    # would leave a test set too small/noisy to mean much.
    y_pred = cross_val_predict(model, X, y, cv=loo)

    mae = mean_absolute_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    model.fit(X, y)
    coefs = dict(zip(features, model.coef_.round(4).tolist()))

    return {
        "features": features,
        "target": target,
        "n": len(df),
        "loo_mae": round(mae, 4),
        "loo_r2": round(r2, 4),
        "coefficients": coefs,
        "intercept": round(float(model.intercept_), 4),
    }


def main():
    df_full = pd.read_csv(DATA_PATH)
    df_2feat = df_full.dropna(subset=FEATURES_2 + [TARGET_XWOBA, TARGET_BARREL])
    df_3feat = df_full.dropna(subset=FEATURES_3 + [TARGET_XWOBA, TARGET_BARREL])

    results = []

    print(f"=== Modelo de 2 features (bat_speed, squared_up_pct) -- n={len(df_2feat)} ===\n")
    for target in [TARGET_XWOBA, TARGET_BARREL]:
        res = train_and_eval(df_2feat, FEATURES_2, target)
        results.append(res)
        print(f"Target: {target}")
        print(f"  Leave-one-out R²:  {res['loo_r2']}")
        print(f"  Leave-one-out MAE: {res['loo_mae']}")
        print(f"  Coefficients:      {res['coefficients']}")
        print()

    print(f"=== Modelo de 3 features (+ avg_swing_length real) -- n={len(df_3feat)} ===\n")
    for target in [TARGET_XWOBA, TARGET_BARREL]:
        res = train_and_eval(df_3feat, FEATURES_3, target)
        results.append(res)
        print(f"Target: {target}")
        print(f"  Leave-one-out R²:  {res['loo_r2']}")
        print(f"  Leave-one-out MAE: {res['loo_mae']}")
        print(f"  Coefficients:      {res['coefficients']}")
        print()

    print("Nota: el modelo de 3 features corre sobre un n más chico (33 vs 43) porque solo "
          "esos 33 jugadores aparecen en el top-200-por-swings del leaderboard de bat-tracking. "
          "avg_attack_angle sigue sin estar disponible en la descarga CSV, aunque aparece como "
          "eje seleccionable en el gráfico de Savant -- no se fabricó, se dejó fuera.")
    print()
    print("Comparación con el modelo simulado (model/metrics.json, 4 features, miles de filas, "
          "R²=0.81): ambos modelos reales de arriba siguen siendo más chicos y con muestras "
          "reales limitadas -- la comparación correcta es real-2-features vs real-3-features, "
          "no contra el número simulado.")

    out_path = MODEL_DIR / "real_model_metrics.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
