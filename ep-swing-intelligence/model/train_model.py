"""
model/train_model.py
---------------------
Trains two models from swing mechanics -> outcome quality, using the
player_season_summary table built by etl/clean.py:

  1. Regression:      avg_bat_speed, avg_attack_angle, avg_squared_up_pct,
                       avg_swing_length  ->  avg_xwoba_est   (XGBoost)
  2. Classification-adjacent: same features -> barrel_pct     (Random Forest,
                       treated as regression since barrel_pct is continuous
                       at the player-season grain)

Writes predictions back to model_predictions, saves the model + feature
importances, and prints an evaluation report.
"""

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
import xgboost as xgb

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "ep_swing_intel.db"
MODEL_DIR = Path(__file__).resolve().parent
MODEL_VERSION = "v1.0"

FEATURES = ["avg_bat_speed", "avg_attack_angle", "avg_squared_up_pct", "avg_swing_length"]
TARGET_XWOBA = "avg_xwoba_est"
TARGET_BARREL = "barrel_pct"


def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM player_season_summary", conn)
    conn.close()
    return df


def train_xwoba_model(df):
    X = df[FEATURES]
    y = df[TARGET_XWOBA]
    X_train, X_test, y_train, y_test, idx_train, idx_test = train_test_split(
        X, y, df.index, test_size=0.2, random_state=42
    )

    model = xgb.XGBRegressor(
        n_estimators=300, max_depth=3, learning_rate=0.05,
        subsample=0.85, colsample_bytree=0.85, random_state=42,
    )
    model.fit(X_train, y_train)

    pred_test = model.predict(X_test)
    metrics = {
        "r2": round(float(r2_score(y_test, pred_test)), 4),
        "mae": round(float(mean_absolute_error(y_test, pred_test)), 4),
        "n_train": len(X_train),
        "n_test": len(X_test),
    }

    importances = dict(zip(FEATURES, [round(float(v), 4) for v in model.feature_importances_]))
    return model, metrics, importances


def train_barrel_model(df):
    X = df[FEATURES]
    y = df[TARGET_BARREL]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=300, max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    pred_test = model.predict(X_test)
    metrics = {
        "r2": round(float(r2_score(y_test, pred_test)), 4),
        "mae": round(float(mean_absolute_error(y_test, pred_test)), 4),
    }
    importances = dict(zip(FEATURES, [round(float(v), 4) for v in model.feature_importances_]))
    return model, metrics, importances


def write_predictions(df, xwoba_model, barrel_model):
    conn = sqlite3.connect(DB_PATH)
    X = df[FEATURES]

    pred_xwoba = xwoba_model.predict(X)
    pred_barrel = barrel_model.predict(X)

    out = pd.DataFrame({
        "player_id": df["player_id"],
        "predicted_xwoba": pred_xwoba.round(3),
        "actual_xwoba": df[TARGET_XWOBA],
        "residual": (pred_xwoba - df[TARGET_XWOBA]).round(3),
        "predicted_barrel_pct": pred_barrel.round(2),
        "actual_barrel_pct": df[TARGET_BARREL],
        "model_version": MODEL_VERSION,
        "scored_at": datetime.now(timezone.utc).isoformat(),
    })

    conn.execute("DELETE FROM model_predictions")
    out.to_sql("model_predictions", conn, if_exists="append", index=False)
    conn.commit()
    conn.close()
    return out


def main():
    df = load_data()
    print(f"Training on {len(df)} qualified players.\n")

    xwoba_model, xwoba_metrics, xwoba_importance = train_xwoba_model(df)
    print("=== xwOBA regression (XGBoost) ===")
    print(f"  R^2:  {xwoba_metrics['r2']}")
    print(f"  MAE:  {xwoba_metrics['mae']}")
    print(f"  Feature importance: {xwoba_importance}\n")

    barrel_model, barrel_metrics, barrel_importance = train_barrel_model(df)
    print("=== Barrel% regression (Random Forest) ===")
    print(f"  R^2:  {barrel_metrics['r2']}")
    print(f"  MAE:  {barrel_metrics['mae']}")
    print(f"  Feature importance: {barrel_importance}\n")

    preds = write_predictions(df, xwoba_model, barrel_model)
    print(f"Wrote {len(preds)} rows to model_predictions.")

    joblib.dump(xwoba_model, MODEL_DIR / "xwoba_model.pkl")
    joblib.dump(barrel_model, MODEL_DIR / "barrel_model.pkl")

    metrics_report = {
        "model_version": MODEL_VERSION,
        "trained_at": datetime.now(timezone.utc).isoformat(),
        "features": FEATURES,
        "xwoba_model": {"type": "XGBRegressor", **xwoba_metrics, "feature_importance": xwoba_importance},
        "barrel_model": {"type": "RandomForestRegressor", **barrel_metrics, "feature_importance": barrel_importance},
    }
    with open(MODEL_DIR / "metrics.json", "w") as f:
        json.dump(metrics_report, f, indent=2)
    print(f"\nSaved models + metrics.json to {MODEL_DIR}")


if __name__ == "__main__":
    main()
