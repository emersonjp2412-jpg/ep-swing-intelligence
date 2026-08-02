"""
data/real_sample/devers_savant_2026.py
----------------------------------------
Real Baseball Savant data for Rafael Devers (SF), transcribed by hand from
screenshots the user captured directly from the Savant app. Balanced
power/contact profile in the middle of the distribution: Bat Speed 46th
pctl (close to league average), Barrel% 77th, Hard-Hit% 91st -- useful as
a mid-range anchor alongside the more extreme profiles already collected.
"""

DEVERS_2026_SNAPSHOT = {
    "player_name": "Rafael Devers",
    "season": 2026,
    "batting_run_value": 5, "batting_run_value_pctl": 64,
    "baserunning_run_value": -1, "baserunning_run_value_pctl": 32,
    "fielding_run_value": 1, "fielding_run_value_pctl": 54,
    "xwoba": 0.324, "xwoba_pctl": 55,
    "xba": 0.233, "xba_pctl": 25,
    "xslg": 0.455, "xslg_pctl": 76,
    "avg_exit_velo": 92.3, "avg_exit_velo_pctl": 89,
    "barrel_pct": 11.6, "barrel_pct_pctl": 77,
    "hard_hit_pct": 50.7, "hard_hit_pct_pctl": 91,
    "la_sweet_spot_pct": 32.7, "la_sweet_spot_pct_pctl": 34,
    "bat_speed": 71.9, "bat_speed_pctl": 46,
    "squared_up_pct": 24.0, "squared_up_pct_pctl": 41,
    "chase_pct": 29.5, "chase_pct_pctl": 53,
    "whiff_pct": 29.9, "whiff_pct_pctl": 22,
    "k_pct": 27.6, "k_pct_pctl": 16,
    "bb_pct": 9.3, "bb_pct_pctl": 55,
    "range_oaa": 0, "range_oaa_pctl": 62,
    "arm_strength": 80.2, "arm_strength_pctl": 21,
    "sprint_speed": 26.0, "sprint_speed_pctl": 20,
}

DEVERS_SEASONS = [
    dict(season=2017, age=20, pitches=892, batted_balls=165, barrels=14, barrel_pct=9.3,
         barrel_per_pa=5.8, exit_velo=89.7, max_ev=112.3, launch_angle=8.6, la_sweet_spot_pct=26.1,
         xba=.231, xslg=.417, woba=.344, xwoba=.299, xwobacon=.367, hard_hit_pct=44.2, k_pct=23.8, bb_pct=7.5),
    dict(season=2018, age=21, pitches=1828, batted_balls=331, barrels=30, barrel_pct=10.1,
         barrel_per_pa=6.1, exit_velo=90.9, max_ev=116.3, launch_angle=11.2, la_sweet_spot_pct=30.2,
         xba=.233, xslg=.407, woba=.310, xwoba=.303, xwobacon=.377, hard_hit_pct=42.0, k_pct=24.7, bb_pct=7.8),
    dict(season=2019, age=22, pitches=2636, batted_balls=531, barrels=48, barrel_pct=10.0,
         barrel_per_pa=6.8, exit_velo=92.5, max_ev=115.0, launch_angle=10.5, la_sweet_spot_pct=33.1,
         xba=.298, xslg=.526, woba=.377, xwoba=.367, xwobacon=.422, hard_hit_pct=48.5, k_pct=17.0, bb_pct=6.8),
    dict(season=2020, age=23, pitches=980, batted_balls=165, barrels=20, barrel_pct=12.2,
         barrel_per_pa=8.1, exit_velo=93.0, max_ev=116.7, launch_angle=10.6, la_sweet_spot_pct=33.3,
         xba=.256, xslg=.460, woba=.337, xwoba=.328, xwobacon=.425, hard_hit_pct=43.6, k_pct=27.0, bb_pct=5.2),
    dict(season=2021, age=24, pitches=2502, batted_balls=452, barrels=68, barrel_pct=15.1,
         barrel_per_pa=10.2, exit_velo=92.9, max_ev=114.4, launch_angle=13.1, la_sweet_spot_pct=35.2,
         xba=.285, xslg=.565, woba=.373, xwoba=.391, xwobacon=.473, hard_hit_pct=51.8, k_pct=21.5, bb_pct=9.3),
    dict(season=2022, age=25, pitches=2232, batted_balls=444, barrels=51, barrel_pct=11.5,
         barrel_per_pa=8.3, exit_velo=93.1, max_ev=113.7, launch_angle=11.3, la_sweet_spot_pct=33.1,
         xba=.280, xslg=.514, woba=.373, xwoba=.365, xwobacon=.426, hard_hit_pct=50.9, k_pct=18.6, bb_pct=8.1),
    dict(season=2023, age=26, pitches=2579, batted_balls=457, barrels=58, barrel_pct=12.7,
         barrel_per_pa=8.8, exit_velo=93.1, max_ev=115.0, launch_angle=12.4, la_sweet_spot_pct=30.0,
         xba=.276, xslg=.543, woba=.359, xwoba=.379, xwobacon=.440, hard_hit_pct=55.1, k_pct=19.2, bb_pct=9.5),
    dict(season=2024, age=27, pitches=2375, batted_balls=384, barrels=50, barrel_pct=13.1,
         barrel_per_pa=8.3, exit_velo=93.2, max_ev=114.7, launch_angle=11.6, la_sweet_spot_pct=35.2,
         xba=.267, xslg=.514, woba=.364, xwoba=.366, xwobacon=.459, hard_hit_pct=52.6, k_pct=24.5, bb_pct=11.1),
    dict(season=2025, age=28, pitches=3060, batted_balls=419, barrels=67, barrel_pct=16.0,
         barrel_per_pa=9.2, exit_velo=93.5, max_ev=114.5, launch_angle=12.6, la_sweet_spot_pct=34.6,
         xba=.244, xslg=.487, woba=.365, xwoba=.367, xwobacon=.452, hard_hit_pct=56.1, k_pct=26.3, bb_pct=15.4),
    dict(season=2026, age=29, pitches=1793, batted_balls=278, barrels=32, barrel_pct=11.6,
         barrel_per_pa=7.2, exit_velo=92.3, max_ev=112.5, launch_angle=14.6, la_sweet_spot_pct=32.7,
         xba=.233, xslg=.455, woba=.344, xwoba=.324, xwobacon=.416, hard_hit_pct=50.7, k_pct=27.6, bb_pct=9.3),
]

DEVERS_CAREER = dict(
    pitches=20877, batted_balls=3626, barrels=438, barrel_pct=12.4, barrel_per_pa=8.1,
    exit_velo=92.6, max_ev=116.7, launch_angle=11.8, la_sweet_spot_pct=32.8,
    xba=.265, xslg=.500, woba=.359, xwoba=.357, xwobacon=.431,
    hard_hit_pct=50.5, k_pct=22.4, bb_pct=9.5,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, xba=.243, xslg=.407,
    woba=.316, xwoba=.316, xwobacon=.369, hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
