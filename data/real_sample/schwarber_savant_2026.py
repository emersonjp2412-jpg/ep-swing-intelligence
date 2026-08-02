"""
data/real_sample/schwarber_savant_2026.py
--------------------------------------------
Real Baseball Savant data for Kyle Schwarber, transcribed by hand from
screenshots the user captured directly from the Savant app. Note: 2016 has
almost no sample (2 batted balls) — real ACL injury season, not a data error.
"""

SCHWARBER_2026_SNAPSHOT = {
    "player_name": "Kyle Schwarber",
    "season": 2026,
    "batting_run_value": 33, "batting_run_value_pctl": 99,
    "xwoba": 0.367, "xwoba_pctl": 90,
    "xba": 0.239, "xba_pctl": 33,
    "xslg": 0.503, "xslg_pctl": 91,
    "avg_exit_velo": 93.3, "avg_exit_velo_pctl": 96,
    "barrel_pct": 18.3, "barrel_pct_pctl": 98,
    "hard_hit_pct": 52.0, "hard_hit_pct_pctl": 94,
    "la_sweet_spot_pct": 39.6, "la_sweet_spot_pct_pctl": 92,
    "bat_speed": 77.1, "bat_speed_pctl": 96,
    "squared_up_pct": 16.9, "squared_up_pct_pctl": 2,
    "chase_pct": 25.7, "chase_pct_pctl": 73,
    "whiff_pct": 34.8, "whiff_pct_pctl": 6,
    "k_pct": 34.7, "k_pct_pctl": 1,
    "bb_pct": 13.9, "bb_pct_pctl": 93,
    "sprint_speed": 25.9, "sprint_speed_pctl": 17,
}

SCHWARBER_SEASONS = [
    dict(season=2015, age=22, pitches=1163, batted_balls=156, barrels=19, barrel_pct=14.3,
         barrel_per_pa=7.0, exit_velo=91.9, max_ev=111.3, launch_angle=15.5, la_sweet_spot_pct=32.1,
         xba=.238, xslg=.482, woba=.364, xwoba=.362, xwobacon=.460, hard_hit_pct=42.3, k_pct=28.2, bb_pct=13.2),
    dict(season=2016, age=23, pitches=28, batted_balls=2, barrels=0, barrel_pct=0.0,
         barrel_per_pa=0.0, exit_velo=101.6, max_ev=108.2, launch_angle=3.1, la_sweet_spot_pct=0.0,
         xba=.254, xslg=.286, woba=.138, xwoba=.325, xwobacon=.467, hard_hit_pct=100.0, k_pct=40.0, bb_pct=20.0),
    dict(season=2017, age=24, pitches=2110, batted_balls=272, barrels=41, barrel_pct=17.2,
         barrel_per_pa=8.4, exit_velo=89.6, max_ev=116.1, launch_angle=18.6, la_sweet_spot_pct=29.8,
         xba=.221, xslg=.485, woba=.333, xwoba=.345, xwobacon=.455, hard_hit_pct=41.5, k_pct=30.9, bb_pct=12.1),
    dict(season=2018, age=25, pitches=2139, batted_balls=291, barrels=37, barrel_pct=13.9,
         barrel_per_pa=7.3, exit_velo=90.9, max_ev=117.1, launch_angle=12.3, la_sweet_spot_pct=34.0,
         xba=.242, xslg=.468, woba=.343, xwoba=.347, xwobacon=.445, hard_hit_pct=45.0, k_pct=27.5, bb_pct=15.3),
    dict(season=2019, age=26, pitches=2539, batted_balls=379, barrels=55, barrel_pct=15.9,
         barrel_per_pa=9.0, exit_velo=93.5, max_ev=117.6, launch_angle=15.5, la_sweet_spot_pct=35.6,
         xba=.261, xslg=.552, woba=.357, xwoba=.374, xwobacon=.469, hard_hit_pct=51.2, k_pct=25.6, bb_pct=11.5),
    dict(season=2020, age=27, pitches=955, batted_balls=125, barrels=14, barrel_pct=11.5,
         barrel_per_pa=6.3, exit_velo=92.8, max_ev=114.9, launch_angle=8.8, la_sweet_spot_pct=28.8,
         xba=.219, xslg=.437, woba=.307, xwoba=.336, xwobacon=.422, hard_hit_pct=47.2, k_pct=29.5, bb_pct=13.4),
    dict(season=2021, age=28, pitches=1986, batted_balls=274, barrels=48, barrel_pct=17.6,
         barrel_per_pa=10.2, exit_velo=92.3, max_ev=116.6, launch_angle=15.4, la_sweet_spot_pct=36.9,
         xba=.258, xslg=.565, woba=.392, xwoba=.397, xwobacon=.506, hard_hit_pct=52.2, k_pct=27.0, bb_pct=13.6),
    dict(season=2022, age=29, pitches=2878, batted_balls=379, barrels=76, barrel_pct=20.1,
         barrel_per_pa=11.4, exit_velo=93.3, max_ev=114.8, launch_angle=19.2, la_sweet_spot_pct=35.4,
         xba=.234, xslg=.559, woba=.355, xwoba=.379, xwobacon=.508, hard_hit_pct=54.4, k_pct=29.9, bb_pct=12.9),
    dict(season=2023, age=30, pitches=3068, batted_balls=373, barrels=61, barrel_pct=16.4,
         barrel_per_pa=8.5, exit_velo=92.4, max_ev=115.2, launch_angle=19.0, la_sweet_spot_pct=34.3,
         xba=.212, xslg=.487, woba=.350, xwoba=.362, xwobacon=.456, hard_hit_pct=48.8, k_pct=29.9, bb_pct=17.5),
    dict(season=2024, age=31, pitches=2852, batted_balls=384, barrels=60, barrel_pct=15.6,
         barrel_per_pa=8.7, exit_velo=93.6, max_ev=115.6, launch_angle=15.0, la_sweet_spot_pct=31.8,
         xba=.249, xslg=.519, woba=.366, xwoba=.380, xwobacon=.488, hard_hit_pct=55.5, k_pct=28.5, bb_pct=15.3),
    dict(season=2025, age=32, pitches=3059, batted_balls=408, barrels=85, barrel_pct=20.8,
         barrel_per_pa=11.7, exit_velo=94.3, max_ev=117.2, launch_angle=20.1, la_sweet_spot_pct=35.3,
         xba=.249, xslg=.581, woba=.391, xwoba=.401, xwobacon=.513, hard_hit_pct=59.6, k_pct=27.2, bb_pct=14.9),
    dict(season=2026, age=33, pitches=1911, batted_balls=225, barrels=41, barrel_pct=18.3,
         barrel_per_pa=9.2, exit_velo=93.3, max_ev=113.2, launch_angle=22.1, la_sweet_spot_pct=39.6,
         xba=.239, xslg=.503, woba=.389, xwoba=.367, xwobacon=.527, hard_hit_pct=52.0, k_pct=34.7, bb_pct=13.9),
]

SCHWARBER_CAREER = dict(
    pitches=24688, batted_balls=3268, barrels=537, barrel_pct=17.1, barrel_per_pa=9.2,
    exit_velo=92.7, max_ev=117.6, launch_angle=17.0, la_sweet_spot_pct=34.2,
    xba=.239, xslg=.521, woba=.361, xwoba=.372, xwobacon=.481, hard_hit_pct=51.1, k_pct=28.8, bb_pct=14.2,
)
