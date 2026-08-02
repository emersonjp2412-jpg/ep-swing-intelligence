"""
data/real_sample/bogaerts_savant_2026.py
----------------------------------------
Real Baseball Savant data for Xander Bogaerts (SD), transcribed by hand
from screenshots the user captured directly from the Savant app. Another
contact-lean profile: LA Sweet-Spot% only 8th pctl in 2026, but Chase%
83rd and BB% 79th pctl -- a patient, ball-in-play-heavy hitter rather than
a power one, useful variance alongside Marte/Albies.
"""

BOGAERTS_2026_SNAPSHOT = {
    "player_name": "Xander Bogaerts",
    "season": 2026,
    "batting_run_value": -7, "batting_run_value_pctl": 18,
    "baserunning_run_value": 1, "baserunning_run_value_pctl": 71,
    "fielding_run_value": 6, "fielding_run_value_pctl": 91,
    "xwoba": 0.317, "xwoba_pctl": 45,
    "xba": 0.241, "xba_pctl": 35,
    "xslg": 0.371, "xslg_pctl": 28,
    "avg_exit_velo": 88.1, "avg_exit_velo_pctl": 31,
    "barrel_pct": 6.1, "barrel_pct_pctl": 28,
    "hard_hit_pct": 38.8, "hard_hit_pct_pctl": 38,
    "la_sweet_spot_pct": 28.1, "la_sweet_spot_pct_pctl": 8,
    "bat_speed": 72.5, "bat_speed_pctl": 55,
    "squared_up_pct": 27.1, "squared_up_pct_pctl": 70,
    "chase_pct": 24.3, "chase_pct_pctl": 83,
    "whiff_pct": 22.9, "whiff_pct_pctl": 57,
    "k_pct": 18.2, "k_pct_pctl": 68,
    "bb_pct": 11.7, "bb_pct_pctl": 79,
    "range_oaa": 6, "range_oaa_pctl": 94,
    "arm_strength": 82.4, "arm_strength_pctl": 35,
    "sprint_speed": 27.0, "sprint_speed_pctl": 39,
}

BOGAERTS_SEASONS = [
    dict(season=2015, age=22, pitches=2530, batted_balls=518, barrels=13, barrel_pct=2.8,
         barrel_per_pa=2.0, exit_velo=88.0, max_ev=111.8, launch_angle=6.8, la_sweet_spot_pct=28.0,
         xba=.271, xslg=.362, woba=.338, xwoba=.300, xwobacon=.333, hard_hit_pct=33.8, k_pct=15.4, bb_pct=4.9),
    dict(season=2016, age=23, pitches=2849, batted_balls=532, barrels=28, barrel_pct=6.3,
         barrel_per_pa=3.9, exit_velo=89.0, max_ev=113.2, launch_angle=11.0, la_sweet_spot_pct=28.0,
         xba=.257, xslg=.402, woba=.348, xwoba=.319, xwobacon=.349, hard_hit_pct=32.7, k_pct=17.1, bb_pct=8.1),
    dict(season=2017, age=24, pitches=2544, batted_balls=457, barrels=6, barrel_pct=1.5,
         barrel_per_pa=0.9, exit_velo=87.3, max_ev=113.9, launch_angle=8.1, la_sweet_spot_pct=26.7,
         xba=.243, xslg=.332, woba=.321, xwoba=.287, xwobacon=.309, hard_hit_pct=30.2, k_pct=18.3, bb_pct=8.8),
    dict(season=2018, age=25, pitches=2364, batted_balls=417, barrels=41, barrel_pct=10.4,
         barrel_per_pa=7.1, exit_velo=90.6, max_ev=111.9, launch_angle=12.6, la_sweet_spot_pct=32.9,
         xba=.277, xslg=.493, woba=.373, xwoba=.363, xwobacon=.406, hard_hit_pct=41.8, k_pct=17.6, bb_pct=9.5),
    dict(season=2019, age=26, pitches=2862, batted_balls=498, barrels=43, barrel_pct=9.3,
         barrel_per_pa=6.2, exit_velo=90.7, max_ev=112.4, launch_angle=13.3, la_sweet_spot_pct=35.1,
         xba=.274, xslg=.477, woba=.390, xwoba=.356, xwobacon=.393, hard_hit_pct=44.5, k_pct=17.5, bb_pct=10.9),
    dict(season=2020, age=27, pitches=967, batted_balls=163, barrels=14, barrel_pct=8.6,
         barrel_per_pa=6.2, exit_velo=89.0, max_ev=112.5, launch_angle=8.7, la_sweet_spot_pct=31.3,
         xba=.258, xslg=.471, woba=.368, xwoba=.340, xwobacon=.385, hard_hit_pct=36.8, k_pct=18.2, bb_pct=9.3),
    dict(season=2021, age=28, pitches=2505, batted_balls=423, barrels=41, barrel_pct=9.7,
         barrel_per_pa=6.8, exit_velo=89.6, max_ev=113.6, launch_angle=12.5, la_sweet_spot_pct=36.4,
         xba=.274, xslg=.470, woba=.368, xwoba=.358, xwobacon=.402, hard_hit_pct=43.0, k_pct=18.7, bb_pct=10.3),
    dict(season=2022, age=29, pitches=2500, batted_balls=446, barrels=29, barrel_pct=6.5,
         barrel_per_pa=4.6, exit_velo=88.1, max_ev=113.0, launch_angle=10.2, la_sweet_spot_pct=30.3,
         xba=.258, xslg=.393, woba=.363, xwoba=.325, xwobacon=.358, hard_hit_pct=39.5, k_pct=18.7, bb_pct=9.0),
    dict(season=2023, age=30, pitches=2644, batted_balls=492, barrels=30, barrel_pct=6.1,
         barrel_per_pa=4.5, exit_velo=87.6, max_ev=111.4, launch_angle=7.9, la_sweet_spot_pct=28.3,
         xba=.252, xslg=.400, woba=.343, xwoba=.317, xwobacon=.340, hard_hit_pct=34.6, k_pct=16.5, bb_pct=8.4),
    dict(season=2024, age=31, pitches=1791, batted_balls=355, barrels=18, barrel_pct=5.1,
         barrel_per_pa=3.9, exit_velo=88.1, max_ev=111.3, launch_angle=10.9, la_sweet_spot_pct=32.1,
         xba=.260, xslg=.386, woba=.300, xwoba=.308, xwobacon=.345, hard_hit_pct=33.2, k_pct=17.1, bb_pct=6.0),
    dict(season=2025, age=32, pitches=2100, batted_balls=406, barrels=28, barrel_pct=6.9,
         barrel_per_pa=5.1, exit_velo=89.0, max_ev=112.2, launch_angle=11.1, la_sweet_spot_pct=36.7,
         xba=.267, xslg=.413, woba=.313, xwoba=.327, xwobacon=.359, hard_hit_pct=39.2, k_pct=17.0, bb_pct=8.7),
    dict(season=2026, age=33, pitches=1583, batted_balls=278, barrels=17, barrel_pct=6.1,
         barrel_per_pa=4.2, exit_velo=88.1, max_ev=111.0, launch_angle=5.7, la_sweet_spot_pct=28.1,
         xba=.241, xslg=.371, woba=.289, xwoba=.317, xwobacon=.332, hard_hit_pct=38.8, k_pct=18.2, bb_pct=11.7),
]

BOGAERTS_CAREER = dict(
    pitches=27239, batted_balls=4985, barrels=308, barrel_pct=6.5, barrel_per_pa=4.5,
    exit_velo=88.8, max_ev=113.9, launch_angle=10.0, la_sweet_spot_pct=31.1,
    xba=.262, xslg=.412, woba=.345, xwoba=.326, xwobacon=.358,
    hard_hit_pct=37.2, k_pct=17.5, bb_pct=8.7,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, xba=.243, xslg=.407,
    woba=.316, xwoba=.316, xwobacon=.369, hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
