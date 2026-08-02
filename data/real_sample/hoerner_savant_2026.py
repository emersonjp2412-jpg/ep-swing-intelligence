"""
data/real_sample/hoerner_savant_2026.py
----------------------------------------
Real Baseball Savant data for Nico Hoerner, transcribed by hand from
screenshots the user captured directly from the Savant app. Third
pure-contact data point alongside Arraez and Kwan: elite Squared-Up%
(98th) and K% (99th) paired with bottom-of-the-league Bat Speed (6th)
and Barrel% (2nd) -- the clearest bat-speed/contact tradeoff case in
the roster. 2026 shows real in-season decline vs. 2025 (BA -.053,
Barrel% -1.6pts), useful variance for the model beyond peak-season snapshots.
"""

HOERNER_2026_SNAPSHOT = {
    "player_name": "Nico Hoerner",
    "season": 2026,
    "batting_run_value": -9, "batting_run_value_pctl": 11,
    "xwoba": 0.321, "xwoba_pctl": 52,
    "xba": 0.293, "xba_pctl": 96,
    "xslg": 0.368, "xslg_pctl": 27,
    "avg_exit_velo": 86.1, "avg_exit_velo_pctl": 9,
    "barrel_pct": 0.8, "barrel_pct_pctl": 2,
    "hard_hit_pct": 28.2, "hard_hit_pct_pctl": 8,
    "la_sweet_spot_pct": 37.2, "la_sweet_spot_pct_pctl": 78,
    "bat_speed": 68.3, "bat_speed_pctl": 6,
    "squared_up_pct": 36.1, "squared_up_pct_pctl": 98,
    "chase_pct": 31.0, "chase_pct_pctl": 42,
    "whiff_pct": 11.9, "whiff_pct_pctl": 98,
    "k_pct": 8.4, "k_pct_pctl": 99,
    "bb_pct": 7.9, "bb_pct_pctl": 37,
    "sprint_speed": 28.4, "sprint_speed_pctl": 79,
}

HOERNER_SEASONS = [
    dict(season=2019, age=22, pitches=298, batted_balls=68, barrels=1, barrel_pct=1.7,
         barrel_per_pa=1.2, exit_velo=85.6, max_ev=103.4, launch_angle=3.9, la_sweet_spot_pct=36.8,
         xba=.309, xslg=.401, woba=.305, xwoba=.315, xwobacon=.355, hard_hit_pct=23.5, k_pct=13.4, bb_pct=3.7),
    dict(season=2020, age=23, pitches=523, batted_balls=86, barrels=1, barrel_pct=1.2,
         barrel_per_pa=0.8, exit_velo=87.5, max_ev=106.7, launch_angle=0.8, la_sweet_spot_pct=27.9,
         xba=.243, xslg=.315, woba=.265, xwoba=.297, xwobacon=.309, hard_hit_pct=37.2, k_pct=19.0, bb_pct=9.5),
    dict(season=2021, age=24, pitches=650, batted_balls=125, barrels=2, barrel_pct=1.6,
         barrel_per_pa=1.2, exit_velo=87.0, max_ev=107.8, launch_angle=7.7, la_sweet_spot_pct=31.2,
         xba=.278, xslg=.364, woba=.330, xwoba=.322, xwobacon=.335, hard_hit_pct=34.4, k_pct=14.7, bb_pct=10.0),
    dict(season=2022, age=25, pitches=1831, batted_balls=426, barrels=11, barrel_pct=2.6,
         barrel_per_pa=2.1, exit_velo=87.2, max_ev=109.7, launch_angle=10.6, la_sweet_spot_pct=32.4,
         xba=.273, xslg=.384, woba=.320, xwoba=.309, xwobacon=.323, hard_hit_pct=33.5, k_pct=11.0, bb_pct=5.4),
    dict(season=2023, age=26, pitches=2539, batted_balls=542, barrels=10, barrel_pct=1.8,
         barrel_per_pa=1.5, exit_velo=86.6, max_ev=109.2, launch_angle=10.5, la_sweet_spot_pct=33.2,
         xba=.272, xslg=.361, woba=.322, xwoba=.313, xwobacon=.316, hard_hit_pct=33.4, k_pct=12.1, bb_pct=7.1),
    dict(season=2024, age=27, pitches=2314, batted_balls=519, barrels=6, barrel_pct=1.2,
         barrel_per_pa=0.9, exit_velo=85.7, max_ev=110.1, launch_angle=10.4, la_sweet_spot_pct=36.0,
         xba=.281, xslg=.359, woba=.313, xwoba=.318, xwobacon=.318, hard_hit_pct=27.6, k_pct=10.3, bb_pct=6.9),
    dict(season=2025, age=28, pitches=2305, batted_balls=554, barrels=13, barrel_pct=2.4,
         barrel_per_pa=2.0, exit_velo=86.7, max_ev=108.1, launch_angle=12.5, la_sweet_spot_pct=36.1,
         xba=.292, xslg=.391, woba=.324, xwoba=.322, xwobacon=.320, hard_hit_pct=30.3, k_pct=7.6, bb_pct=6.0),
    dict(season=2026, age=29, pitches=1623, batted_balls=376, barrels=3, barrel_pct=0.8,
         barrel_per_pa=0.7, exit_velo=86.1, max_ev=105.8, launch_angle=13.2, la_sweet_spot_pct=37.2,
         xba=.293, xslg=.368, woba=.289, xwoba=.321, xwobacon=.312, hard_hit_pct=28.2, k_pct=8.4, bb_pct=7.9),
]

HOERNER_CAREER = dict(
    pitches=12083, batted_balls=2696, barrels=47, barrel_pct=1.8, barrel_per_pa=1.4,
    exit_velo=86.5, max_ev=110.1, launch_angle=10.7, la_sweet_spot_pct=34.6,
    xba=.281, xslg=.371, woba=.314, xwoba=.316, xwobacon=.320, hard_hit_pct=30.8, k_pct=10.6, bb_pct=6.9,
)

# Reference row from the same screenshot, MLB league average across the
# 2015-present window covered by the table (not Hoerner-specific).
MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, max_ev=122.9, launch_angle=12.5,
    la_sweet_spot_pct=33.3, xba=.243, xslg=.407, woba=.316, xwoba=.316, xwobacon=.369,
    hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
