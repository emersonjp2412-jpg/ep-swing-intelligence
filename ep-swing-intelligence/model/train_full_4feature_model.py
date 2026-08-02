"""
model/train_full_4feature_model.py
-------------------------------------
Chapter 5: the model this project has been building toward since chapter 2.

Merges FOUR real public Savant CSV exports by player_id (not name-matching,
which avoids the Jr./accent mismatches from earlier chapters):

  - bat_tracking_leaders_2026.csv       -> avg_bat_speed, squared_up_per_swing,
                                            swing_length
  - bat_tracking_swing_path_2026.csv    -> attack_angle (the 4th feature that
                                            was missing through chapters 2-4)
  - expected_stats_2026.csv             -> est_woba (Savant's OFFICIAL xwOBA,
                                            not our own approximation)
  - exit_velocity_2026.csv              -> brl_percent (official Barrel%)

This is the real analogue of the ORIGINAL 4-feature simulated model
(model/train_model.py, R²=0.81) -- same feature set, but every number here
is real, and n is the full overlapping population, not a curated sample.

Run with: python3 model/train_full_4feature_model.py
"""

import json
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_predict
from sklearn.metrics import mean_absolute_error, r2_score

ROOT = Path(__file__).resolve().parent.parent
SAMPLE_DIR = ROOT / "data" / "real_sample"
MODEL_DIR = Path(__file__).resolve().parent
REPORT_DIR = ROOT / "report"

FEATURES = ["avg_bat_speed", "squared_up_per_swing", "swing_length", "attack_angle"]
TARGET_WOBA = "est_woba"
TARGET_BARREL = "brl_percent"

NAVY = "#0B1B33"
GOLD = "#D4A53A"
OFFWHITE = "#F5F3EC"


def load_and_merge():
    bt = pd.read_csv(SAMPLE_DIR / "bat_tracking_leaders_2026.csv", encoding="utf-8-sig")
    sp = pd.read_csv(SAMPLE_DIR / "bat_tracking_swing_path_2026.csv", encoding="utf-8-sig")
    xs = pd.read_csv(SAMPLE_DIR / "expected_stats_2026.csv", encoding="utf-8-sig")
    ev = pd.read_csv(SAMPLE_DIR / "exit_velocity_2026.csv", encoding="utf-8-sig")

    bt = bt.rename(columns={"id": "player_id"})[
        ["player_id", "name", "avg_bat_speed", "squared_up_per_swing", "swing_length"]]
    sp = sp.rename(columns={"id": "player_id"})[["player_id", "attack_angle"]]
    xs = xs.rename(columns={"player_id": "player_id"})[["player_id", "est_woba", "pa"]]
    ev = ev.rename(columns={"player_id": "player_id"})[["player_id", "brl_percent"]]

    xs["player_id"] = xs["player_id"].astype(int)
    ev["player_id"] = ev["player_id"].astype(int)

    df = bt.merge(sp, on="player_id", how="inner")
    df = df.merge(xs, on="player_id", how="inner")
    df = df.merge(ev, on="player_id", how="inner")
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
    }


def make_chart(results):
    labels = ["xwOBA oficial\n(est_woba)", "Barrel%\noficial"]
    r2s = [results[0]["cv_r2"], results[1]["cv_r2"]]

    fig, ax = plt.subplots(figsize=(7, 6), dpi=200)
    fig.patch.set_facecolor(OFFWHITE)
    ax.set_facecolor(OFFWHITE)

    bars = ax.bar(labels, r2s, color=[NAVY, GOLD], width=0.5, zorder=3)
    for b, v in zip(bars, r2s):
        ax.annotate(f'{v:.2f}', xy=(b.get_x() + b.get_width()/2, v),
                    xytext=(0, 6), textcoords="offset points",
                    ha='center', fontsize=15, fontweight='bold', color=NAVY)

    ax.set_ylabel("R² (10-fold CV)", fontsize=12, color=NAVY)
    ax.set_ylim(0, max(r2s) * 1.4)
    ax.set_title(f"EP Swing Intelligence — Capítulo 5\nModelo real de 4 features, targets oficiales de Savant (n={results[0]['n']})",
                 fontsize=12.5, fontweight="bold", color=NAVY, pad=14)
    ax.grid(axis="y", linestyle="--", alpha=0.3, zorder=0)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_color(NAVY)

    plt.tight_layout()
    out = REPORT_DIR / "chart_capitulo5_r2.png"
    plt.savefig(out, facecolor=OFFWHITE, bbox_inches="tight")
    plt.close()
    return out


def main():
    df = load_and_merge()
    print(f"Jugadores con las 4 variables + ambos targets oficiales: {len(df)}\n")

    results = []
    for target in [TARGET_WOBA, TARGET_BARREL]:
        res = train_and_eval(df, FEATURES, target)
        results.append(res)
        print(f"=== Target: {target} (oficial de Savant) ===")
        print(f"  n:                {res['n']}")
        print(f"  CV R² (10-fold):  {res['cv_r2']}")
        print(f"  CV MAE:           {res['cv_mae']}")
        print(f"  Coeficientes:     {res['coefficients']}")
        print()

    print("=== Comparación con todos los capítulos anteriores ===")
    print("  Cap 2 (2 features, n=43, xwOBA propio):            R²=0.27")
    print("  Cap 3 (3 features + swing_length, n=33, xwOBA propio): R²=0.38")
    print(f"  Cap 4 (3 features, n=205, run_value real):          R²=0.13")
    print(f"  Cap 5 (4 features, n={len(df)}, xwOBA OFICIAL):          R²={results[0]['cv_r2']}")
    print()
    print("  Modelo simulado original (4 features, miles de filas fabricadas): R²=0.81")

    out_json = MODEL_DIR / "full_4feature_model_metrics.json"
    with open(out_json, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nWrote {out_json}")

    chart_path = make_chart(results)
    print(f"Wrote {chart_path}")

    # Also export the merged dataset for transparency/reuse
    merged_path = SAMPLE_DIR / "merged_4feature_dataset_2026.csv"
    df.to_csv(merged_path, index=False)
    print(f"Wrote {merged_path}")


if __name__ == "__main__":
    main()
