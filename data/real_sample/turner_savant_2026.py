"""
data/real_sample/turner_savant_2026.py
----------------------------------------
Real Baseball Savant data for Trea Turner (PHI), transcribed by hand from
screenshots the user captured directly from the Savant app. Part of the
"Objetivo MLB" group (Phillies/Mets/Nationals targets relevant to EP's
outreach pipeline). Bat Speed 43rd pctl / Squared-Up% 49th pctl in 2026 --
solidly average bat-tracking profile, consistent with a contact-over-power
skillset (Chase% 20th pctl is the standout number).
"""

TURNER_2026_SNAPSHOT = {
    "player_name": "Trea Turner",
    "season": 2026,
    "batting_run_value": -6, "batting_run_value_pctl": 21,
    "baserunning_run_value": 3, "baserunning_run_value_pctl": 93,
    "fielding_run_value": -9, "fielding_run_value_pctl": 2,
    "xwoba": 0.295, "xwoba_pctl": 20,
    "xba": 0.244, "xba_pctl": 39,
    "xslg": 0.372, "xslg_pctl": 30,
    "avg_exit_velo": 88.9, "avg_exit_velo_pctl": 41,
    "barrel_pct": 6.6, "barrel_pct_pctl": 33,
    "hard_hit_pct": 41.6, "hard_hit_pct_pctl": 51,
    "la_sweet_spot_pct": 33.1, "la_sweet_spot_pct_pctl": 39,
    "bat_speed": 71.7, "bat_speed_pctl": 43,
    "squared_up_pct": 24.8, "squared_up_pct_pctl": 49,
    "chase_pct": 35.0, "chase_pct_pctl": 20,
    "whiff_pct": 27.5, "whiff_pct_pctl": 34,
    "k_pct": 22.7, "k_pct_pctl": 44,
    "bb_pct": 6.2, "bb_pct_pctl": 16,
    "range_oaa": -8, "range_oaa_pctl": 1,
    "arm_strength": 82.4, "arm_strength_pctl": 35,
}

TURNER_SEASONS = [
    dict(season=2015, age=22, pitches=171, batted_balls=28, barrels=1, barrel_pct=4.2,
         barrel_per_pa=2.3, exit_velo=86.2, max_ev=103.0, launch_angle=5.1, la_sweet_spot_pct=32.1,
         xba=.251, xslg=.326, woba=.278, xwoba=.295, xwobacon=.365, hard_hit_pct=25.0, k_pct=27.3, bb_pct=9.1),
    dict(season=2016, age=23, pitches=1232, batted_balls=250, barrels=17, barrel_pct=8.1,
         barrel_per_pa=5.2, exit_velo=89.9, max_ev=113.5, launch_angle=11.5, la_sweet_spot_pct=34.4,
         xba=.298, xslg=.496, woba=.395, xwoba=.356, xwobacon=.426, hard_hit_pct=36.4, k_pct=18.2, bb_pct=4.3),
    dict(season=2017, age=24, pitches=1694, batted_balls=333, barrels=18, barrel_pct=6.0,
         barrel_per_pa=4.0, exit_velo=89.1, max_ev=111.9, launch_angle=7.1, la_sweet_spot_pct=29.1,
         xba=.273, xslg=.428, woba=.338, xwoba=.329, xwobacon=.370, hard_hit_pct=39.2, k_pct=17.9, bb_pct=6.7),
    dict(season=2018, age=25, pitches=2927, batted_balls=534, barrels=31, barrel_pct=6.4,
         barrel_per_pa=4.2, exit_velo=89.1, max_ev=112.3, launch_angle=9.3, la_sweet_spot_pct=29.0,
         xba=.273, xslg=.415, woba=.331, xwoba=.335, xwobacon=.371, hard_hit_pct=38.6, k_pct=17.8, bb_pct=9.3),
    dict(season=2019, age=26, pitches=2234, batted_balls=410, barrels=28, barrel_pct=7.3,
         barrel_per_pa=4.9, exit_velo=90.4, max_ev=113.5, launch_angle=9.9, la_sweet_spot_pct=29.8,
         xba=.279, xslg=.455, woba=.356, xwoba=.339, xwobacon=.394, hard_hit_pct=42.0, k_pct=19.9, bb_pct=7.6),
    dict(season=2020, age=27, pitches=1033, batted_balls=199, barrels=19, barrel_pct=9.7,
         barrel_per_pa=7.3, exit_velo=90.5, max_ev=111.2, launch_angle=9.5, la_sweet_spot_pct=34.2,
         xba=.303, xslg=.515, woba=.413, xwoba=.383, xwobacon=.415, hard_hit_pct=40.7, k_pct=13.9, bb_pct=8.5),
    dict(season=2021, age=28, pitches=2487, batted_balls=489, barrels=36, barrel_pct=7.4,
         barrel_per_pa=5.6, exit_velo=89.6, max_ev=112.2, launch_angle=11.4, la_sweet_spot_pct=34.6,
         xba=.300, xslg=.485, woba=.386, xwoba=.363, xwobacon=.415, hard_hit_pct=46.2, k_pct=17.0, bb_pct=6.3),
    dict(season=2022, age=29, pitches=2720, batted_balls=527, barrels=40, barrel_pct=7.6,
         barrel_per_pa=5.6, exit_velo=88.9, max_ev=112.5, launch_angle=10.2, la_sweet_spot_pct=35.3,
         xba=.275, xslg=.446, woba=.350, xwoba=.338, xwobacon=.391, hard_hit_pct=41.6, k_pct=18.5, bb_pct=6.4),
    dict(season=2023, age=30, pitches=2675, batted_balls=490, barrels=41, barrel_pct=8.4,
         barrel_per_pa=5.9, exit_velo=89.9, max_ev=110.8, launch_angle=13.0, la_sweet_spot_pct=36.1,
         xba=.263, xslg=.453, woba=.333, xwoba=.331, xwobacon=.396, hard_hit_pct=42.2, k_pct=21.7, bb_pct=6.5),
    dict(season=2024, age=31, pitches=2043, batted_balls=408, barrels=28, barrel_pct=6.9,
         barrel_per_pa=5.2, exit_velo=89.1, max_ev=110.6, launch_angle=11.5, la_sweet_spot_pct=30.9,
         xba=.263, xslg=.430, woba=.349, xwoba=.323, xwobacon=.370, hard_hit_pct=40.7, k_pct=18.2, bb_pct=5.0),
    dict(season=2025, age=32, pitches=2407, batted_balls=484, barrels=28, barrel_pct=5.8,
         barrel_per_pa=4.4, exit_velo=89.3, max_ev=111.7, launch_angle=9.1, la_sweet_spot_pct=34.7,
         xba=.270, xslg=.410, woba=.352, xwoba=.321, xwobacon=.356, hard_hit_pct=42.1, k_pct=16.7, bb_pct=6.7),
    dict(season=2026, age=33, pitches=1724, batted_balls=317, barrels=21, barrel_pct=6.6,
         barrel_per_pa=4.7, exit_velo=88.9, max_ev=110.1, launch_angle=10.0, la_sweet_spot_pct=33.1,
         xba=.244, xslg=.372, woba=.299, xwoba=.295, xwobacon=.351, hard_hit_pct=41.6, k_pct=22.7, bb_pct=6.2),
]

TURNER_CAREER = dict(
    pitches=23347, batted_balls=4469, barrels=308, barrel_pct=7.2, barrel_per_pa=5.1,
    exit_velo=89.4, xba=.275, xslg=.441, woba=.350, xwoba=.335, xwobacon=.385,
    hard_hit_pct=41.2, k_pct=18.7, bb_pct=6.8,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, xba=.243, xslg=.407,
    woba=.316, xwoba=.316, xwobacon=.369, hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
