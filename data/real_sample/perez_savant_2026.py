"""
data/real_sample/perez_savant_2026.py
----------------------------------------
Real Baseball Savant data for Salvador Perez (KC), transcribed by hand from
screenshots the user captured directly from the Savant app. Second catcher
in the dataset. 2026 shows real age-decline signal across the board
(Batting Run Value 3rd pctl, Chase% 1st pctl, BB% 4th pctl) -- a genuinely
weak season, kept in rather than cherry-picked out, which matters for
model honesty. 2019 season missing from Savant (Tommy John surgery,
missed the season).
"""

PEREZ_2026_SNAPSHOT = {
    "player_name": "Salvador Perez",
    "season": 2026,
    "batting_run_value": -13, "batting_run_value_pctl": 3,
    "baserunning_run_value": -2, "baserunning_run_value_pctl": 11,
    "fielding_run_value": -10, "fielding_run_value_pctl": 1,
    "xwoba": 0.297, "xwoba_pctl": 23,
    "xba": 0.228, "xba_pctl": 22,
    "xslg": 0.410, "xslg_pctl": 54,
    "avg_exit_velo": 89.0, "avg_exit_velo_pctl": 42,
    "barrel_pct": 10.3, "barrel_pct_pctl": 64,
    "hard_hit_pct": 42.5, "hard_hit_pct_pctl": 59,
    "la_sweet_spot_pct": 34.2, "la_sweet_spot_pct_pctl": 52,
    "bat_speed": 71.6, "bat_speed_pctl": 41,
    "squared_up_pct": 23.7, "squared_up_pct_pctl": 38,
    "chase_pct": 45.6, "chase_pct_pctl": 1,
    "whiff_pct": 25.6, "whiff_pct_pctl": 43,
    "k_pct": 20.6, "k_pct_pctl": 57,
    "bb_pct": 3.9, "bb_pct_pctl": 4,
    "range_oaa": -5, "range_oaa_pctl": None,  # NOT QUALIFIED
    "arm_strength": None, "arm_strength_pctl": None,
    "sprint_speed": None, "sprint_speed_pctl": None,
    "blocks_above_avg": -3, "blocks_above_avg_pctl": 19,
    "cs_above_avg": 0, "cs_above_avg_pctl": 60,
    "framing": -6, "framing_pctl": 3,
    "pop_time": 1.98, "pop_time_pctl": 24,
}

PEREZ_SEASONS = [
    dict(season=2015, age=25, pitches=1840, batted_balls=454, barrels=24, barrel_pct=6.3,
         barrel_per_pa=4.3, exit_velo=87.3, max_ev=110.9, launch_angle=13.0, la_sweet_spot_pct=32.8,
         xba=.260, xslg=.408, woba=.300, xwoba=.298, xwobacon=.342, hard_hit_pct=32.6, k_pct=14.8, bb_pct=2.4),
    dict(season=2016, age=26, pitches=1875, batted_balls=397, barrels=25, barrel_pct=7.0,
         barrel_per_pa=4.6, exit_velo=88.8, max_ev=112.7, launch_angle=18.9, la_sweet_spot_pct=29.5,
         xba=.234, xslg=.394, woba=.308, xwoba=.288, xwobacon=.346, hard_hit_pct=37.8, k_pct=21.8, bb_pct=4.0),
    dict(season=2017, age=27, pitches=1737, batted_balls=381, barrels=36, barrel_pct=10.8,
         barrel_per_pa=7.2, exit_velo=88.7, max_ev=111.3, launch_angle=18.7, la_sweet_spot_pct=34.4,
         xba=.275, xslg=.532, woba=.329, xwoba=.349, xwobacon=.419, hard_hit_pct=38.9, k_pct=19.1, bb_pct=3.4),
    dict(season=2018, age=28, pitches=1926, batted_balls=407, barrels=44, barrel_pct=11.6,
         barrel_per_pa=8.1, exit_velo=91.3, max_ev=112.1, launch_angle=18.0, la_sweet_spot_pct=35.4,
         xba=.256, xslg=.477, woba=.304, xwoba=.334, xwobacon=.396, hard_hit_pct=47.5, k_pct=19.9, bb_pct=3.1),
    dict(season=2020, age=30, pitches=563, batted_balls=115, barrels=16, barrel_pct=14.2,
         barrel_per_pa=10.3, exit_velo=91.0, max_ev=110.4, launch_angle=14.2, la_sweet_spot_pct=41.7,
         xba=.319, xslg=.622, woba=.410, xwoba=.406, xwobacon=.522, hard_hit_pct=47.0, k_pct=23.1, bb_pct=1.9),
    dict(season=2021, age=31, pitches=2392, batted_balls=454, barrels=74, barrel_pct=16.3,
         barrel_per_pa=11.1, exit_velo=93.0, max_ev=114.4, launch_angle=15.9, la_sweet_spot_pct=34.1,
         xba=.269, xslg=.562, woba=.359, xwoba=.369, xwobacon=.480, hard_hit_pct=56.2, k_pct=25.6, bb_pct=4.2),
    dict(season=2022, age=32, pitches=1700, batted_balls=339, barrels=38, barrel_pct=11.2,
         barrel_per_pa=8.0, exit_velo=91.4, max_ev=112.5, launch_angle=17.8, la_sweet_spot_pct=34.8,
         xba=.239, xslg=.481, woba=.324, xwoba=.324, xwobacon=.403, hard_hit_pct=49.0, k_pct=23.0, bb_pct=3.8),
    dict(season=2023, age=33, pitches=2061, batted_balls=411, barrels=36, barrel_pct=8.8,
         barrel_per_pa=6.2, exit_velo=90.1, max_ev=113.1, launch_angle=15.6, la_sweet_spot_pct=38.0,
         xba=.262, xslg=.465, woba=.302, xwoba=.326, xwobacon=.409, hard_hit_pct=44.0, k_pct=23.3, bb_pct=3.3),
    dict(season=2024, age=34, pitches=2301, batted_balls=467, barrels=57, barrel_pct=12.3,
         barrel_per_pa=8.7, exit_velo=91.1, max_ev=113.3, launch_angle=19.0, la_sweet_spot_pct=39.4,
         xba=.271, xslg=.530, woba=.335, xwoba=.361, xwobacon=.429, hard_hit_pct=44.8, k_pct=19.8, bb_pct=6.7),
    dict(season=2025, age=35, pitches=2267, batted_balls=473, barrels=70, barrel_pct=14.8,
         barrel_per_pa=10.9, exit_velo=90.0, max_ev=114.8, launch_angle=18.1, la_sweet_spot_pct=35.7,
         xba=.269, xslg=.534, woba=.311, xwoba=.357, xwobacon=.426, hard_hit_pct=46.7, k_pct=19.5, bb_pct=4.4),
    dict(season=2026, age=36, pitches=1512, batted_balls=301, barrels=31, barrel_pct=10.3,
         barrel_per_pa=7.5, exit_velo=89.0, max_ev=111.2, launch_angle=16.1, la_sweet_spot_pct=34.2,
         xba=.228, xslg=.410, woba=.271, xwoba=.297, xwobacon=.348, hard_hit_pct=42.5, k_pct=20.6, bb_pct=3.9),
]

PEREZ_CAREER = dict(
    pitches=20174, batted_balls=4199, barrels=451, barrel_pct=11.2, barrel_per_pa=7.9,
    exit_velo=90.1, max_ev=114.8, launch_angle=17.0, la_sweet_spot_pct=35.1,
    xba=.259, xslg=.488, woba=.319, xwoba=.335, xwobacon=.406,
    hard_hit_pct=44.1, k_pct=20.9, bb_pct=3.9,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, xba=.243, xslg=.407,
    woba=.316, xwoba=.316, xwobacon=.369, hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
