"""
data/real_sample/turang_savant_2026.py
----------------------------------------
Real Baseball Savant data for Brice Turang, transcribed by hand from
screenshots the user captured directly from the Savant app. One of the
four EP-TSP case-study players (kinetic sequencing / SRI methodology
validation, MLBAM ID 668930) -- adding him here with real bat-tracking
data closes the loop between the earlier EP-TSP scouting work and this
dataset. Bat Speed only 21st pctl but Squared-Up% 67th, consistent with
the "correct sequencing raises effective output despite modest raw bat
speed" finding from the original SRI case study.
"""

TURANG_2026_SNAPSHOT = {
    "player_name": "Brice Turang",
    "season": 2026,
    "batting_run_value": 16, "batting_run_value_pctl": 87,
    "xwoba": 0.350, "xwoba_pctl": 77,
    "xba": 0.258, "xba_pctl": 63,
    "xslg": 0.449, "xslg_pctl": 74,
    "avg_exit_velo": 90.7, "avg_exit_velo_pctl": 75,
    "barrel_pct": 8.7, "barrel_pct_pctl": 55,
    "hard_hit_pct": 43.5, "hard_hit_pct_pctl": 63,
    "la_sweet_spot_pct": 38.1, "la_sweet_spot_pct_pctl": 85,
    "bat_speed": 70.1, "bat_speed_pctl": 21,
    "squared_up_pct": 26.9, "squared_up_pct_pctl": 67,
    "chase_pct": 24.0, "chase_pct_pctl": 85,
    "whiff_pct": 21.7, "whiff_pct_pctl": 65,
    "k_pct": 24.5, "k_pct_pctl": 31,
    "bb_pct": 13.0, "bb_pct_pctl": 88,
    "sprint_speed": 28.6, "sprint_speed_pctl": 85,
}

TURANG_SEASONS = [
    dict(season=2023, age=23, pitches=1795, batted_balls=315, barrels=9, barrel_pct=2.9,
         barrel_per_pa=2.0, exit_velo=85.5, max_ev=108.3, launch_angle=12.6, la_sweet_spot_pct=34.3,
         xba=.222, xslg=.322, woba=.262, xwoba=.275, xwobacon=.306, hard_hit_pct=27.0, k_pct=21.0, bb_pct=8.5),
    dict(season=2024, age=24, pitches=2470, batted_balls=462, barrels=11, barrel_pct=2.4,
         barrel_per_pa=1.8, exit_velo=87.0, max_ev=107.8, launch_angle=6.1, la_sweet_spot_pct=32.0,
         xba=.261, xslg=.346, woba=.294, xwoba=.302, xwobacon=.328, hard_hit_pct=29.7, k_pct=17.0, bb_pct=8.1),
    dict(season=2025, age=25, pitches=2772, batted_balls=441, barrels=35, barrel_pct=8.0,
         barrel_per_pa=5.3, exit_velo=91.1, max_ev=111.2, launch_angle=8.6, la_sweet_spot_pct=35.1,
         xba=.262, xslg=.429, woba=.346, xwoba=.335, xwobacon=.395, hard_hit_pct=47.4, k_pct=22.8, bb_pct=10.0),
    dict(season=2026, age=26, pitches=1885, batted_balls=278, barrels=24, barrel_pct=8.7,
         barrel_per_pa=5.4, exit_velo=90.7, max_ev=109.8, launch_angle=8.3, la_sweet_spot_pct=38.1,
         xba=.258, xslg=.449, woba=.359, xwoba=.350, xwobacon=.419, hard_hit_pct=43.5, k_pct=24.5, bb_pct=13.0),
]

TURANG_CAREER = dict(
    pitches=8922, batted_balls=1496, barrels=79, barrel_pct=5.3, barrel_per_pa=3.6,
    exit_velo=88.6, max_ev=111.2, launch_angle=8.6, la_sweet_spot_pct=34.6,
    xba=.253, xslg=.386, woba=.317, xwoba=.316, xwobacon=.360, hard_hit_pct=36.9, k_pct=21.1, bb_pct=9.8,
)
