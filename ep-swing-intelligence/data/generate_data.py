"""
generate_data.py
-----------------
Generates a Statcast-style batted-ball dataset, calibrated against publicly
known MLB distributions and Baseball Savant's documented metric definitions
(barrel, hard-hit, sweet-spot). This sandbox cannot reach baseballsavant.mlb.com
or Kaggle directly, so this simulates realistic data instead of scraping it.

To swap in REAL data on a machine with internet access, replace this script's
output with:

    from pybaseball import statcast
    df = statcast(start_dt="2025-03-27", end_dt="2025-09-28")
    df.to_csv("data/raw_statcast.csv", index=False)

...then adjust column names in etl/clean.py to match (they're documented there).
Everything downstream (SQL schema, model, Streamlit app, PDF report) is written
against the same column names, so no other code needs to change.
"""

import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)

TEAMS = ["Rays", "Brewers", "Red Sox", "Nationals", "Phillies", "Mets", "Guardians",
         "Orioles", "Braves", "Dodgers", "Astros", "Yankees", "Cubs", "Padres"]
POSITIONS = ["C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH"]

FIRST_NAMES = ["Brice", "Wilyer", "Junior", "James", "Marco", "Devin", "Xavier", "Kaleb",
               "Ronny", "Elly", "Corbin", "Julio", "Adley", "Gunnar", "Bobby", "Riley",
               "Jordan", "Nolan", "Ezequiel", "Trevor", "Anthony", "Michael", "Luis", "Carlos"]
LAST_NAMES = ["Turang", "Abreu", "Caminero", "Wood", "Rivas", "Holt", "Reyes", "Marsh",
              "Ortiz", "De La Cruz", "Carroll", "Rodriguez", "Henderson", "Witt", "Meyer",
              "Greene", "Alvarez", "Arenado", "Tovar", "Story", "Volpe", "Perez", "Diaz", "Nunez"]

N_PLAYERS = 240
MIN_BBE_PER_PLAYER = 60
MAX_BBE_PER_PLAYER = 320


def make_players(n):
    names = set()
    rows = []
    while len(rows) < n:
        name = f"{RNG.choice(FIRST_NAMES)} {RNG.choice(LAST_NAMES)}"
        if name in names:
            continue
        names.add(name)
        rows.append({
            "player_id": 100000 + len(rows),
            "player_name": name,
            "team": RNG.choice(TEAMS),
            "position": RNG.choice(POSITIONS),
            "bats": RNG.choice(["R", "L", "S"], p=[0.58, 0.35, 0.07]),
        })
    return pd.DataFrame(rows)


def player_true_ability(n):
    # Bat speed: MLB league avg ~70-71 mph, calibrated so ~99.9th pct lands near 80mph
    # (real reference point: 79.9 mph = 100th percentile, per Baseball Savant 2026 data).
    bat_speed_true = np.clip(RNG.normal(70.5, 3.4, n), 58, 81)
    # Attack angle: Savant's "ideal" window is 5-20 degrees; league spreads around ~10-13.
    attack_angle_true = np.clip(RNG.normal(11.5, 4.8, n), -5, 30)
    # Squared-up%: how much of potential EV is realized on contact.
    squared_up_true = np.clip(RNG.normal(26.5, 4.5, n), 12, 45)
    # Swing length (feet) - shorter is generally more efficient/contact-oriented.
    swing_length_true = np.clip(RNG.normal(7.35, 0.55, n), 5.8, 9.2)
    return bat_speed_true, attack_angle_true, squared_up_true, swing_length_true


def barrel_classify(ev, la):
    """Approximate Statcast barrel rule: qualifying launch-angle window widens
    as exit velocity increases above 98 mph. This mirrors the publicly
    documented shape of the real classifier, not MLB's exact proprietary table.
    """
    if ev < 98:
        return False
    width = 6 + max(0, ev - 98) * 2.5  # widens ~2.5 deg per mph above 98
    center = 28 - max(0, ev - 98) * 0.25  # center drifts down slightly at higher EV
    lo, hi = center - width / 2, center + width / 2 + 12  # slightly asymmetric widening
    return lo <= la <= hi


def simulate_batted_balls(players_df):
    bat_speed_t, attack_angle_t, squared_up_t, swing_len_t = player_true_ability(len(players_df))
    all_rows = []
    bb_id = 1
    for i, prow in players_df.iterrows():
        n_bbe = int(RNG.integers(MIN_BBE_PER_PLAYER, MAX_BBE_PER_PLAYER))
        pitch_speed = RNG.normal(93.5, 3.5, n_bbe)

        bat_speed = np.clip(RNG.normal(bat_speed_t[i], 3.8, n_bbe), 45, 84)
        attack_angle = RNG.normal(attack_angle_t[i], 6.0, n_bbe)
        squared_up = np.clip(RNG.normal(squared_up_t[i], 9.5, n_bbe), 3, 60)
        swing_length = np.clip(RNG.normal(swing_len_t[i], 0.35, n_bbe), 5.5, 9.8)

        # Simplified physics-informed exit velocity model (not MLB's proprietary formula),
        # calibrated so league-average EV and spread land near real MLB values
        # (~88.5 mph mean, wide enough spread for realistic barrel/hard-hit rates).
        exit_velocity = (
            0.23 * pitch_speed
            + 0.75 * bat_speed
            + 0.53 * squared_up
            + RNG.normal(0, 8.5, n_bbe)
        )
        exit_velocity = np.clip(exit_velocity, 35, 121)

        launch_angle = attack_angle + RNG.normal(0, 13, n_bbe)
        launch_angle = np.clip(launch_angle, -45, 75)

        for j in range(n_bbe):
            ev, la = float(exit_velocity[j]), float(launch_angle[j])
            all_rows.append({
                "bb_id": bb_id,
                "player_id": prow["player_id"],
                "bat_speed": round(float(bat_speed[j]), 1),
                "attack_angle": round(float(attack_angle[j]), 1),
                "squared_up_pct": round(float(squared_up[j]), 1),
                "swing_length": round(float(swing_length[j]), 2),
                "pitch_speed": round(float(pitch_speed[j]), 1),
                "exit_velocity": round(ev, 1),
                "launch_angle": round(la, 1),
                "is_barrel": barrel_classify(ev, la),
                "is_hard_hit": ev >= 95.0,
                "is_sweet_spot": 8.0 <= la <= 32.0,
            })
            bb_id += 1
    return pd.DataFrame(all_rows)


def estimate_xwoba(df):
    """Simplified empirical approximation of xwOBA shape from EV + LA.
    NOT MLB's proprietary xwOBA model — good enough for a portfolio-grade
    demonstration of the pipeline, clearly labeled as an approximation
    everywhere it's surfaced (DB column, dashboard, report).
    """
    ev_score = np.clip((df["exit_velocity"] - 68) / 42, 0, 1)
    la_score = np.exp(-((df["launch_angle"] - 15) ** 2) / (2 * 13 ** 2))
    base = 0.05 + 0.95 * ev_score * la_score
    noise = RNG.normal(0, 0.05, len(df))
    xwoba = np.clip(base + noise, 0.0, 2.05)
    return xwoba.round(3)


def main():
    players = make_players(N_PLAYERS)
    bbe = simulate_batted_balls(players)
    bbe["xwoba_est"] = estimate_xwoba(bbe)

    # Inject a few nulls / dirty rows on purpose so the cleaning step has real work to do.
    dirty_idx = RNG.choice(bbe.index, size=int(len(bbe) * 0.015), replace=False)
    bbe.loc[dirty_idx[: len(dirty_idx) // 3], "exit_velocity"] = np.nan
    bbe.loc[dirty_idx[len(dirty_idx) // 3: 2 * len(dirty_idx) // 3], "bat_speed"] = -1
    dup_rows = bbe.sample(n=30, random_state=1)
    bbe = pd.concat([bbe, dup_rows], ignore_index=True)

    players.to_csv("data/raw_players.csv", index=False)
    bbe.to_csv("data/raw_batted_balls.csv", index=False)
    print(f"players: {len(players)} rows")
    print(f"batted balls: {len(bbe)} rows (includes intentional dirty/dup rows for the ETL step)")


if __name__ == "__main__":
    main()
