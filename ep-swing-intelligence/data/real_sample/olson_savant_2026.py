"""
data/real_sample/olson_savant_2026.py
----------------------------------------
Real Baseball Savant data for Matt Olson (ATL), transcribed by hand from
screenshots the user captured directly from the Savant app. Power-extreme
profile: Batting Run Value 96th pctl, xSLG 92nd, Bat Speed 82nd -- paired
with a notably low Sprint Speed (10th pctl), a swing-mechanics/power
combination the dataset needed more of at the high end.
"""

OLSON_2026_SNAPSHOT = {
    "player_name": "Matt Olson",
    "season": 2026,
    "batting_run_value": 23, "batting_run_value_pctl": 96,
    "baserunning_run_value": 0, "baserunning_run_value_pctl": 39,
    "fielding_run_value": 4, "fielding_run_value_pctl": 79,
    "xwoba": 0.358, "xwoba_pctl": 85,
    "xba": 0.249, "xba_pctl": 47,
    "xslg": 0.506, "xslg_pctl": 92,
    "avg_exit_velo": 92.6, "avg_exit_velo_pctl": 92,
    "barrel_pct": 13.8, "barrel_pct_pctl": 87,
    "hard_hit_pct": 50.3, "hard_hit_pct_pctl": 90,
    "la_sweet_spot_pct": 30.9, "la_sweet_spot_pct_pctl": 20,
    "bat_speed": 74.9, "bat_speed_pctl": 82,
    "squared_up_pct": 23.2, "squared_up_pct_pctl": 34,
    "chase_pct": 27.1, "chase_pct_pctl": 67,
    "whiff_pct": 24.3, "whiff_pct_pctl": 49,
    "k_pct": 24.1, "k_pct_pctl": 34,
    "bb_pct": 10.3, "bb_pct_pctl": 66,
    "range_oaa": 3, "range_oaa_pctl": 87,
    "arm_strength": 82.6, "arm_strength_pctl": 37,
    "sprint_speed": 25.4, "sprint_speed_pctl": 10,
}

OLSON_SEASONS = [
    dict(season=2016, age=22, pitches=106, batted_balls=17, barrels=0, barrel_pct=0.0,
         barrel_per_pa=0.0, exit_velo=91.2, max_ev=107.8, launch_angle=25.5, la_sweet_spot_pct=17.6,
         xba=.181, xslg=.241, woba=.248, xwoba=.309, xwobacon=.224, hard_hit_pct=23.5, k_pct=14.3, bb_pct=25.0),
    dict(season=2017, age=23, pitches=914, batted_balls=129, barrels=21, barrel_pct=18.3,
         barrel_per_pa=9.7, exit_velo=92.6, max_ev=111.0, launch_angle=17.8, la_sweet_spot_pct=28.7,
         xba=.259, xslg=.588, woba=.411, xwoba=.392, xwobacon=.515, hard_hit_pct=48.8, k_pct=27.8, bb_pct=10.2),
    dict(season=2018, age=24, pitches=2844, batted_balls=419, barrels=51, barrel_pct=13.4,
         barrel_per_pa=7.7, exit_velo=93.3, max_ev=113.3, launch_angle=18.1, la_sweet_spot_pct=35.1,
         xba=.250, xslg=.494, woba=.340, xwoba=.357, xwobacon=.436, hard_hit_pct=52.2, k_pct=24.7, bb_pct=10.6),
    dict(season=2019, age=25, pitches=2288, batted_balls=346, barrels=50, barrel_pct=15.7,
         barrel_per_pa=9.1, exit_velo=92.7, max_ev=111.9, launch_angle=19.4, la_sweet_spot_pct=36.1,
         xba=.278, xslg=.578, woba=.368, xwoba=.388, xwobacon=.495, hard_hit_pct=50.4, k_pct=25.2, bb_pct=9.3),
    dict(season=2020, age=26, pitches=1002, batted_balls=133, barrels=17, barrel_pct=13.1,
         barrel_per_pa=6.9, exit_velo=92.3, max_ev=112.5, launch_angle=19.6, la_sweet_spot_pct=30.1,
         xba=.224, xslg=.453, woba=.316, xwoba=.340, xwobacon=.450, hard_hit_pct=45.9, k_pct=31.4, bb_pct=13.9),
    dict(season=2021, age=27, pitches=2774, batted_balls=463, barrels=59, barrel_pct=12.7,
         barrel_per_pa=8.8, exit_velo=91.6, max_ev=115.3, launch_angle=16.2, la_sweet_spot_pct=32.4,
         xba=.258, xslg=.513, woba=.379, xwoba=.378, xwobacon=.412, hard_hit_pct=48.8, k_pct=16.8, bb_pct=13.1),
    dict(season=2022, age=28, pitches=2893, batted_balls=450, barrels=61, barrel_pct=13.6,
         barrel_per_pa=8.7, exit_velo=92.9, max_ev=116.8, launch_angle=16.1, la_sweet_spot_pct=33.8,
         xba=.243, xslg=.481, woba=.344, xwoba=.347, xwobacon=.423, hard_hit_pct=50.9, k_pct=24.3, bb_pct=10.7),
    dict(season=2023, age=29, pitches=3092, batted_balls=445, barrels=73, barrel_pct=16.4,
         barrel_per_pa=10.1, exit_velo=93.7, max_ev=118.6, launch_angle=16.1, la_sweet_spot_pct=31.0,
         xba=.262, xslg=.571, woba=.413, xwoba=.395, xwobacon=.476, hard_hit_pct=55.5, k_pct=23.2, bb_pct=14.4),
    dict(season=2024, age=30, pitches=2947, batted_balls=435, barrels=54, barrel_pct=12.5,
         barrel_per_pa=7.9, exit_velo=91.5, max_ev=113.9, launch_angle=16.1, la_sweet_spot_pct=35.4,
         xba=.242, xslg=.454, woba=.339, xwoba=.342, xwobacon=.415, hard_hit_pct=47.4, k_pct=24.8, bb_pct=10.4),
    dict(season=2025, age=31, pitches=3166, batted_balls=453, barrels=65, barrel_pct=14.4,
         barrel_per_pa=9.0, exit_velo=93.3, max_ev=114.0, launch_angle=14.8, la_sweet_spot_pct=37.1,
         xba=.249, xslg=.492, woba=.366, xwoba=.360, xwobacon=.432, hard_hit_pct=53.3, k_pct=24.3, bb_pct=12.6),
    dict(season=2026, age=32, pitches=1964, batted_balls=298, barrels=41, barrel_pct=13.8,
         barrel_per_pa=9.0, exit_velo=92.6, max_ev=111.6, launch_angle=17.9, la_sweet_spot_pct=30.9,
         xba=.249, xslg=.506, woba=.371, xwoba=.358, xwobacon=.438, hard_hit_pct=50.3, k_pct=24.1, bb_pct=10.3),
]

OLSON_CAREER = dict(
    pitches=23990, batted_balls=3588, barrels=492, barrel_pct=14.1, barrel_per_pa=8.7,
    exit_velo=92.7, max_ev=118.6, launch_angle=16.9, la_sweet_spot_pct=33.6,
    xba=.252, xslg=.509, woba=.364, xwoba=.365, xwobacon=.441,
    hard_hit_pct=50.7, k_pct=23.8, bb_pct=11.7,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, xba=.243, xslg=.407,
    woba=.316, xwoba=.316, xwobacon=.369, hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
