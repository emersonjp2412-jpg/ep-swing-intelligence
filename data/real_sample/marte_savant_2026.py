"""
data/real_sample/marte_savant_2026.py
----------------------------------------
Real Baseball Savant data for Ketel Marte (ARI), transcribed by hand from
screenshots the user captured directly from the Savant app. Contact-heavy
profile the dataset was missing: xBA 94th pctl, Chase% 34th, K% 84th pctl
(low), paired with a fully-qualified above-average Bat Speed (81st pctl).
"""

MARTE_2026_SNAPSHOT = {
    "player_name": "Ketel Marte",
    "season": 2026,
    "batting_run_value": 4, "batting_run_value_pctl": 59,
    "baserunning_run_value": 0, "baserunning_run_value_pctl": 57,
    "fielding_run_value": 4, "fielding_run_value_pctl": 77,
    "xwoba": 0.358, "xwoba_pctl": 85,
    "xba": 0.290, "xba_pctl": 94,
    "xslg": 0.486, "xslg_pctl": 85,
    "avg_exit_velo": 91.0, "avg_exit_velo_pctl": 79,
    "barrel_pct": 10.3, "barrel_pct_pctl": 64,
    "hard_hit_pct": 44.0, "hard_hit_pct_pctl": 68,
    "la_sweet_spot_pct": 33.2, "la_sweet_spot_pct_pctl": 40,
    "bat_speed": 74.8, "bat_speed_pctl": 81,
    "squared_up_pct": 26.8, "squared_up_pct_pctl": 65,
    "chase_pct": 32.3, "chase_pct_pctl": 34,
    "whiff_pct": 21.1, "whiff_pct_pctl": 68,
    "k_pct": 14.7, "k_pct_pctl": 84,
    "bb_pct": 7.0, "bb_pct_pctl": 26,
    "range_oaa": 3, "range_oaa_pctl": 86,
    "arm_strength": 80.9, "arm_strength_pctl": 25,
}

MARTE_SEASONS = [
    dict(season=2015, age=21, pitches=952, batted_balls=180, barrels=3, barrel_pct=1.9,
         barrel_per_pa=1.2, exit_velo=87.2, max_ev=109.3, launch_angle=6.8, la_sweet_spot_pct=25.0,
         xba=.242, xslg=.317, woba=.330, xwoba=.287, xwobacon=.303, hard_hit_pct=27.8, k_pct=17.4, bb_pct=9.7),
    dict(season=2016, age=22, pitches=1766, batted_balls=362, barrels=1, barrel_pct=0.3,
         barrel_per_pa=0.2, exit_velo=85.8, max_ev=113.5, launch_angle=7.0, la_sweet_spot_pct=29.0,
         xba=.244, xslg=.297, woba=.266, xwoba=.255, xwobacon=.290, hard_hit_pct=19.9, k_pct=18.0, bb_pct=3.9),
    dict(season=2017, age=23, pitches=947, batted_balls=188, barrels=5, barrel_pct=2.9,
         barrel_per_pa=2.0, exit_velo=87.5, max_ev=112.8, launch_angle=7.9, la_sweet_spot_pct=34.0,
         xba=.292, xslg=.419, woba=.319, xwoba=.346, xwobacon=.364, hard_hit_pct=34.6, k_pct=14.5, bb_pct=11.4),
    dict(season=2018, age=24, pitches=2177, batted_balls=444, barrels=22, barrel_pct=5.4,
         barrel_per_pa=3.8, exit_velo=88.8, max_ev=115.1, launch_angle=5.8, la_sweet_spot_pct=28.8,
         xba=.257, xslg=.394, woba=.330, xwoba=.320, xwobacon=.332, hard_hit_pct=36.9, k_pct=13.6, bb_pct=9.3),
    dict(season=2019, age=25, pitches=2402, batted_balls=485, barrels=45, barrel_pct=9.9,
         barrel_per_pa=7.2, exit_velo=90.0, max_ev=116.3, launch_angle=11.5, la_sweet_spot_pct=34.6,
         xba=.300, xslg=.525, woba=.405, xwoba=.375, xwobacon=.406, hard_hit_pct=40.0, k_pct=13.7, bb_pct=8.4),
    dict(season=2020, age=26, pitches=695, batted_balls=163, barrels=6, barrel_pct=3.8,
         barrel_per_pa=3.1, exit_velo=89.2, max_ev=115.9, launch_angle=10.0, la_sweet_spot_pct=28.8,
         xba=.265, xslg=.381, woba=.316, xwoba=.306, xwobacon=.319, hard_hit_pct=40.5, k_pct=10.8, bb_pct=3.6),
    dict(season=2021, age=27, pitches=1411, batted_balls=281, barrels=25, barrel_pct=8.9,
         barrel_per_pa=6.7, exit_velo=91.1, max_ev=116.0, launch_angle=10.3, la_sweet_spot_pct=33.5,
         xba=.301, xslg=.496, woba=.385, xwoba=.371, xwobacon=.416, hard_hit_pct=48.4, k_pct=16.0, bb_pct=8.3),
    dict(season=2022, age=28, pitches=2159, batted_balls=396, barrels=24, barrel_pct=6.1,
         barrel_per_pa=4.3, exit_velo=90.1, max_ev=115.0, launch_angle=13.5, la_sweet_spot_pct=31.6,
         xba=.247, xslg=.388, woba=.317, xwoba=.317, xwobacon=.343, hard_hit_pct=41.9, k_pct=18.1, bb_pct=9.9),
    dict(season=2023, age=29, pitches=2483, batted_balls=465, barrels=37, barrel_pct=8.0,
         barrel_per_pa=5.7, exit_velo=91.1, max_ev=117.1, launch_angle=10.7, la_sweet_spot_pct=30.8,
         xba=.262, xslg=.430, woba=.361, xwoba=.342, xwobacon=.365, hard_hit_pct=42.8, k_pct=16.8, bb_pct=10.9),
    dict(season=2024, age=30, pitches=2146, batted_balls=407, barrels=50, barrel_pct=12.3,
         barrel_per_pa=8.6, exit_velo=94.0, max_ev=117.0, launch_angle=9.4, la_sweet_spot_pct=33.7,
         xba=.289, xslg=.545, woba=.391, xwoba=.394, xwobacon=.450, hard_hit_pct=53.8, k_pct=18.2, bb_pct=11.1),
    dict(season=2025, age=31, pitches=2095, batted_balls=400, barrels=54, barrel_pct=13.5,
         barrel_per_pa=9.7, exit_velo=90.8, max_ev=119.6, launch_angle=14.8, la_sweet_spot_pct=33.0,
         xba=.285, xslg=.534, woba=.381, xwoba=.390, xwobacon=.420, hard_hit_pct=47.0, k_pct=14.9, bb_pct=11.5),
    dict(season=2026, age=32, pitches=1594, batted_balls=343, barrels=35, barrel_pct=10.3,
         barrel_per_pa=7.9, exit_velo=91.0, max_ev=116.9, launch_angle=12.6, la_sweet_spot_pct=33.2,
         xba=.290, xslg=.486, woba=.328, xwoba=.358, xwobacon=.394, hard_hit_pct=44.0, k_pct=14.7, bb_pct=7.0),
]

MARTE_CAREER = dict(
    pitches=20827, batted_balls=4114, barrels=307, barrel_pct=7.8, barrel_per_pa=5.5,
    exit_velo=90.0, max_ev=119.6, launch_angle=10.3, la_sweet_spot_pct=31.6,
    xba=.273, xslg=.445, woba=.349, xwoba=.344, xwobacon=.373,
    hard_hit_pct=40.6, k_pct=15.8, bb_pct=9.1,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, xba=.243, xslg=.407,
    woba=.316, xwoba=.316, xwobacon=.369, hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
