"""
data/real_sample/witt_savant_2026.py
----------------------------------------
Real Baseball Savant data for Bobby Witt Jr., transcribed by hand from
screenshots the user captured directly from the Savant app. Second
"balance" profile: above-average Bat Speed (70th) paired with plus
Squared-Up% (80th) and elite two-way value (Fielding Run Value 99th,
Baserunning 98th, Range OAA 100th) -- a five-tool shape rather than a
bat-only one, useful contrast against Soto's pure-hitter balance case.
"""

WITT_2026_SNAPSHOT = {
    "player_name": "Bobby Witt Jr.",
    "season": 2026,
    "batting_run_value": 12, "batting_run_value_pctl": 81,
    "xwoba": 0.386, "xwoba_pctl": 97,
    "xba": 0.306, "xba_pctl": 99,
    "xslg": 0.517, "xslg_pctl": 95,
    "avg_exit_velo": 92.9, "avg_exit_velo_pctl": 95,
    "barrel_pct": 12.2, "barrel_pct_pctl": 80,
    "hard_hit_pct": 52.2, "hard_hit_pct_pctl": 94,
    "la_sweet_spot_pct": 38.1, "la_sweet_spot_pct_pctl": 85,
    "bat_speed": 73.8, "bat_speed_pctl": 70,
    "squared_up_pct": 28.6, "squared_up_pct_pctl": 80,
    "chase_pct": 33.0, "chase_pct_pctl": 29,
    "whiff_pct": 24.8, "whiff_pct_pctl": 47,
    "k_pct": 17.6, "k_pct_pctl": 72,
    "bb_pct": 9.9, "bb_pct_pctl": 62,
    "sprint_speed": 30.3, "sprint_speed_pctl": 99,
}

WITT_SEASONS = [
    dict(season=2022, age=22, pitches=2332, batted_balls=461, barrels=40, barrel_pct=8.7,
         barrel_per_pa=6.3, exit_velo=89.7, max_ev=113.7, launch_angle=16.8, la_sweet_spot_pct=32.5,
         xba=.252, xslg=.444, woba=.311, xwoba=.318, xwobacon=.384, hard_hit_pct=38.6, k_pct=21.4, bb_pct=4.7),
    dict(season=2023, age=23, pitches=2701, batted_balls=529, barrels=61, barrel_pct=11.6,
         barrel_per_pa=8.8, exit_velo=90.7, max_ev=113.8, launch_angle=15.7, la_sweet_spot_pct=34.4,
         xba=.289, xslg=.534, woba=.343, xwoba=.368, xwobacon=.425, hard_hit_pct=45.6, k_pct=17.4, bb_pct=5.8),
    dict(season=2024, age=24, pitches=2600, batted_balls=538, barrels=77, barrel_pct=14.3,
         barrel_per_pa=10.9, exit_velo=92.7, max_ev=116.9, launch_angle=15.1, la_sweet_spot_pct=35.7,
         xba=.309, xslg=.583, woba=.410, xwoba=.407, xwobacon=.457, hard_hit_pct=48.3, k_pct=15.0, bb_pct=8.0),
    dict(season=2025, age=25, pitches=2511, batted_balls=505, barrels=63, barrel_pct=12.5,
         barrel_per_pa=9.2, exit_velo=93.3, max_ev=117.5, launch_angle=15.2, la_sweet_spot_pct=35.4,
         xba=.285, xslg=.508, woba=.360, xwoba=.365, xwobacon=.424, hard_hit_pct=48.5, k_pct=18.2, bb_pct=7.1),
    dict(season=2026, age=26, pitches=1526, batted_balls=299, barrels=36, barrel_pct=12.2,
         barrel_per_pa=8.7, exit_velo=92.9, max_ev=117.2, launch_angle=16.6, la_sweet_spot_pct=38.1,
         xba=.306, xslg=.517, woba=.346, xwoba=.386, xwobacon=.441, hard_hit_pct=52.2, k_pct=17.6, bb_pct=9.9),
]

WITT_CAREER = dict(
    pitches=11670, batted_balls=2332, barrels=277, barrel_pct=11.9, barrel_per_pa=8.8,
    exit_velo=91.8, max_ev=117.5, launch_angle=15.8, la_sweet_spot_pct=35.0,
    xba=.287, xslg=.518, woba=.356, xwoba=.368, xwobacon=.426, hard_hit_pct=46.3, k_pct=17.9, bb_pct=6.9,
)
