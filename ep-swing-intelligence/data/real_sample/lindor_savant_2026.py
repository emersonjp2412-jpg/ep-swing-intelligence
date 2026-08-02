"""
data/real_sample/lindor_savant_2026.py
----------------------------------------
Real Baseball Savant data for Francisco Lindor (NYM), transcribed by hand
from screenshots the user captured directly from the Savant app. Part of
the "Objetivo MLB" group -- and directly relevant since Shamir Bidor
(Performance Scout, NY Mets) is one of Emerson's professional references.
2026 sample is small enough that Batting Run Value, Baserunning Run Value,
and every Batting-section stat are flagged "NOT QUALIFIED" by Savant (no
percentile shown) -- only Fielding, Running, and the raw batting numbers
themselves are usable this season. Percentile fields are left as None
where Savant didn't display one.
"""

LINDOR_2026_SNAPSHOT = {
    "player_name": "Francisco Lindor",
    "season": 2026,
    "batting_run_value": -2, "batting_run_value_pctl": None,  # NOT QUALIFIED
    "baserunning_run_value": -1, "baserunning_run_value_pctl": None,  # NOT QUALIFIED
    "fielding_run_value": 3, "fielding_run_value_pctl": 71,
    "xwoba": 0.340, "xwoba_pctl": None,  # NOT QUALIFIED
    "xba": 0.254, "xba_pctl": None,
    "xslg": 0.438, "xslg_pctl": None,
    "avg_exit_velo": 91.9, "avg_exit_velo_pctl": None,
    "barrel_pct": 8.8, "barrel_pct_pctl": None,
    "hard_hit_pct": 49.0, "hard_hit_pct_pctl": None,
    "la_sweet_spot_pct": 31.3, "la_sweet_spot_pct_pctl": None,
    "bat_speed": 72.7, "bat_speed_pctl": None,
    "squared_up_pct": 26.1, "squared_up_pct_pctl": None,
    "chase_pct": 28.0, "chase_pct_pctl": None,
    "whiff_pct": 24.8, "whiff_pct_pctl": None,
    "k_pct": 17.5, "k_pct_pctl": None,
    "bb_pct": 10.2, "bb_pct_pctl": None,
    "range_oaa": 2, "range_oaa_pctl": 81,
    "arm_strength": 81.6, "arm_strength_pctl": 31,
    "sprint_speed": 26.6, "sprint_speed_pctl": 29,
}

LINDOR_SEASONS = [
    dict(season=2015, age=21, pitches=1578, batted_balls=341, barrels=12, barrel_pct=4.0,
         barrel_per_pa=2.7, exit_velo=89.9, max_ev=110.4, launch_angle=6.3, la_sweet_spot_pct=27.3,
         xba=.278, xslg=.405, woba=.358, xwoba=.323, xwobacon=.360, hard_hit_pct=36.7, k_pct=15.8, bb_pct=6.2),
    dict(season=2016, age=22, pitches=2552, batted_balls=534, barrels=22, barrel_pct=4.6,
         barrel_per_pa=3.2, exit_velo=88.7, max_ev=112.1, launch_angle=7.9, la_sweet_spot_pct=34.6,
         xba=.288, xslg=.424, woba=.340, xwoba=.338, xwobacon=.355, hard_hit_pct=33.5, k_pct=12.9, bb_pct=8.3),
    dict(season=2017, age=23, pitches=2727, batted_balls=566, barrels=40, barrel_pct=7.9,
         barrel_per_pa=5.5, exit_velo=89.1, max_ev=111.7, launch_angle=14.6, la_sweet_spot_pct=32.2,
         xba=.280, xslg=.500, woba=.353, xwoba=.357, xwobacon=.382, hard_hit_pct=35.9, k_pct=12.9, bb_pct=8.3),
    dict(season=2018, age=24, pitches=2920, batted_balls=560, barrels=52, barrel_pct=10.5,
         barrel_per_pa=7.0, exit_velo=90.6, max_ev=114.5, launch_angle=14.7, la_sweet_spot_pct=34.3,
         xba=.289, xslg=.512, woba=.368, xwoba=.375, xwobacon=.407, hard_hit_pct=41.0, k_pct=14.4, bb_pct=9.4),
    dict(season=2019, age=25, pitches=2426, batted_balls=507, barrels=38, barrel_pct=8.4,
         barrel_per_pa=5.8, exit_velo=91.0, max_ev=113.5, launch_angle=12.3, la_sweet_spot_pct=29.8,
         xba=.273, xslg=.464, woba=.349, xwoba=.333, xwobacon=.370, hard_hit_pct=41.0, k_pct=15.0, bb_pct=7.0),
    dict(season=2020, age=26, pitches=1118, batted_balls=197, barrels=11, barrel_pct=5.6,
         barrel_per_pa=4.1, exit_velo=89.9, max_ev=111.4, launch_angle=13.5, la_sweet_spot_pct=36.5,
         xba=.279, xslg=.441, woba=.324, xwoba=.346, xwobacon=.371, hard_hit_pct=41.1, k_pct=15.4, bb_pct=9.0),
    dict(season=2021, age=27, pitches=2096, batted_balls=365, barrels=30, barrel_pct=8.2,
         barrel_per_pa=5.7, exit_velo=90.7, max_ev=112.9, launch_angle=14.4, la_sweet_spot_pct=35.6,
         xba=.249, xslg=.456, woba=.317, xwoba=.344, xwobacon=.379, hard_hit_pct=44.1, k_pct=18.3, bb_pct=11.1),
    dict(season=2022, age=28, pitches=2829, batted_balls=504, barrels=42, barrel_pct=8.3,
         barrel_per_pa=5.9, exit_velo=89.3, max_ev=110.7, launch_angle=13.8, la_sweet_spot_pct=29.2,
         xba=.253, xslg=.439, woba=.342, xwoba=.333, xwobacon=.373, hard_hit_pct=41.3, k_pct=18.8, bb_pct=8.4),
    dict(season=2023, age=29, pitches=2741, batted_balls=472, barrels=49, barrel_pct=10.4,
         barrel_per_pa=7.1, exit_velo=91.2, max_ev=112.4, launch_angle=19.2, la_sweet_spot_pct=35.8,
         xba=.250, xslg=.462, woba=.346, xwoba=.346, xwobacon=.388, hard_hit_pct=43.9, k_pct=19.9, bb_pct=9.6),
    dict(season=2024, age=30, pitches=2713, batted_balls=494, barrels=67, barrel_pct=13.6,
         barrel_per_pa=9.7, exit_velo=90.9, max_ev=112.7, launch_angle=17.0, la_sweet_spot_pct=35.4,
         xba=.278, xslg=.539, woba=.363, xwoba=.381, xwobacon=.436, hard_hit_pct=47.4, k_pct=18.4, bb_pct=8.1),
    dict(season=2025, age=31, pitches=2940, batted_balls=520, barrels=46, barrel_pct=8.9,
         barrel_per_pa=6.3, exit_velo=90.5, max_ev=112.9, launch_angle=15.1, la_sweet_spot_pct=34.6,
         xba=.260, xslg=.454, woba=.350, xwoba=.345, xwobacon=.379, hard_hit_pct=44.4, k_pct=17.9, bb_pct=8.9),
    dict(season=2026, age=32, pitches=899, batted_balls=147, barrels=13, barrel_pct=8.8,
         barrel_per_pa=6.3, exit_velo=91.9, max_ev=111.3, launch_angle=15.6, la_sweet_spot_pct=31.3,
         xba=.254, xslg=.438, woba=.308, xwoba=.340, xwobacon=.367, hard_hit_pct=49.0, k_pct=17.5, bb_pct=10.2),
]

LINDOR_CAREER = dict(
    pitches=27539, batted_balls=5207, barrels=422, barrel_pct=8.6, barrel_per_pa=6.0,
    exit_velo=90.2, max_ev=114.5, launch_angle=13.8, la_sweet_spot_pct=33.1,
    xba=.270, xslg=.467, woba=.347, xwoba=.349, xwobacon=.383,
    hard_hit_pct=41.1, k_pct=16.4, bb_pct=8.6,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, xba=.243, xslg=.407,
    woba=.316, xwoba=.316, xwobacon=.369, hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
