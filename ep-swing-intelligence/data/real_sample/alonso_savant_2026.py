"""
data/real_sample/alonso_savant_2026.py
-----------------------------------------
Real Baseball Savant data for Pete Alonso, transcribed by hand from
screenshots the user captured directly from the Savant app.
"""

ALONSO_2026_SNAPSHOT = {
    "player_name": "Pete Alonso",
    "season": 2026,
    "batting_run_value": 13, "batting_run_value_pctl": 84,
    "xwoba": 0.378, "xwoba_pctl": 94,
    "xba": 0.273, "xba_pctl": 83,
    "xslg": 0.509, "xslg_pctl": 93,
    "avg_exit_velo": 93.9, "avg_exit_velo_pctl": 98,
    "barrel_pct": 12.3, "barrel_pct_pctl": 81,
    "hard_hit_pct": 54.6, "hard_hit_pct_pctl": 97,
    "la_sweet_spot_pct": 34.9, "la_sweet_spot_pct_pctl": 58,
    "bat_speed": 74.7, "bat_speed_pctl": 79,
    "squared_up_pct": 23.8, "squared_up_pct_pctl": 39,
    "chase_pct": 26.7, "chase_pct_pctl": 68,
    "whiff_pct": 27.5, "whiff_pct_pctl": 34,
    "k_pct": 24.7, "k_pct_pctl": 30,
    "bb_pct": 11.8, "bb_pct_pctl": 81,
    "sprint_speed": 25.3, "sprint_speed_pctl": 8,
}

ALONSO_SEASONS = [
    dict(season=2019, age=24, pitches=2762, batted_balls=417, barrels=66, barrel_pct=17.4,
         barrel_per_pa=9.5, exit_velo=90.7, max_ev=118.3, launch_angle=14.8, la_sweet_spot_pct=36.9,
         xba=.257, xslg=.551, woba=.384, xwoba=.380, xwobacon=.482, hard_hit_pct=42.7, k_pct=26.4, bb_pct=10.4),
    dict(season=2020, age=25, pitches=929, batted_balls=148, barrels=19, barrel_pct=13.1,
         barrel_per_pa=7.9, exit_velo=90.2, max_ev=118.4, launch_angle=15.5, la_sweet_spot_pct=30.4,
         xba=.225, xslg=.463, woba=.342, xwoba=.334, xwobacon=.407, hard_hit_pct=41.2, k_pct=25.5, bb_pct=10.0),
    dict(season=2021, age=26, pitches=2298, batted_balls=438, barrels=65, barrel_pct=14.9,
         barrel_per_pa=10.2, exit_velo=91.0, max_ev=118.4, launch_angle=14.7, la_sweet_spot_pct=34.5,
         xba=.264, xslg=.547, woba=.363, xwoba=.376, xwobacon=.437, hard_hit_pct=47.3, k_pct=19.9, bb_pct=9.4),
    dict(season=2022, age=27, pitches=2507, batted_balls=478, barrels=59, barrel_pct=12.3,
         barrel_per_pa=8.6, exit_velo=89.8, max_ev=116.5, launch_angle=18.2, la_sweet_spot_pct=34.5,
         xba=.258, xslg=.506, woba=.366, xwoba=.357, xwobacon=.407, hard_hit_pct=44.8, k_pct=18.7, bb_pct=9.8),
    dict(season=2023, age=28, pitches=2567, batted_balls=421, barrels=62, barrel_pct=14.7,
         barrel_per_pa=9.4, exit_velo=89.5, max_ev=115.7, launch_angle=18.2, la_sweet_spot_pct=32.3,
         xba=.242, xslg=.534, woba=.346, xwoba=.369, xwobacon=.438, hard_hit_pct=40.1, k_pct=22.9, bb_pct=9.9),
    dict(season=2024, age=29, pitches=2780, batted_balls=440, barrels=58, barrel_pct=13.2,
         barrel_per_pa=8.3, exit_velo=89.8, max_ev=116.3, launch_angle=14.4, la_sweet_spot_pct=30.5,
         xba=.239, xslg=.470, woba=.340, xwoba=.345, xwobacon=.418, hard_hit_pct=46.4, k_pct=24.7, bb_pct=10.1),
    dict(season=2025, age=30, pitches=2807, batted_balls=471, barrels=89, barrel_pct=18.9,
         barrel_per_pa=12.6, exit_velo=93.5, max_ev=115.9, launch_angle=15.4, la_sweet_spot_pct=38.4,
         xba=.274, xslg=.572, woba=.368, xwoba=.386, xwobacon=.471, hard_hit_pct=54.4, k_pct=22.8, bb_pct=8.6),
    dict(season=2026, age=31, pitches=1893, batted_balls=284, barrels=35, barrel_pct=12.3,
         barrel_per_pa=7.7, exit_velo=93.9, max_ev=114.6, launch_angle=14.7, la_sweet_spot_pct=34.9,
         xba=.273, xslg=.509, woba=.348, xwoba=.378, xwobacon=.462, hard_hit_pct=54.6, k_pct=24.7, bb_pct=11.8),
]

ALONSO_CAREER = dict(
    pitches=18543, batted_balls=3097, barrels=453, barrel_pct=14.8, barrel_per_pa=9.5,
    exit_velo=91.0, max_ev=118.4, launch_angle=15.8, la_sweet_spot_pct=34.4,
    xba=.256, xslg=.524, woba=.359, xwoba=.368, xwobacon=.442, hard_hit_pct=46.6, k_pct=23.0, bb_pct=9.9,
)
