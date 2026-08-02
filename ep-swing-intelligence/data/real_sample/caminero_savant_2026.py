"""
data/real_sample/caminero_savant_2026.py
----------------------------------------
Real Baseball Savant data for Junior Caminero, transcribed by hand from
screenshots the user captured directly from the Savant app. The third
EP-TSP case-study player. The single most extreme Bat Speed reading in
the whole roster (79.8 mph, 100th percentile) paired with a bottom-decile
LA Sweet-Spot% (9th) and poor Fielding Run Value (1st, -15 Range OAA) --
pure, still-developing raw power without the swing-plane efficiency of
the other power-group players yet.
"""

CAMINERO_2026_SNAPSHOT = {
    "player_name": "Junior Caminero",
    "season": 2026,
    "batting_run_value": 28, "batting_run_value_pctl": 98,
    "xwoba": 0.373, "xwoba_pctl": 92,
    "xba": 0.280, "xba_pctl": 87,
    "xslg": 0.506, "xslg_pctl": 92,
    "avg_exit_velo": 93.1, "avg_exit_velo_pctl": 96,
    "barrel_pct": 13.4, "barrel_pct_pctl": 87,
    "hard_hit_pct": 51.4, "hard_hit_pct_pctl": 92,
    "la_sweet_spot_pct": 28.7, "la_sweet_spot_pct_pctl": 9,
    "bat_speed": 79.8, "bat_speed_pctl": 100,
    "squared_up_pct": 24.3, "squared_up_pct_pctl": 44,
    "chase_pct": 28.5, "chase_pct_pctl": 60,
    "whiff_pct": 22.7, "whiff_pct_pctl": 58,
    "k_pct": 18.4, "k_pct_pctl": 67,
    "bb_pct": 12.5, "bb_pct_pctl": 86,
    "sprint_speed": 26.3, "sprint_speed_pctl": 25,
}

CAMINERO_SEASONS = [
    dict(season=2023, age=19, pitches=134, batted_balls=26, barrels=3, barrel_pct=11.5,
         barrel_per_pa=8.3, exit_velo=85.4, max_ev=112.0, launch_angle=-0.3, la_sweet_spot_pct=15.4,
         xba=.202, xslg=.344, woba=.276, xwoba=.259, xwobacon=.305, hard_hit_pct=42.3, k_pct=22.2, bb_pct=5.6),
    dict(season=2024, age=20, pitches=629, batted_balls=127, barrels=15, barrel_pct=11.8,
         barrel_per_pa=8.5, exit_velo=89.7, max_ev=116.3, launch_angle=6.8, la_sweet_spot_pct=25.2,
         xba=.234, xslg=.412, woba=.309, xwoba=.303, xwobacon=.364, hard_hit_pct=45.7, k_pct=21.5, bb_pct=6.2),
    dict(season=2025, age=21, pitches=2494, batted_balls=484, barrels=68, barrel_pct=14.0,
         barrel_per_pa=10.4, exit_velo=92.4, max_ev=116.7, launch_angle=10.7, la_sweet_spot_pct=27.7,
         xba=.255, xslg=.501, woba=.357, xwoba=.346, xwobacon=.404, hard_hit_pct=51.4, k_pct=19.1, bb_pct=6.3),
    dict(season=2026, age=22, pitches=1767, batted_balls=314, barrels=42, barrel_pct=13.4,
         barrel_per_pa=9.2, exit_velo=93.1, max_ev=116.9, launch_angle=9.2, la_sweet_spot_pct=28.7,
         xba=.280, xslg=.506, woba=.391, xwoba=.373, xwobacon=.421, hard_hit_pct=51.4, k_pct=18.4, bb_pct=12.5),
]

CAMINERO_CAREER = dict(
    pitches=5024, batted_balls=951, barrels=128, barrel_pct=13.5, barrel_per_pa=9.7,
    exit_velo=92.1, max_ev=116.9, launch_angle=9.4, la_sweet_spot_pct=27.3,
    xba=.259, xslg=.486, woba=.360, xwoba=.347, xwobacon=.402, hard_hit_pct=50.4, k_pct=19.3, bb_pct=8.4,
)
