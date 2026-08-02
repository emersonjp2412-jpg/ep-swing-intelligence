"""
etl/clean.py
------------
Cleans the raw batted-ball export and loads it into the SQL database defined
in sql/schema.sql. Designed to run unchanged against a real pybaseball export
(see data/generate_data.py header for the swap-in instructions) as long as the
column names line up — mapping notes are inline below.

Steps:
  1. Load raw CSVs
  2. Validate & clean (nulls, out-of-range values, duplicates)
  3. Load into SQLite following sql/schema.sql
  4. Aggregate to player_season_summary
  5. Print a data-quality report
"""

import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
SQL_DIR = ROOT / "sql"
DB_PATH = DATA_DIR / "ep_swing_intel.db"

# If pointing this at a real pybaseball statcast() export instead of the
# simulated data, rename these columns first:
#   bat_speed        <- bat_speed
#   attack_angle      <- attack_angle
#   exit_velocity     <- launch_speed
#   launch_angle      <- launch_angle
#   xwoba_est          <- estimated_woba_using_speedangle
#   squared_up_pct    <- (not in standard statcast() export; requires bat-tracking columns)
REQUIRED_COLUMNS = [
    "bb_id", "player_id", "bat_speed", "attack_angle", "squared_up_pct",
    "swing_length", "pitch_speed", "exit_velocity", "launch_angle",
    "is_barrel", "is_hard_hit", "is_sweet_spot", "xwoba_est",
]


def load_raw():
    players = pd.read_csv(DATA_DIR / "raw_players.csv")
    bbe = pd.read_csv(DATA_DIR / "raw_batted_balls.csv")
    return players, bbe


def clean(bbe: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    report = {"rows_in": len(bbe)}

    missing_cols = [c for c in REQUIRED_COLUMNS if c not in bbe.columns]
    if missing_cols:
        raise ValueError(f"Missing expected columns: {missing_cols}")

    # 1. Drop exact duplicate batted-ball records (same bb_id).
    before = len(bbe)
    bbe = bbe.drop_duplicates(subset="bb_id", keep="first")
    report["duplicates_removed"] = before - len(bbe)

    # 2. Drop rows with nulls in required numeric fields — can't impute a
    #    physical measurement like exit velocity without fabricating data.
    numeric_cols = ["bat_speed", "attack_angle", "squared_up_pct", "swing_length",
                     "pitch_speed", "exit_velocity", "launch_angle", "xwoba_est"]
    before = len(bbe)
    bbe = bbe.dropna(subset=numeric_cols)
    report["null_rows_dropped"] = before - len(bbe)

    # 3. Range validation — physically impossible values are data errors, not outliers.
    before = len(bbe)
    bbe = bbe[
        (bbe["bat_speed"] > 0) & (bbe["bat_speed"] < 90)
        & (bbe["exit_velocity"] > 0) & (bbe["exit_velocity"] < 125)
        & (bbe["squared_up_pct"] >= 0) & (bbe["squared_up_pct"] <= 100)
        & (bbe["swing_length"] > 0) & (bbe["swing_length"] < 12)
        & (bbe["launch_angle"] >= -90) & (bbe["launch_angle"] <= 90)
    ]
    report["out_of_range_dropped"] = before - len(bbe)

    # 4. Normalize booleans stored as True/False strings or 0/1 into clean ints.
    for col in ["is_barrel", "is_hard_hit", "is_sweet_spot"]:
        bbe[col] = bbe[col].astype(str).str.lower().map(
            {"true": 1, "1": 1, "false": 0, "0": 0}
        ).astype(int)

    report["rows_out"] = len(bbe)
    return bbe, report


def load_to_sqlite(players: pd.DataFrame, bbe: pd.DataFrame):
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    schema_sql = (SQL_DIR / "schema.sql").read_text()
    conn.executescript(schema_sql)

    players.to_sql("players", conn, if_exists="append", index=False)
    bbe[[
        "bb_id", "player_id", "bat_speed", "attack_angle", "squared_up_pct",
        "swing_length", "pitch_speed", "exit_velocity", "launch_angle",
        "is_barrel", "is_hard_hit", "is_sweet_spot", "xwoba_est",
    ]].to_sql("batted_balls", conn, if_exists="append", index=False)

    # Player-level aggregation — this is what the model & dashboards consume.
    agg = bbe.groupby("player_id").agg(
        n_bbe=("bb_id", "count"),
        avg_bat_speed=("bat_speed", "mean"),
        avg_attack_angle=("attack_angle", "mean"),
        avg_squared_up_pct=("squared_up_pct", "mean"),
        avg_swing_length=("swing_length", "mean"),
        avg_exit_velocity=("exit_velocity", "mean"),
        barrel_pct=("is_barrel", "mean"),
        hard_hit_pct=("is_hard_hit", "mean"),
        sweet_spot_pct=("is_sweet_spot", "mean"),
        avg_xwoba_est=("xwoba_est", "mean"),
    ).reset_index()
    for pct_col in ["barrel_pct", "hard_hit_pct", "sweet_spot_pct"]:
        agg[pct_col] = (agg[pct_col] * 100).round(2)
    agg = agg.round(3)

    # Only keep players with a minimum sample size — same logic Savant applies
    # for its own qualified leaderboards.
    MIN_BBE = 40
    agg = agg[agg["n_bbe"] >= MIN_BBE]

    agg.to_sql("player_season_summary", conn, if_exists="append", index=False)
    conn.commit()
    conn.close()
    return agg


def main():
    players, bbe_raw = load_raw()
    bbe_clean, report = clean(bbe_raw)
    agg = load_to_sqlite(players, bbe_clean)

    print("=== Data quality report ===")
    for k, v in report.items():
        print(f"  {k}: {v}")
    print(f"\nDatabase written to: {DB_PATH}")
    print(f"player_season_summary: {len(agg)} qualified players (min 40 BBE)")


if __name__ == "__main__":
    main()
