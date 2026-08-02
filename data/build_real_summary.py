"""
data/build_real_summary.py
---------------------------
Bridge between data/real_sample/registry.py (hand-transcribed Savant
snapshots, one row per PLAYER) and the model's expected input grain, which
is player_season_summary (also one row per player) per sql/schema.sql.

Update: as of data/real_sample/bat_tracking_leaders_2026.csv (a real CSV
export from Savant's "Statcast Bat Tracking Leaders" page, top 200 hitters
by swing volume, 2026), avg_swing_length is now a REAL third feature,
matched by player name. attack_angle is still not available -- the CSV
export doesn't include it even though it's a selectable axis on the
Savant chart itself, so it's still excluded rather than fabricated.

Coverage: of registry.py's players, 33/43 appear in the bat-tracking
leaderboard (10 fell below the top-200-by-swings threshold: Judge,
Stanton, Lindor, Betts, Castellanos, Rutschman, Dominguez, Langford,
Robert Jr., Acuna Jr.). Those 10 keep avg_swing_length = NaN and get
dropped by train_real_model.py's dropna when swing_length is used as a
feature -- n=33 for the 3-feature model, n=43 still available for the
2-feature model.

Run with: python3 data/build_real_summary.py
Writes:   data/real_player_season_summary.csv
"""

import csv
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "real_sample"))
from registry import REAL_PLAYER_SNAPSHOTS  # noqa: E402

BAT_TRACKING_CSV = ROOT / "real_sample" / "bat_tracking_leaders_2026.csv"


def _to_last_first(full_name):
    """'Bobby Witt Jr.' -> 'Witt Jr., Bobby' to match the Savant CSV's name format."""
    parts = full_name.strip().split()
    if len(parts) < 2:
        return full_name
    first = parts[0]
    last = " ".join(parts[1:])
    return f"{last}, {first}"


def _load_bat_tracking_swing_length():
    """Returns {player_name_in_our_format: swing_length} for matched players."""
    with open(BAT_TRACKING_CSV, encoding="utf-8-sig") as f:
        csv_rows = {row["name"]: row for row in csv.DictReader(f)}

    swing_length_by_player = {}
    for s in REAL_PLAYER_SNAPSHOTS:
        our_name = s["player_name"]
        key = _to_last_first(our_name)
        if key in csv_rows:
            swing_length_by_player[our_name] = float(csv_rows[key]["swing_length"])
    return swing_length_by_player


def build():
    swing_length_map = _load_bat_tracking_swing_length()

    rows = []
    for i, s in enumerate(REAL_PLAYER_SNAPSHOTS, start=1):
        rows.append({
            "player_id": i,
            "player_name": s["player_name"],
            "avg_bat_speed": s["bat_speed"],
            "avg_squared_up_pct": s["squared_up_pct"],
            "avg_swing_length": swing_length_map.get(s["player_name"]),  # NaN if not in bat-tracking CSV
            "avg_exit_velocity": s["avg_exit_velo"],
            "barrel_pct": s["barrel_pct"],
            "hard_hit_pct": s["hard_hit_pct"],
            "sweet_spot_pct": s["la_sweet_spot_pct"],
            "avg_xwoba_est": s["xwoba"],
        })

    df = pd.DataFrame(rows)

    n_before = len(df)
    n_2feat = len(df.dropna(subset=["avg_bat_speed", "avg_squared_up_pct", "avg_xwoba_est", "barrel_pct"]))
    n_3feat = len(df.dropna(subset=["avg_bat_speed", "avg_squared_up_pct", "avg_swing_length",
                                     "avg_xwoba_est", "barrel_pct"]))
    print(f"{n_2feat}/{n_before} players have complete data for the 2-feature model "
          f"(bat_speed, squared_up_pct).")
    print(f"{n_3feat}/{n_before} players have real avg_swing_length too "
          f"(from bat_tracking_leaders_2026.csv) -- usable for the 3-feature model.")
    print("avg_attack_angle is still NOT available -- excluded, not fabricated.")

    out_path = ROOT / "real_player_season_summary.csv"
    df.to_csv(out_path, index=False)
    print(f"\nWrote {out_path} ({len(df)} players)")
    return df


if __name__ == "__main__":
    build()