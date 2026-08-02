"""
data/real_data_validation.py
------------------------------
Proof that this isn't hand-waved: real Statcast data pulled/transcribed from
genuine sources — baseballsavant.mlb.com itself is blocked in this sandbox's
network allowlist, so this combines two real sources instead:

  1. Judge & Stanton (2015-2017) full batted-ball logs, pulled from a
     GitHub-hosted CSV export (data/real_sample/judge.csv, stanton.csv).
  2. Aaron Judge (2016-2026) and Giancarlo Stanton (2015-2026), real seasons
     transcribed by hand from Baseball Savant screenshots the user captured
     directly in the app — including their real 2026 Bat Speed and
     Squared-Up%, the only real bat-tracking data points in this project.

This data predates (source 1) or falls outside (source 2, only 1 season has
bat-tracking) full bat-tracking coverage, so it can't fully replace the
simulated multi-player model — but every number printed below is real,
official MLB data, not the simulated approximation used in
data/generate_data.py.

Run with: python3 data/real_data_validation.py
"""

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent / "real_sample"))
from judge_savant_2026 import JUDGE_2026_SNAPSHOT, JUDGE_SEASONS, JUDGE_CAREER, MLB_LEAGUE_AVG_REFERENCE
from stanton_savant_2026 import STANTON_2026_SNAPSHOT, STANTON_SEASONS, STANTON_CAREER

PLAYERS = {
    "Aaron Judge (2015-17 batted-ball log)": "data/real_sample/judge.csv",
    "Giancarlo Stanton (2015-17 batted-ball log)": "data/real_sample/stanton.csv",
}


def validate_github_samples():
    for name, path in PLAYERS.items():
        df = pd.read_csv(path)
        # type == 'X' is Statcast's own flag for "ball put in play" (ends the PA).
        # Foul balls (type == 'S', description == 'foul') also carry launch_speed/
        # launch_angle but are NOT batted-ball events — including them silently
        # drags the average down a lot, since fouled-off pitches skew weak/mishit.
        bbe = df[df["type"] == "X"].dropna(subset=["launch_speed", "launch_angle"])

        avg_ev = bbe["launch_speed"].mean()
        avg_la = bbe["launch_angle"].mean()
        avg_xwoba = bbe["estimated_woba_using_speedangle"].mean()
        hard_hit_pct = (bbe["launch_speed"] >= 95).mean() * 100
        sweet_spot_pct = ((bbe["launch_angle"] >= 8) & (bbe["launch_angle"] <= 32)).mean() * 100

        print(f"{name} — {df['game_year'].min()}-{df['game_year'].max()}, {len(bbe)} batted balls (type=='X' only)")
        print(f"  Exit Velocity promedio (real):  {avg_ev:.1f} mph")
        print(f"  Launch Angle promedio (real):   {avg_la:.1f}°")
        print(f"  xwOBA promedio (real, oficial):  {avg_xwoba:.3f}")
        print(f"  Hard-Hit% (real):                {hard_hit_pct:.1f}%")
        print(f"  Sweet-Spot% (real):              {sweet_spot_pct:.1f}%")
        print()


def validate_judge_savant():
    print("=== Aaron Judge — Baseball Savant, 2016-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(JUDGE_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (11 temporadas reales): EV {JUDGE_CAREER['exit_velo']}mph · "
          f"Barrel% {JUDGE_CAREER['barrel_pct']} · xwOBA {JUDGE_CAREER['xwoba']} · "
          f"vs. liga: EV {MLB_LEAGUE_AVG_REFERENCE['exit_velo']}mph · "
          f"Barrel% {MLB_LEAGUE_AVG_REFERENCE['barrel_pct']} · xwOBA {MLB_LEAGUE_AVG_REFERENCE['xwoba']}")

    s = JUDGE_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real (el único punto de bat-tracking 100% real del proyecto) ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_stanton_savant():
    print("=== Giancarlo Stanton — Baseball Savant, 2015-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(STANTON_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (12 temporadas reales): EV {STANTON_CAREER['exit_velo']}mph · "
          f"Barrel% {STANTON_CAREER['barrel_pct']} · xwOBA {STANTON_CAREER['xwoba']}")

    s = STANTON_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentiles no legibles en la captura — 'NOT QUALIFIED')")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%")
    print(f"  xwOBA:          {s['xwoba']}")
    print(f"  Barrel%:        {s['barrel_pct']}%")
    print()


def compare_real_bat_tracking():
    from registry import REAL_PLAYER_SNAPSHOTS, TARGET_ROSTER_SIZE

    print(f"=== Comparación real: {len(REAL_PLAYER_SNAPSHOTS)} jugadores con bat-tracking 100% real ===\n")
    print(f"  {'Jugador':<20}{'Bat Speed':>11}{'Squared-Up%':>13}{'xwOBA':>9}{'Barrel%':>10}{'Hard-Hit%':>11}")
    for s in REAL_PLAYER_SNAPSHOTS:
        print(f"  {s['player_name']:<20}{s['bat_speed']:>11}{s['squared_up_pct']:>13}"
              f"{s['xwoba']:>9}{s['barrel_pct']:>10}{s['hard_hit_pct']:>11}")

    n = len(REAL_PLAYER_SNAPSHOTS)
    print(f"\n  {n}/{TARGET_ROSTER_SIZE} recolectados. "
          f"Faltan {max(0, TARGET_ROSTER_SIZE - n)} para reemplazar el dataset simulado.\n")


def validate_cruz_savant():
    from cruz_savant_2026 import CRUZ_2026_SNAPSHOT, CRUZ_SEASONS, CRUZ_CAREER
    print("=== Oneil Cruz — Baseball Savant, 2021-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(CRUZ_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (6 temporadas reales): EV {CRUZ_CAREER['exit_velo']}mph · "
          f"Barrel% {CRUZ_CAREER['barrel_pct']} · xwOBA {CRUZ_CAREER['xwoba']}")
    s = CRUZ_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_tatis_savant():
    from tatis_savant_2026 import TATIS_2026_SNAPSHOT, TATIS_SEASONS, TATIS_CAREER
    print("=== Fernando Tatis Jr. — Baseball Savant, 2019-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(TATIS_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (6 temporadas reales, 2022 ausente por suspensión): EV {TATIS_CAREER['exit_velo']}mph · "
          f"Barrel% {TATIS_CAREER['barrel_pct']} · xwOBA {TATIS_CAREER['xwoba']}")
    s = TATIS_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_schwarber_savant():
    from schwarber_savant_2026 import SCHWARBER_2026_SNAPSHOT, SCHWARBER_SEASONS, SCHWARBER_CAREER
    print("=== Kyle Schwarber — Baseball Savant, 2015-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(SCHWARBER_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (12 temporadas reales): EV {SCHWARBER_CAREER['exit_velo']}mph · "
          f"Barrel% {SCHWARBER_CAREER['barrel_pct']} · xwOBA {SCHWARBER_CAREER['xwoba']}")
    s = SCHWARBER_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_alonso_savant():
    from alonso_savant_2026 import ALONSO_2026_SNAPSHOT, ALONSO_SEASONS, ALONSO_CAREER
    print("=== Pete Alonso — Baseball Savant, 2019-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(ALONSO_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (8 temporadas reales): EV {ALONSO_CAREER['exit_velo']}mph · "
          f"Barrel% {ALONSO_CAREER['barrel_pct']} · xwOBA {ALONSO_CAREER['xwoba']}")
    s = ALONSO_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_alvarez_savant():
    from alvarez_savant_2026 import ALVAREZ_2026_SNAPSHOT, ALVAREZ_SEASONS, ALVAREZ_CAREER
    print("=== Yordan Alvarez — Baseball Savant, 2019-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(ALVAREZ_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (8 temporadas reales): EV {ALVAREZ_CAREER['exit_velo']}mph · "
          f"Barrel% {ALVAREZ_CAREER['barrel_pct']} · xwOBA {ALVAREZ_CAREER['xwoba']}")
    s = ALVAREZ_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_delacruz_savant():
    from delacruz_savant_2026 import DELACRUZ_2026_SNAPSHOT, DELACRUZ_SEASONS, DELACRUZ_CAREER
    print("=== Elly De La Cruz — Baseball Savant, 2023-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(DELACRUZ_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (4 temporadas reales): EV {DELACRUZ_CAREER['exit_velo']}mph · "
          f"Barrel% {DELACRUZ_CAREER['barrel_pct']} · xwOBA {DELACRUZ_CAREER['xwoba']}")
    s = DELACRUZ_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_arraez_savant():
    from arraez_savant_2026 import ARRAEZ_2026_SNAPSHOT, ARRAEZ_SEASONS, ARRAEZ_CAREER
    print("=== Luis Arraez — Baseball Savant, 2019-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(ARRAEZ_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (8 temporadas reales): EV {ARRAEZ_CAREER['exit_velo']}mph · "
          f"Barrel% {ARRAEZ_CAREER['barrel_pct']} · xwOBA {ARRAEZ_CAREER['xwoba']}")
    s = ARRAEZ_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_kwan_savant():
    from kwan_savant_2026 import KWAN_2026_SNAPSHOT, KWAN_SEASONS, KWAN_CAREER
    print("=== Steven Kwan — Baseball Savant, 2022-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(KWAN_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (5 temporadas reales): EV {KWAN_CAREER['exit_velo']}mph · "
          f"Barrel% {KWAN_CAREER['barrel_pct']} · xwOBA {KWAN_CAREER['xwoba']}")
    s = KWAN_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_hoerner_savant():
    from hoerner_savant_2026 import HOERNER_2026_SNAPSHOT, HOERNER_SEASONS, HOERNER_CAREER
    print("=== Nico Hoerner — Baseball Savant, 2019-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(HOERNER_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (8 temporadas reales): EV {HOERNER_CAREER['exit_velo']}mph · "
          f"Barrel% {HOERNER_CAREER['barrel_pct']} · xwOBA {HOERNER_CAREER['xwoba']}")
    s = HOERNER_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_altuve_savant():
    from altuve_savant_2026 import ALTUVE_2026_SNAPSHOT, ALTUVE_SEASONS, ALTUVE_CAREER
    print("=== Jose Altuve — Baseball Savant, 2015-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(ALTUVE_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (12 temporadas reales): EV {ALTUVE_CAREER['exit_velo']}mph · "
          f"Barrel% {ALTUVE_CAREER['barrel_pct']} · xwOBA {ALTUVE_CAREER['xwoba']}")
    s = ALTUVE_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_freeman_savant():
    from freeman_savant_2026 import FREEMAN_2026_SNAPSHOT, FREEMAN_SEASONS, FREEMAN_CAREER
    print("=== Freddie Freeman — Baseball Savant, 2015-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(FREEMAN_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (12 temporadas reales): EV {FREEMAN_CAREER['exit_velo']}mph · "
          f"Barrel% {FREEMAN_CAREER['barrel_pct']} · xwOBA {FREEMAN_CAREER['xwoba']}")
    s = FREEMAN_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_soto_savant():
    from soto_savant_2026 import SOTO_2026_SNAPSHOT, SOTO_SEASONS, SOTO_CAREER
    print("=== Juan Soto — Baseball Savant, 2018-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(SOTO_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (9 temporadas reales): EV {SOTO_CAREER['exit_velo']}mph · "
          f"Barrel% {SOTO_CAREER['barrel_pct']} · xwOBA {SOTO_CAREER['xwoba']}")
    s = SOTO_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_witt_savant():
    from witt_savant_2026 import WITT_2026_SNAPSHOT, WITT_SEASONS, WITT_CAREER
    print("=== Bobby Witt Jr. — Baseball Savant, 2022-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(WITT_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (5 temporadas reales): EV {WITT_CAREER['exit_velo']}mph · "
          f"Barrel% {WITT_CAREER['barrel_pct']} · xwOBA {WITT_CAREER['xwoba']}")
    s = WITT_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_acuna_savant():
    from acuna_savant_2026 import ACUNA_2026_SNAPSHOT, ACUNA_SEASONS, ACUNA_CAREER
    print("=== Ronald Acuna Jr. — Baseball Savant, 2018-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(ACUNA_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (9 temporadas reales): EV {ACUNA_CAREER['exit_velo']}mph · "
          f"Barrel% {ACUNA_CAREER['barrel_pct']} · xwOBA {ACUNA_CAREER['xwoba']}")
    s = ACUNA_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (NOT QUALIFIED — sin percentil en 2026)")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (NOT QUALIFIED — sin percentil en 2026)")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_carroll_savant():
    from carroll_savant_2026 import CARROLL_2026_SNAPSHOT, CARROLL_SEASONS, CARROLL_CAREER
    print("=== Corbin Carroll — Baseball Savant, 2022-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(CARROLL_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (5 temporadas reales): EV {CARROLL_CAREER['exit_velo']}mph · "
          f"Barrel% {CARROLL_CAREER['barrel_pct']} · xwOBA {CARROLL_CAREER['xwoba']}")
    s = CARROLL_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_henderson_savant():
    from henderson_savant_2026 import HENDERSON_2026_SNAPSHOT, HENDERSON_SEASONS, HENDERSON_CAREER
    print("=== Gunnar Henderson — Baseball Savant, 2022-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(HENDERSON_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (5 temporadas reales): EV {HENDERSON_CAREER['exit_velo']}mph · "
          f"Barrel% {HENDERSON_CAREER['barrel_pct']} · xwOBA {HENDERSON_CAREER['xwoba']}")
    s = HENDERSON_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_rutschman_savant():
    from rutschman_savant_2026 import RUTSCHMAN_2026_SNAPSHOT, RUTSCHMAN_SEASONS, RUTSCHMAN_CAREER
    print("=== Adley Rutschman — Baseball Savant, 2022-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(RUTSCHMAN_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (5 temporadas reales): EV {RUTSCHMAN_CAREER['exit_velo']}mph · "
          f"Barrel% {RUTSCHMAN_CAREER['barrel_pct']} · xwOBA {RUTSCHMAN_CAREER['xwoba']}")
    s = RUTSCHMAN_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_turang_savant():
    from turang_savant_2026 import TURANG_2026_SNAPSHOT, TURANG_SEASONS, TURANG_CAREER
    print("=== Brice Turang — Baseball Savant, 2023-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(TURANG_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (4 temporadas reales): EV {TURANG_CAREER['exit_velo']}mph · "
          f"Barrel% {TURANG_CAREER['barrel_pct']} · xwOBA {TURANG_CAREER['xwoba']}")
    s = TURANG_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_abreu_savant():
    from abreu_savant_2026 import ABREU_2026_SNAPSHOT, ABREU_SEASONS, ABREU_CAREER
    print("=== Wilyer Abreu — Baseball Savant, 2023-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(ABREU_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (4 temporadas reales): EV {ABREU_CAREER['exit_velo']}mph · "
          f"Barrel% {ABREU_CAREER['barrel_pct']} · xwOBA {ABREU_CAREER['xwoba']}")
    s = ABREU_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_caminero_savant():
    from caminero_savant_2026 import CAMINERO_2026_SNAPSHOT, CAMINERO_SEASONS, CAMINERO_CAREER
    print("=== Junior Caminero — Baseball Savant, 2023-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(CAMINERO_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (4 temporadas reales): EV {CAMINERO_CAREER['exit_velo']}mph · "
          f"Barrel% {CAMINERO_CAREER['barrel_pct']} · xwOBA {CAMINERO_CAREER['xwoba']}")
    s = CAMINERO_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_wood_savant():
    from wood_savant_2026 import WOOD_2026_SNAPSHOT, WOOD_SEASONS, WOOD_CAREER
    print("=== James Wood — Baseball Savant, 2024-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(WOOD_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (3 temporadas reales): EV {WOOD_CAREER['exit_velo']}mph · "
          f"Barrel% {WOOD_CAREER['barrel_pct']} · xwOBA {WOOD_CAREER['xwoba']}")
    s = WOOD_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_chourio_savant():
    from chourio_savant_2026 import CHOURIO_2026_SNAPSHOT, CHOURIO_SEASONS, CHOURIO_CAREER
    print("=== Jackson Chourio — Baseball Savant, 2024-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(CHOURIO_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (3 temporadas reales): EV {CHOURIO_CAREER['exit_velo']}mph · "
          f"Barrel% {CHOURIO_CAREER['barrel_pct']} · xwOBA {CHOURIO_CAREER['xwoba']}")
    s = CHOURIO_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_merrill_savant():
    from merrill_savant_2026 import MERRILL_2026_SNAPSHOT, MERRILL_SEASONS, MERRILL_CAREER
    print("=== Jackson Merrill — Baseball Savant, 2024-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(MERRILL_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (3 temporadas reales): EV {MERRILL_CAREER['exit_velo']}mph · "
          f"Barrel% {MERRILL_CAREER['barrel_pct']} · xwOBA {MERRILL_CAREER['xwoba']}")
    s = MERRILL_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_dominguez_savant():
    from dominguez_savant_2026 import DOMINGUEZ_2026_SNAPSHOT, DOMINGUEZ_SEASONS, DOMINGUEZ_CAREER
    print("=== Jasson Dominguez — Baseball Savant, 2023-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(DOMINGUEZ_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (4 temporadas reales): EV {DOMINGUEZ_CAREER['exit_velo']}mph · "
          f"Barrel% {DOMINGUEZ_CAREER['barrel_pct']} · xwOBA {DOMINGUEZ_CAREER['xwoba']}")
    s = DOMINGUEZ_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real (casi todo NOT QUALIFIED, muestra chica) ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (sin percentil — NOT QUALIFIED)")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (sin percentil — NOT QUALIFIED)")
    print(f"  xwOBA:          {s['xwoba']}  (sin percentil — NOT QUALIFIED)")
    print(f"  Arm Strength:   {s['arm_strength']} mph  (percentil {s['arm_strength_pctl']}, único campo calificado)")
    print()


def validate_walker_savant():
    from walker_savant_2026 import WALKER_2026_SNAPSHOT, WALKER_SEASONS, WALKER_CAREER
    print("=== Jordan Walker — Baseball Savant, 2023-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(WALKER_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (4 temporadas reales): EV {WALKER_CAREER['exit_velo']}mph · "
          f"Barrel% {WALKER_CAREER['barrel_pct']} · xwOBA {WALKER_CAREER['xwoba']}")
    s = WALKER_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_langford_savant():
    from langford_savant_2026 import LANGFORD_2026_SNAPSHOT, LANGFORD_SEASONS, LANGFORD_CAREER
    print("=== Wyatt Langford — Baseball Savant, 2024-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(LANGFORD_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (3 temporadas reales): EV {LANGFORD_CAREER['exit_velo']}mph · "
          f"Barrel% {LANGFORD_CAREER['barrel_pct']} · xwOBA {LANGFORD_CAREER['xwoba']}")
    s = LANGFORD_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real (Bat Speed / Squared-Up% NOT QUALIFIED) ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (sin percentil — NOT QUALIFIED)")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (sin percentil — NOT QUALIFIED)")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_turner_savant():
    from turner_savant_2026 import TURNER_2026_SNAPSHOT, TURNER_SEASONS, TURNER_CAREER
    print("=== Trea Turner — Baseball Savant, 2015-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(TURNER_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (12 temporadas reales): EV {TURNER_CAREER['exit_velo']}mph · "
          f"Barrel% {TURNER_CAREER['barrel_pct']} · xwOBA {TURNER_CAREER['xwoba']}")
    s = TURNER_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


def validate_lindor_savant():
    from lindor_savant_2026 import LINDOR_2026_SNAPSHOT, LINDOR_SEASONS, LINDOR_CAREER
    print("=== Francisco Lindor — Baseball Savant, 2015-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(LINDOR_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (12 temporadas reales): EV {LINDOR_CAREER['exit_velo']}mph · "
          f"Barrel% {LINDOR_CAREER['barrel_pct']} · xwOBA {LINDOR_CAREER['xwoba']}")
    s = LINDOR_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real (mayoría NOT QUALIFIED, muestra chica) ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (sin percentil — NOT QUALIFIED)")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (sin percentil — NOT QUALIFIED)")
    print(f"  xwOBA:          {s['xwoba']}  (sin percentil — NOT QUALIFIED)")
    print(f"  Fielding Run Value: {s['fielding_run_value']}  (percentil {s['fielding_run_value_pctl']}, único campo calificado)")
    print()


def validate_abrams_savant():
    from abrams_savant_2026 import ABRAMS_2026_SNAPSHOT, ABRAMS_SEASONS, ABRAMS_CAREER
    print("=== CJ Abrams — Baseball Savant, 2022-2026 (transcrito de capturas reales) ===\n")
    seasons = pd.DataFrame(ABRAMS_SEASONS)
    print(seasons[["season", "exit_velo", "barrel_pct", "xwoba", "hard_hit_pct", "k_pct", "bb_pct"]]
          .to_string(index=False))
    print(f"\nCareer (5 temporadas reales): EV {ABRAMS_CAREER['exit_velo']}mph · "
          f"Barrel% {ABRAMS_CAREER['barrel_pct']} · xwOBA {ABRAMS_CAREER['xwoba']}")
    s = ABRAMS_2026_SNAPSHOT
    print(f"\n--- 2026 Bat-Tracking real ---")
    print(f"  Bat Speed:      {s['bat_speed']} mph  (percentil {s['bat_speed_pctl']})")
    print(f"  Squared-Up%:    {s['squared_up_pct']}%  (percentil {s['squared_up_pct_pctl']})")
    print(f"  xwOBA:          {s['xwoba']}  (percentil {s['xwoba_pctl']})")
    print(f"  Barrel%:        {s['barrel_pct']}%  (percentil {s['barrel_pct_pctl']})")
    print()


if __name__ == "__main__":
    validate_github_samples()
    validate_judge_savant()
    validate_stanton_savant()
    validate_cruz_savant()
    validate_tatis_savant()
    validate_schwarber_savant()
    validate_alonso_savant()
    validate_alvarez_savant()
    validate_delacruz_savant()
    validate_arraez_savant()
    validate_kwan_savant()
    validate_hoerner_savant()
    validate_altuve_savant()
    validate_freeman_savant()
    validate_soto_savant()
    validate_witt_savant()
    validate_acuna_savant()
    validate_carroll_savant()
    validate_henderson_savant()
    validate_rutschman_savant()
    validate_turang_savant()
    validate_abreu_savant()
    validate_caminero_savant()
    validate_wood_savant()
    validate_chourio_savant()
    validate_merrill_savant()
    validate_dominguez_savant()
    validate_walker_savant()
    validate_langford_savant()
    validate_turner_savant()
    validate_lindor_savant()
    validate_abrams_savant()
    compare_real_bat_tracking()
