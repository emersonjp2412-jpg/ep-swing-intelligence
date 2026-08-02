"""
data/fetch_real_data.py
------------------------
Run this on YOUR machine (not in the Claude sandbox — baseballsavant.mlb.com
is blocked there). This pulls real 2024-2025 Statcast data including real
Bat Tracking metrics (bat_speed, attack_angle, etc.) via pybaseball, and
writes it in the exact format etl/clean.py expects — so the rest of the
pipeline (SQL, model, Streamlit, PDF, Power BI) runs completely unchanged.

Setup:
    pip install pybaseball

Run:
    python3 data/fetch_real_data.py

This takes a few minutes — statcast() pulls pitch-by-pitch data for the
whole date range and bat tracking coverage is still partial (~50-70% of
pitches as of 2024-2025), which is normal and handled by the dropna step
in etl/clean.py.
"""

import numpy as np
import pandas as pd
from pybaseball import statcast, playerid_reverse_lookup

START_DATE = "2024-04-01"
END_DATE = "2024-09-29"  # widen this range for more data, at the cost of runtime


def fetch():
    print(f"Pulling Statcast data {START_DATE} to {END_DATE} — this can take a few minutes...")
    df = statcast(start_dt=START_DATE, end_dt=END_DATE)
    print(f"Pulled {len(df)} pitches.")

    # Keep only batted-ball events with real bat-tracking coverage.
    df = df.dropna(subset=["bat_speed", "attack_angle", "launch_speed", "launch_angle"])
    print(f"{len(df)} rows have both bat-tracking and batted-ball outcome data.")

    return df


def build_players_table(df):
    ids = df["batter"].dropna().unique().astype(int).tolist()
    lookup = playerid_reverse_lookup(ids, key_type="mlbam")
    lookup["player_name"] = lookup["name_first"].str.title() + " " + lookup["name_last"].str.title()
    players = lookup[["key_mlbam", "player_name"]].rename(columns={"key_mlbam": "player_id"})
    # team/position/bats aren't in this lookup table — pybaseball's
    # `chadwick_register()` or a roster call can fill these in if needed;
    # left as placeholders here so the schema still lines up.
    players["team"] = "UNK"
    players["position"] = "UNK"
    players["bats"] = df.groupby("batter")["stand"].agg(lambda s: s.mode()[0]).reindex(players["player_id"]).values
    return players


def build_batted_balls_table(df):
    out = pd.DataFrame({
        "bb_id": range(1, len(df) + 1),
        "player_id": df["batter"].astype(int).values,
        "bat_speed": df["bat_speed"].values,
        "attack_angle": df["attack_angle"].values,
        # Real statcast doesn't publish "squared_up_pct" as a per-pitch field
        # in the standard statcast() export — it's derived on Savant's bat
        # tracking leaderboard. As a stand-in, approximate it here from how
        # close actual EV came to bat_speed-implied potential EV; swap for
        # the real `swing_take`/bat-tracking leaderboard via savant-extras
        # (pip install savant-extras) if you want the official figure.
        "squared_up_pct": np.clip((df["launch_speed"] / (df["bat_speed"] * 1.2 + 20)) * 100, 0, 100).values,
        "swing_length": df["swing_length"].values if "swing_length" in df.columns else np.nan,
        "pitch_speed": df["release_speed"].values,
        "exit_velocity": df["launch_speed"].values,
        "launch_angle": df["launch_angle"].values,
        "is_barrel": (df["launch_speed_angle"] == 6).astype(int).values if "launch_speed_angle" in df.columns else 0,
        "is_hard_hit": (df["launch_speed"] >= 95).astype(int).values,
        "is_sweet_spot": ((df["launch_angle"] >= 8) & (df["launch_angle"] <= 32)).astype(int).values,
        "xwoba_est": df["estimated_woba_using_speedangle"].values,  # this IS the real MLB xwOBA, not an approximation
    })
    return out


if __name__ == "__main__":
    raw = fetch()
    players = build_players_table(raw)
    bbe = build_batted_balls_table(raw)

    players.to_csv("data/raw_players.csv", index=False)
    bbe.to_csv("data/raw_batted_balls.csv", index=False)

    print(f"\nWrote data/raw_players.csv ({len(players)} players)")
    print(f"Wrote data/raw_batted_balls.csv ({len(bbe)} batted balls)")
    print("\nNow run the rest of the pipeline unchanged:")
    print("  python3 etl/clean.py && python3 model/train_model.py && python3 report/generate_report.py")
