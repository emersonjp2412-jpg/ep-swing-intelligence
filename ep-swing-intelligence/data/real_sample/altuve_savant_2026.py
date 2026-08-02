"""
data/real_sample/altuve_savant_2026.py
----------------------------------------
Real Baseball Savant data for Jose Altuve, transcribed by hand from
screenshots the user captured directly from the Savant app. Contact
profile with clear age-36 decline signal: Bat Speed 12th percentile,
Avg Exit Velo 6th, but Squared-Up% still 77th -- swing quality holding
up better than raw physical output. Longest season history in the
roster so far (12 seasons, 2015-2026), useful for the model's aging-curve
signal.
"""

ALTUVE_2026_SNAPSHOT = {
    "player_name": "Jose Altuve",
    "season": 2026,
    "batting_run_value": -1, "batting_run_value_pctl": 42,
    "xwoba": 0.280, "xwoba_pctl": 9,
    "xba": 0.226, "xba_pctl": 20,
    "xslg": 0.337, "xslg_pctl": 14,
    "avg_exit_velo": 85.8, "avg_exit_velo_pctl": 6,
    "barrel_pct": 5.8, "barrel_pct_pctl": 27,
    "hard_hit_pct": 32.5, "hard_hit_pct_pctl": 16,
    "la_sweet_spot_pct": 33.7, "la_sweet_spot_pct_pctl": 44,
    "bat_speed": 68.8, "bat_speed_pctl": 12,
    "squared_up_pct": 28.2, "squared_up_pct_pctl": 77,
    "chase_pct": 36.4, "chase_pct_pctl": 17,
    "whiff_pct": 23.0, "whiff_pct_pctl": 56,
    "k_pct": 21.3, "k_pct_pctl": 52,
    "bb_pct": 8.4, "bb_pct_pctl": 43,
    "sprint_speed": 27.4, "sprint_speed_pctl": 52,
}

ALTUVE_SEASONS = [
    dict(season=2015, age=25, pitches=2227, batted_balls=580, barrels=18, barrel_pct=3.4,
         barrel_per_pa=2.6, exit_velo=86.1, max_ev=106.5, launch_angle=11.2, la_sweet_spot_pct=31.2,
         xba=.262, xslg=.382, woba=.347, xwoba=.300, xwobacon=.312, hard_hit_pct=28.6, k_pct=9.7, bb_pct=4.8),
    dict(season=2016, age=26, pitches=2474, batted_balls=580, barrels=40, barrel_pct=7.5,
         barrel_per_pa=5.6, exit_velo=88.3, max_ev=109.0, launch_angle=11.4, la_sweet_spot_pct=39.3,
         xba=.318, xslg=.526, woba=.391, xwoba=.385, xwobacon=.402, hard_hit_pct=36.4, k_pct=9.8, bb_pct=8.4),
    dict(season=2017, age=27, pitches=2308, batted_balls=511, barrels=34, barrel_pct=7.7,
         barrel_per_pa=5.1, exit_velo=86.1, max_ev=109.1, launch_angle=9.7, la_sweet_spot_pct=34.8,
         xba=.291, xslg=.477, woba=.405, xwoba=.360, xwobacon=.378, hard_hit_pct=28.1, k_pct=12.7, bb_pct=8.8),
    dict(season=2018, age=28, pitches=2123, batted_balls=459, barrels=27, barrel_pct=6.2,
         barrel_per_pa=4.5, exit_velo=87.2, max_ev=112.3, launch_angle=10.1, la_sweet_spot_pct=34.0,
         xba=.288, xslg=.449, woba=.363, xwoba=.352, xwobacon=.370, hard_hit_pct=33.8, k_pct=13.2, bb_pct=9.2),
    dict(season=2019, age=29, pitches=1994, batted_balls=422, barrels=34, barrel_pct=9.2,
         barrel_per_pa=6.2, exit_velo=87.4, max_ev=109.3, launch_angle=9.7, la_sweet_spot_pct=28.2,
         xba=.268, xslg=.484, woba=.374, xwoba=.344, xwobacon=.376, hard_hit_pct=34.5, k_pct=15.0, bb_pct=7.5),
    dict(season=2020, age=30, pitches=762, batted_balls=153, barrels=7, barrel_pct=4.6,
         barrel_per_pa=3.3, exit_velo=86.7, max_ev=106.9, launch_angle=9.3, la_sweet_spot_pct=24.8,
         xba=.230, xslg=.349, woba=.278, xwoba=.288, xwobacon=.313, hard_hit_pct=33.3, k_pct=18.6, bb_pct=8.1),
    dict(season=2021, age=31, pitches=2489, batted_balls=517, barrels=33, barrel_pct=6.4,
         barrel_per_pa=4.9, exit_velo=87.7, max_ev=109.1, launch_angle=15.6, la_sweet_spot_pct=32.1,
         xba=.258, xslg=.427, woba=.357, xwoba=.333, xwobacon=.345, hard_hit_pct=35.0, k_pct=13.4, bb_pct=9.7),
    dict(season=2022, age=32, pitches=2308, batted_balls=441, barrels=34, barrel_pct=7.8,
         barrel_per_pa=5.6, exit_velo=85.9, max_ev=109.8, launch_angle=16.1, la_sweet_spot_pct=35.4,
         xba=.268, xslg=.452, woba=.397, xwoba=.356, xwobacon=.370, hard_hit_pct=29.7, k_pct=14.4, bb_pct=10.9),
    dict(season=2023, age=33, pitches=1557, batted_balls=290, barrels=24, barrel_pct=8.3,
         barrel_per_pa=5.9, exit_velo=86.0, max_ev=109.6, launch_angle=11.4, la_sweet_spot_pct=29.7,
         xba=.241, xslg=.423, woba=.393, xwoba=.332, xwobacon=.351, hard_hit_pct=31.4, k_pct=17.3, bb_pct=10.7),
    dict(season=2024, age=34, pitches=2454, batted_balls=509, barrels=33, barrel_pct=6.5,
         barrel_per_pa=4.8, exit_velo=86.5, max_ev=108.4, launch_angle=14.1, la_sweet_spot_pct=35.4,
         xba=.261, xslg=.406, woba=.344, xwoba=.319, xwobacon=.356, hard_hit_pct=31.2, k_pct=17.4, bb_pct=6.9),
    dict(season=2025, age=35, pitches=2314, batted_balls=486, barrels=30, barrel_pct=6.2,
         barrel_per_pa=4.6, exit_velo=85.1, max_ev=110.6, launch_angle=17.7, la_sweet_spot_pct=29.8,
         xba=.237, xslg=.384, woba=.331, xwoba=.300, xwobacon=.323, hard_hit_pct=30.9, k_pct=16.7, bb_pct=8.4),
    dict(season=2026, age=36, pitches=1258, batted_balls=243, barrels=14, barrel_pct=5.8,
         barrel_per_pa=4.0, exit_velo=85.8, max_ev=107.3, launch_angle=10.3, la_sweet_spot_pct=33.7,
         xba=.226, xslg=.337, woba=.307, xwoba=.280, xwobacon=.316, hard_hit_pct=32.5, k_pct=21.3, bb_pct=8.4),
]

ALTUVE_CAREER = dict(
    pitches=24268, batted_balls=5191, barrels=328, barrel_pct=6.6, barrel_per_pa=4.8,
    exit_velo=86.6, max_ev=112.3, launch_angle=12.5, la_sweet_spot_pct=33.0,
    xba=.267, xslg=.432, woba=.363, xwoba=.334, xwobacon=.355, hard_hit_pct=32.0, k_pct=14.3, bb_pct=8.4,
)
