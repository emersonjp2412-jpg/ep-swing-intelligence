"""
data/real_sample/cruz_savant_2026.py
--------------------------------------
Real Baseball Savant data for Oneil Cruz, transcribed by hand from
screenshots the user captured directly from the Savant app.
"""

CRUZ_2026_SNAPSHOT = {
    "player_name": "Oneil Cruz",
    "season": 2026,
    "batting_run_value": 12, "batting_run_value_pctl": 81,
    "xwoba": 0.358, "xwoba_pctl": 85,
    "xba": 0.255, "xba_pctl": 57,
    "xslg": 0.490, "xslg_pctl": 87,
    "avg_exit_velo": 96.0, "avg_exit_velo_pctl": 100,
    "barrel_pct": 16.7, "barrel_pct_pctl": 96,
    "hard_hit_pct": 59.2, "hard_hit_pct_pctl": 100,
    "la_sweet_spot_pct": 34.9, "la_sweet_spot_pct_pctl": 58,
    "bat_speed": 78.5, "bat_speed_pctl": 99,
    "squared_up_pct": 21.5, "squared_up_pct_pctl": 22,
    "chase_pct": 32.4, "chase_pct_pctl": 33,
    "whiff_pct": 37.8, "whiff_pct_pctl": 1,
    "k_pct": 34.6, "k_pct_pctl": 1,
    "bb_pct": 10.6, "bb_pct_pctl": 70,
    "sprint_speed": 28.4, "sprint_speed_pctl": 79,
}

CRUZ_SEASONS = [
    dict(season=2021, age=22, pitches=33, batted_balls=5, barrels=2, barrel_pct=40.0,
         barrel_per_pa=22.2, exit_velo=100.5, max_ev=118.2, launch_angle=4.6, la_sweet_spot_pct=40.0,
         xba=.273, xslg=.609, woba=.418, xwoba=.365, xwobacon=.657, hard_hit_pct=80.0, k_pct=44.4, bb_pct=0.0),
    dict(season=2022, age=23, pitches=1459, batted_balls=206, barrels=32, barrel_pct=15.6,
         barrel_per_pa=8.9, exit_velo=91.9, max_ev=122.4, launch_angle=8.3, la_sweet_spot_pct=30.6,
         xba=.217, xslg=.417, woba=.320, xwoba=.303, xwobacon=.437, hard_hit_pct=46.1, k_pct=34.9, bb_pct=7.8),
    dict(season=2023, age=24, pitches=162, batted_balls=25, barrels=1, barrel_pct=4.0,
         barrel_per_pa=2.5, exit_velo=89.5, max_ev=115.8, launch_angle=10.5, la_sweet_spot_pct=20.0,
         xba=.204, xslg=.363, woba=.335, xwoba=.317, xwobacon=.312, hard_hit_pct=36.0, k_pct=20.0, bb_pct=17.5),
    dict(season=2024, age=25, pitches=2381, batted_balls=364, barrels=57, barrel_pct=15.7,
         barrel_per_pa=9.5, exit_velo=95.5, max_ev=121.5, launch_angle=9.8, la_sweet_spot_pct=32.1,
         xba=.259, xslg=.475, woba=.331, xwoba=.344, xwobacon=.469, hard_hit_pct=54.9, k_pct=30.2, bb_pct=8.5),
    dict(season=2025, age=26, pitches=2235, batted_balls=302, barrels=54, barrel_pct=18.0,
         barrel_per_pa=9.9, exit_velo=95.8, max_ev=122.9, launch_angle=8.1, la_sweet_spot_pct=31.5,
         xba=.218, xslg=.425, woba=.295, xwoba=.324, xwobacon=.433, hard_hit_pct=56.6, k_pct=32.0, bb_pct=11.8),
    dict(season=2026, age=27, pitches=1157, batted_balls=152, barrels=25, barrel_pct=16.7,
         barrel_per_pa=8.8, exit_velo=96.0, max_ev=119.0, launch_angle=7.6, la_sweet_spot_pct=34.9,
         xba=.255, xslg=.490, woba=.357, xwoba=.358, xwobacon=.521, hard_hit_pct=59.2, k_pct=34.6, bb_pct=10.6),
]

CRUZ_CAREER = dict(
    pitches=7427, batted_balls=1054, barrels=171, barrel_pct=16.3, barrel_per_pa=9.3,
    exit_velo=94.8, max_ev=122.9, launch_angle=8.7, la_sweet_spot_pct=31.8,
    xba=.237, xslg=.450, woba=.323, xwoba=.332, xwobacon=.457, hard_hit_pct=54.0, k_pct=32.2, bb_pct=9.8,
)
