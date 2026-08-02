"""
data/real_sample/castellanos_savant_2026.py
----------------------------------------------
Real Baseball Savant data for Nick Castellanos (PHI), transcribed by hand
from screenshots the user captured directly from the Savant app. 2026
sample (477 pitches, 83 batted balls) is small enough that Batting Run
Value and every Batting-section stat are NOT QUALIFIED -- only Fielding
(Arm Strength) and Running are qualified. Low bat speed (69.7, well below
Marte/Robert) is exactly the low-power-mechanics data point the dataset
needed more of.
"""

CASTELLANOS_2026_SNAPSHOT = {
    "player_name": "Nick Castellanos",
    "season": 2026,
    "batting_run_value": -5, "batting_run_value_pctl": None,  # NOT QUALIFIED
    "baserunning_run_value": 0, "baserunning_run_value_pctl": None,
    "fielding_run_value": -4, "fielding_run_value_pctl": None,
    "xwoba": 0.285, "xwoba_pctl": None,
    "xba": 0.244, "xba_pctl": None,
    "xslg": 0.400, "xslg_pctl": None,
    "avg_exit_velo": 87.7, "avg_exit_velo_pctl": None,
    "barrel_pct": 8.4, "barrel_pct_pctl": None,
    "hard_hit_pct": 37.3, "hard_hit_pct_pctl": None,
    "la_sweet_spot_pct": 42.2, "la_sweet_spot_pct_pctl": None,
    "bat_speed": 69.7, "bat_speed_pctl": None,
    "squared_up_pct": 22.4, "squared_up_pct_pctl": None,
    "chase_pct": 40.2, "chase_pct_pctl": None,
    "whiff_pct": 33.5, "whiff_pct_pctl": None,
    "k_pct": 27.9, "k_pct_pctl": None,
    "bb_pct": 4.1, "bb_pct_pctl": None,
    "range_oaa": -4, "range_oaa_pctl": None,
    "arm_strength": 80.5, "arm_strength_pctl": 23,
    "sprint_speed": 27.2, "sprint_speed_pctl": 47,
}

CASTELLANOS_SEASONS = [
    dict(season=2015, age=23, pitches=2317, batted_balls=403, barrels=31, barrel_pct=8.2,
         barrel_per_pa=5.2, exit_velo=88.3, max_ev=111.6, launch_angle=16.9, la_sweet_spot_pct=37.5,
         xba=.257, xslg=.436, woba=.311, xwoba=.322, xwobacon=.410, hard_hit_pct=34.5, k_pct=25.5, bb_pct=6.6),
    dict(season=2016, age=24, pitches=1729, batted_balls=305, barrels=44, barrel_pct=15.2,
         barrel_per_pa=9.8, exit_velo=89.4, max_ev=109.2, launch_angle=16.9, la_sweet_spot_pct=48.2,
         xba=.289, xslg=.584, woba=.350, xwoba=.384, xwobacon=.493, hard_hit_pct=39.0, k_pct=24.8, bb_pct=6.3),
    dict(season=2017, age=25, pitches=2605, batted_balls=477, barrels=51, barrel_pct=11.2,
         barrel_per_pa=7.7, exit_velo=89.1, max_ev=110.5, launch_angle=14.2, la_sweet_spot_pct=42.8,
         xba=.293, xslg=.542, woba=.341, xwoba=.373, xwobacon=.454, hard_hit_pct=42.0, k_pct=21.4, bb_pct=6.2),
    dict(season=2018, age=26, pitches=2439, batted_balls=472, barrels=53, barrel_pct=11.6,
         barrel_per_pa=7.8, exit_velo=89.6, max_ev=110.3, launch_angle=15.2, la_sweet_spot_pct=45.3,
         xba=.296, xslg=.525, woba=.363, xwoba=.374, xwobacon=.460, hard_hit_pct=40.7, k_pct=22.3, bb_pct=7.2),
    dict(season=2019, age=27, pitches=2436, batted_balls=475, barrels=52, barrel_pct=11.4,
         barrel_per_pa=7.8, exit_velo=88.9, max_ev=111.2, launch_angle=13.9, la_sweet_spot_pct=39.8,
         xba=.278, xslg=.540, woba=.357, xwoba=.363, xwobacon=.441, hard_hit_pct=41.5, k_pct=21.5, bb_pct=6.2),
    dict(season=2020, age=28, pitches=966, batted_balls=150, barrels=24, barrel_pct=16.1,
         barrel_per_pa=9.9, exit_velo=91.0, max_ev=108.5, launch_angle=16.5, la_sweet_spot_pct=39.3,
         xba=.274, xslg=.545, woba=.329, xwoba=.375, xwobacon=.500, hard_hit_pct=46.7, k_pct=28.5, bb_pct=7.9),
    dict(season=2021, age=29, pitches=2143, batted_balls=416, barrels=44, barrel_pct=10.6,
         barrel_per_pa=7.5, exit_velo=89.8, max_ev=111.9, launch_angle=14.0, la_sweet_spot_pct=44.0,
         xba=.287, xslg=.545, woba=.391, xwoba=.375, xwobacon=.451, hard_hit_pct=46.9, k_pct=20.7, bb_pct=7.0),
    dict(season=2022, age=30, pitches=2066, batted_balls=396, barrels=26, barrel_pct=6.6,
         barrel_per_pa=4.7, exit_velo=87.5, max_ev=110.1, launch_angle=14.6, la_sweet_spot_pct=36.9,
         xba=.250, xslg=.408, woba=.304, xwoba=.306, xwobacon=.375, hard_hit_pct=35.1, k_pct=23.3, bb_pct=5.2),
    dict(season=2023, age=31, pitches=2427, batted_balls=447, barrels=46, barrel_pct=10.3,
         barrel_per_pa=6.9, exit_velo=88.9, max_ev=111.2, launch_angle=14.4, la_sweet_spot_pct=36.5,
         xba=.255, xslg=.449, woba=.335, xwoba=.322, xwobacon=.423, hard_hit_pct=43.2, k_pct=27.6, bb_pct=5.4),
    dict(season=2024, age=32, pitches=2344, batted_balls=469, barrels=38, barrel_pct=8.1,
         barrel_per_pa=5.8, exit_velo=88.4, max_ev=113.1, launch_angle=15.2, la_sweet_spot_pct=39.0,
         xba=.268, xslg=.454, woba=.321, xwoba=.337, xwobacon=.399, hard_hit_pct=38.2, k_pct=21.1, bb_pct=6.2),
    dict(season=2025, age=33, pitches=2166, batted_balls=420, barrels=32, barrel_pct=7.6,
         barrel_per_pa=5.4, exit_velo=87.8, max_ev=110.2, launch_angle=15.2, la_sweet_spot_pct=39.0,
         xba=.242, xslg=.408, woba=.300, xwoba=.302, xwobacon=.364, hard_hit_pct=34.5, k_pct=22.6, bb_pct=5.4),
    dict(season=2026, age=34, pitches=477, batted_balls=83, barrels=7, barrel_pct=8.4,
         barrel_per_pa=5.7, exit_velo=87.7, max_ev=108.7, launch_angle=13.0, la_sweet_spot_pct=42.2,
         xba=.244, xslg=.400, woba=.238, xwoba=.285, xwobacon=.382, hard_hit_pct=37.3, k_pct=27.9, bb_pct=4.1),
]

CASTELLANOS_CAREER = dict(
    pitches=24115, batted_balls=4513, barrels=448, barrel_pct=10.2, barrel_per_pa=6.9,
    exit_velo=88.8, max_ev=113.1, launch_angle=15.0, la_sweet_spot_pct=40.7,
    xba=.271, xslg=.488, woba=.335, xwoba=.346, xwobacon=.428,
    hard_hit_pct=39.9, k_pct=23.3, bb_pct=6.2,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, xba=.243, xslg=.407,
    woba=.316, xwoba=.316, xwobacon=.369, hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
