"""
data/real_sample/carroll_savant_2026.py
----------------------------------------
Real Baseball Savant data for Corbin Carroll, transcribed by hand from
screenshots the user captured directly from the Savant app. Bat Speed
90th pctl with only average Squared-Up% (42nd) -- a young power/speed
profile still ahead of his contact-quality peak, useful contrast with
Witt Jr.'s more even split between the two.
"""

CARROLL_2026_SNAPSHOT = {
    "player_name": "Corbin Carroll",
    "season": 2026,
    "batting_run_value": 14, "batting_run_value_pctl": 85,
    "xwoba": 0.346, "xwoba_pctl": 73,
    "xba": 0.249, "xba_pctl": 47,
    "xslg": 0.448, "xslg_pctl": 74,
    "avg_exit_velo": 91.5, "avg_exit_velo_pctl": 84,
    "barrel_pct": 12.4, "barrel_pct_pctl": 81,
    "hard_hit_pct": 47.3, "hard_hit_pct_pctl": 83,
    "la_sweet_spot_pct": 28.0, "la_sweet_spot_pct_pctl": 7,
    "bat_speed": 75.5, "bat_speed_pctl": 90,
    "squared_up_pct": 24.1, "squared_up_pct_pctl": 42,
    "chase_pct": 30.3, "chase_pct_pctl": 47,
    "whiff_pct": 28.5, "whiff_pct_pctl": 29,
    "k_pct": 23.0, "k_pct_pctl": 42,
    "bb_pct": 11.5, "bb_pct_pctl": 76,
    "sprint_speed": 29.7, "sprint_speed_pctl": 97,
}

CARROLL_SEASONS = [
    dict(season=2022, age=21, pitches=458, batted_balls=73, barrels=4, barrel_pct=5.5,
         barrel_per_pa=3.5, exit_velo=85.8, max_ev=107.5, launch_angle=9.1, la_sweet_spot_pct=34.2,
         xba=.222, xslg=.372, woba=.358, xwoba=.297, xwobacon=.363, hard_hit_pct=32.9, k_pct=27.0, bb_pct=7.0),
    dict(season=2023, age=22, pitches=2431, batted_balls=450, barrels=34, barrel_pct=7.6,
         barrel_per_pa=5.3, exit_velo=90.0, max_ev=113.8, launch_angle=11.0, la_sweet_spot_pct=32.7,
         xba=.264, xslg=.445, woba=.370, xwoba=.345, xwobacon=.387, hard_hit_pct=40.9, k_pct=19.4, bb_pct=8.8),
    dict(season=2024, age=23, pitches=2648, batted_balls=471, barrels=34, barrel_pct=7.2,
         barrel_per_pa=5.0, exit_velo=89.3, max_ev=111.5, launch_angle=12.0, la_sweet_spot_pct=27.8,
         xba=.239, xslg=.401, woba=.325, xwoba=.328, xwobacon=.355, hard_hit_pct=40.8, k_pct=19.0, bb_pct=10.7),
    dict(season=2025, age=24, pitches=2497, batted_balls=415, barrels=60, barrel_pct=14.5,
         barrel_per_pa=9.3, exit_velo=92.1, max_ev=115.8, launch_angle=16.7, la_sweet_spot_pct=33.5,
         xba=.262, xslg=.529, woba=.371, xwoba=.372, xwobacon=.455, hard_hit_pct=49.9, k_pct=23.8, bb_pct=10.4),
    dict(season=2026, age=25, pitches=1711, batted_balls=279, barrels=34, barrel_pct=12.4,
         barrel_per_pa=7.8, exit_velo=91.5, max_ev=112.9, launch_angle=13.7, la_sweet_spot_pct=28.0,
         xba=.249, xslg=.448, woba=.356, xwoba=.346, xwobacon=.403, hard_hit_pct=47.3, k_pct=23.0, bb_pct=11.5),
]

CARROLL_CAREER = dict(
    pitches=9745, batted_balls=1688, barrels=166, barrel_pct=9.9, barrel_per_pa=6.6,
    exit_velo=90.4, max_ev=115.8, launch_angle=13.0, la_sweet_spot_pct=30.8,
    xba=.253, xslg=.452, woba=.355, xwoba=.345, xwobacon=.396, hard_hit_pct=43.8, k_pct=21.4, bb_pct=10.1,
)
