"""
data/real_sample/alvarez_savant_2026.py
------------------------------------------
Real Baseball Savant data for Yordan Alvarez, transcribed by hand from
screenshots the user captured directly from the Savant app.
"""

ALVAREZ_2026_SNAPSHOT = {
    "player_name": "Yordan Alvarez",
    "season": 2026,
    "batting_run_value": 43, "batting_run_value_pctl": 100,
    "xwoba": 0.473, "xwoba_pctl": 100,
    "xba": 0.336, "xba_pctl": 100,
    "xslg": 0.713, "xslg_pctl": 100,
    "avg_exit_velo": 94.6, "avg_exit_velo_pctl": 99,
    "barrel_pct": 18.9, "barrel_pct_pctl": 98,
    "hard_hit_pct": 53.3, "hard_hit_pct_pctl": 96,
    "la_sweet_spot_pct": 41.8, "la_sweet_spot_pct_pctl": 97,
    "bat_speed": 76.1, "bat_speed_pctl": 92,
    "squared_up_pct": 26.2, "squared_up_pct_pctl": 60,
    "chase_pct": 27.4, "chase_pct_pctl": 65,
    "whiff_pct": 19.6, "whiff_pct_pctl": 77,
    "k_pct": 17.1, "k_pct_pctl": 74,
    "bb_pct": 14.9, "bb_pct_pctl": 96,
    "sprint_speed": 25.0, "sprint_speed_pctl": 5,
}

ALVAREZ_SEASONS = [
    dict(season=2019, age=22, pitches=1494, batted_balls=221, barrels=37, barrel_pct=18.4,
         barrel_per_pa=10.0, exit_velo=92.2, max_ev=117.9, launch_angle=13.4, la_sweet_spot_pct=39.4,
         xba=.285, xslg=.594, woba=.432, xwoba=.408, xwobacon=.518, hard_hit_pct=48.9, k_pct=25.5, bb_pct=14.1),
    dict(season=2020, age=23, pitches=35, batted_balls=7, barrels=0, barrel_pct=0.0,
         barrel_per_pa=0.0, exit_velo=98.6, max_ev=113.1, launch_angle=6.4, la_sweet_spot_pct=0.0,
         xba=.272, xslg=.443, woba=.399, xwoba=.356, xwobacon=.353, hard_hit_pct=71.4, k_pct=11.1, bb_pct=0.0),
    dict(season=2021, age=24, pitches=2397, batted_balls=395, barrels=63, barrel_pct=15.9,
         barrel_per_pa=10.5, exit_velo=93.2, max_ev=116.4, launch_angle=14.1, la_sweet_spot_pct=37.2,
         xba=.270, xslg=.573, woba=.369, xwoba=.385, xwobacon=.484, hard_hit_pct=54.2, k_pct=24.2, bb_pct=8.4),
    dict(season=2022, age=25, pitches=2195, batted_balls=371, barrels=78, barrel_pct=21.0,
         barrel_per_pa=13.9, exit_velo=95.2, max_ev=117.4, launch_angle=12.3, la_sweet_spot_pct=40.7,
         xba=.319, xslg=.686, woba=.427, xwoba=.459, xwobacon=.544, hard_hit_pct=59.8, k_pct=18.9, bb_pct=13.9),
    dict(season=2023, age=26, pitches=1908, batted_balls=322, barrels=58, barrel_pct=18.1,
         barrel_per_pa=11.7, exit_velo=93.3, max_ev=117.7, launch_angle=17.1, la_sweet_spot_pct=35.7,
         xba=.292, xslg=.632, woba=.415, xwoba=.436, xwobacon=.498, hard_hit_pct=52.2, k_pct=18.5, bb_pct=13.9),
    dict(season=2024, age=27, pitches=2264, batted_balls=461, barrels=67, barrel_pct=14.5,
         barrel_per_pa=10.6, exit_velo=93.1, max_ev=117.0, launch_angle=18.3, la_sweet_spot_pct=35.4,
         xba=.299, xslg=.607, woba=.402, xwoba=.415, xwobacon=.462, hard_hit_pct=49.7, k_pct=15.0, bb_pct=10.9),
    dict(season=2025, age=28, pitches=803, batted_balls=138, barrels=19, barrel_pct=13.8,
         barrel_per_pa=9.5, exit_velo=94.7, max_ev=115.4, launch_angle=18.3, la_sweet_spot_pct=42.8,
         xba=.284, xslg=.549, woba=.338, xwoba=.393, xwobacon=.437, hard_hit_pct=52.9, k_pct=16.6, bb_pct=14.1),
    dict(season=2026, age=29, pitches=1766, batted_balls=304, barrels=57, barrel_pct=18.9,
         barrel_per_pa=12.5, exit_velo=94.6, max_ev=118.5, launch_angle=19.8, la_sweet_spot_pct=41.8,
         xba=.336, xslg=.713, woba=.446, xwoba=.473, xwobacon=.553, hard_hit_pct=53.3, k_pct=17.1, bb_pct=14.9),
]

ALVAREZ_CAREER = dict(
    pitches=12862, batted_balls=2219, barrels=379, barrel_pct=17.3, barrel_per_pa=11.4,
    exit_velo=93.7, max_ev=118.5, launch_angle=16.0, la_sweet_spot_pct=38.3,
    xba=.298, xslg=.626, woba=.408, xwoba=.426, xwobacon=.501, hard_hit_pct=53.2, k_pct=19.4, bb_pct=12.5,
)
