"""
data/real_sample/betts_savant_2026.py
----------------------------------------
Real Baseball Savant data for Mookie Betts (LAD), transcribed by hand from
screenshots the user captured directly from the Savant app. The last name
from the user's original 30-player list ("balance" group). 2026 Bat Speed
and Squared-Up% are both NOT QUALIFIED on Savant's percentile page (small
qualifying sample), but raw values are shown and used here -- percentiles
left as None rather than guessed. Elite Chase%/Whiff%/K% (98th/96th/93rd
pctl) despite unremarkable raw power is a clean "plate discipline over
power" profile to round out the set.
"""

BETTS_2026_SNAPSHOT = {
    "player_name": "Mookie Betts",
    "season": 2026,
    "batting_run_value": -1, "batting_run_value_pctl": 41,
    "baserunning_run_value": 0, "baserunning_run_value_pctl": 40,
    "fielding_run_value": 6, "fielding_run_value_pctl": 90,
    "xwoba": 0.329, "xwoba_pctl": 59,
    "xba": 0.270, "xba_pctl": 79,
    "xslg": 0.430, "xslg_pctl": 63,
    "avg_exit_velo": 90.4, "avg_exit_velo_pctl": 72,
    "barrel_pct": 8.2, "barrel_pct_pctl": 52,
    "hard_hit_pct": 38.4, "hard_hit_pct_pctl": 37,
    "la_sweet_spot_pct": 40.1, "la_sweet_spot_pct_pctl": 93,
    "bat_speed": 69.5, "bat_speed_pctl": None,  # NOT QUALIFIED
    "squared_up_pct": 42.8, "squared_up_pct_pctl": None,  # NOT QUALIFIED
    "chase_pct": 18.9, "chase_pct_pctl": 98,
    "whiff_pct": 12.7, "whiff_pct_pctl": 96,
    "k_pct": 12.3, "k_pct_pctl": 93,
    "bb_pct": 7.9, "bb_pct_pctl": 37,
    "range_oaa": 6, "range_oaa_pctl": 94,
    "arm_strength": 81.2, "arm_strength_pctl": 28,
    "sprint_speed": 26.5, "sprint_speed_pctl": 29,
}

BETTS_SEASONS = [
    dict(season=2015, age=22, pitches=2634, batted_balls=524, barrels=29, barrel_pct=6.4,
         barrel_per_pa=4.4, exit_velo=90.4, max_ev=110.3, launch_angle=15.4, la_sweet_spot_pct=33.4,
         xba=.283, xslg=.445, woba=.351, xwoba=.341, xwobacon=.364, hard_hit_pct=37.5, k_pct=12.5, bb_pct=7.0),
    dict(season=2016, age=23, pitches=2709, batted_balls=599, barrels=31, barrel_pct=5.9,
         barrel_per_pa=4.2, exit_velo=89.7, max_ev=114.7, launch_angle=12.5, la_sweet_spot_pct=31.7,
         xba=.278, xslg=.446, woba=.379, xwoba=.336, xwobacon=.352, hard_hit_pct=39.9, k_pct=11.0, bb_pct=6.7),
    dict(season=2017, age=24, pitches=2804, batted_balls=554, barrels=25, barrel_pct=5.1,
         barrel_per_pa=3.5, exit_velo=88.4, max_ev=111.7, launch_angle=14.3, la_sweet_spot_pct=31.9,
         xba=.273, xslg=.436, woba=.339, xwoba=.340, xwobacon=.344, hard_hit_pct=37.9, k_pct=11.1, bb_pct=10.8),
    dict(season=2018, age=25, pitches=2582, batted_balls=434, barrels=61, barrel_pct=14.9,
         barrel_per_pa=9.9, exit_velo=92.2, max_ev=110.6, launch_angle=18.5, la_sweet_spot_pct=39.4,
         xba=.309, xslg=.606, woba=.449, xwoba=.431, xwobacon=.472, hard_hit_pct=50.6, k_pct=14.8, bb_pct=13.2),
    dict(season=2019, age=26, pitches=2909, batted_balls=505, barrels=52, barrel_pct=10.9,
         barrel_per_pa=7.4, exit_velo=91.0, max_ev=109.3, launch_angle=19.0, la_sweet_spot_pct=39.4,
         xba=.311, xslg=.577, woba=.380, xwoba=.411, xwobacon=.441, hard_hit_pct=47.4, k_pct=14.3, bb_pct=13.7),
    dict(season=2020, age=27, pitches=930, batted_balls=182, barrels=14, barrel_pct=7.8,
         barrel_per_pa=5.7, exit_velo=90.7, max_ev=108.5, launch_angle=18.5, la_sweet_spot_pct=40.1,
         xba=.283, xslg=.485, woba=.390, xwoba=.362, xwobacon=.392, hard_hit_pct=43.4, k_pct=15.4, bb_pct=9.8),
    dict(season=2021, age=28, pitches=2232, batted_balls=385, barrels=30, barrel_pct=7.8,
         barrel_per_pa=5.5, exit_velo=90.3, max_ev=107.9, launch_angle=18.9, la_sweet_spot_pct=34.0,
         xba=.258, xslg=.449, woba=.365, xwoba=.357, xwobacon=.369, hard_hit_pct=41.0, k_pct=15.6, bb_pct=12.4),
    dict(season=2022, age=29, pitches=2428, batted_balls=472, barrels=46, barrel_pct=9.8,
         barrel_per_pa=7.2, exit_velo=90.5, max_ev=109.0, launch_angle=18.6, la_sweet_spot_pct=36.2,
         xba=.252, xslg=.484, woba=.373, xwoba=.348, xwobacon=.379, hard_hit_pct=44.9, k_pct=16.3, bb_pct=8.6),
    dict(season=2023, age=30, pitches=2712, batted_balls=482, barrels=60, barrel_pct=12.4,
         barrel_per_pa=8.7, exit_velo=92.4, max_ev=110.1, launch_angle=20.6, la_sweet_spot_pct=42.5,
         xba=.288, xslg=.572, woba=.416, xwoba=.408, xwobacon=.438, hard_hit_pct=48.5, k_pct=15.4, bb_pct=13.9),
    dict(season=2024, age=31, pitches=2047, batted_balls=397, barrels=24, barrel_pct=6.0,
         barrel_per_pa=4.7, exit_velo=89.9, max_ev=109.4, launch_angle=21.4, la_sweet_spot_pct=39.3,
         xba=.282, xslg=.468, woba=.371, xwoba=.364, xwobacon=.367, hard_hit_pct=39.5, k_pct=11.0, bb_pct=11.8),
    dict(season=2025, age=32, pitches=2460, batted_balls=531, barrels=29, barrel_pct=5.5,
         barrel_per_pa=4.4, exit_velo=89.1, max_ev=108.4, launch_angle=18.0, la_sweet_spot_pct=37.7,
         xba=.267, xslg=.422, woba=.318, xwoba=.330, xwobacon=.330, hard_hit_pct=35.8, k_pct=10.3, bb_pct=9.2),
    dict(season=2026, age=33, pitches=1070, batted_balls=232, barrels=19, barrel_pct=8.2,
         barrel_per_pa=6.5, exit_velo=90.4, max_ev=108.1, launch_angle=19.0, la_sweet_spot_pct=40.1,
         xba=.270, xslg=.430, woba=.308, xwoba=.329, xwobacon=.345, hard_hit_pct=38.4, k_pct=12.3, bb_pct=7.9),
]

BETTS_CAREER = dict(
    pitches=27517, batted_balls=5297, barrels=420, barrel_pct=8.4, barrel_per_pa=6.0,
    exit_velo=90.4, max_ev=114.7, launch_angle=17.6, la_sweet_spot_pct=36.6,
    xba=.280, xslg=.487, woba=.372, xwoba=.365, xwobacon=.382,
    hard_hit_pct=42.0, k_pct=13.2, bb_pct=10.5,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, xba=.243, xslg=.407,
    woba=.316, xwoba=.316, xwobacon=.369, hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
