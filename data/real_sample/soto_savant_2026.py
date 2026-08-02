"""
data/real_sample/soto_savant_2026.py
----------------------------------------
Real Baseball Savant data for Juan Soto, transcribed by hand from
screenshots the user captured directly from the Savant app. First
"balance" profile in the roster: elite everywhere in the plate-discipline
/ damage cluster (xwOBA 100th, BB% 99th, Chase% 96th) with a genuinely
average Bat Speed (50th pctl) -- proof that top-of-the-league production
doesn't require elite bat speed when swing decisions and Squared-Up%
(96th) are this good.
"""

SOTO_2026_SNAPSHOT = {
    "player_name": "Juan Soto",
    "season": 2026,
    "batting_run_value": 31, "batting_run_value_pctl": 99,
    "xwoba": 0.422, "xwoba_pctl": 100,
    "xba": 0.297, "xba_pctl": 97,
    "xslg": 0.589, "xslg_pctl": 99,
    "avg_exit_velo": 92.5, "avg_exit_velo_pctl": 92,
    "barrel_pct": 14.3, "barrel_pct_pctl": 90,
    "hard_hit_pct": 48.6, "hard_hit_pct_pctl": 87,
    "la_sweet_spot_pct": 31.6, "la_sweet_spot_pct_pctl": 27,
    "bat_speed": 72.1, "bat_speed_pctl": 50,
    "squared_up_pct": 34.9, "squared_up_pct_pctl": 96,
    "chase_pct": 19.8, "chase_pct_pctl": 96,
    "whiff_pct": 20.6, "whiff_pct_pctl": 71,
    "k_pct": 13.4, "k_pct_pctl": 91,
    "bb_pct": 17.5, "bb_pct_pctl": 99,
    "sprint_speed": 25.9, "sprint_speed_pctl": 16,
}

SOTO_SEASONS = [
    dict(season=2018, age=19, pitches=2031, batted_balls=316, barrels=31, barrel_pct=10.9,
         barrel_per_pa=6.3, exit_velo=90.5, max_ev=113.7, launch_angle=6.2, la_sweet_spot_pct=30.1,
         xba=.262, xslg=.483, woba=.392, xwoba=.372, xwobacon=.419, hard_hit_pct=42.2, k_pct=20.0, bb_pct=16.0),
    dict(season=2019, age=20, pitches=2788, batted_balls=416, barrels=51, barrel_pct=13.1,
         barrel_per_pa=7.7, exit_velo=92.0, max_ev=112.8, launch_angle=12.5, la_sweet_spot_pct=36.3,
         xba=.285, xslg=.575, woba=.394, xwoba=.409, xwobacon=.465, hard_hit_pct=47.8, k_pct=20.0, bb_pct=16.4),
    dict(season=2020, age=21, pitches=827, batted_balls=126, barrels=23, barrel_pct=18.3,
         barrel_per_pa=11.7, exit_velo=92.1, max_ev=113.3, launch_angle=4.3, la_sweet_spot_pct=33.3,
         xba=.332, xslg=.696, woba=.478, xwoba=.475, xwobacon=.527, hard_hit_pct=51.6, k_pct=14.3, bb_pct=20.9),
    dict(season=2021, age=22, pitches=2601, batted_balls=414, barrels=55, barrel_pct=13.3,
         barrel_per_pa=8.4, exit_velo=93.0, max_ev=116.6, launch_angle=5.8, la_sweet_spot_pct=29.7,
         xba=.299, xslg=.547, woba=.420, xwoba=.429, xwobacon=.446, hard_hit_pct=52.7, k_pct=14.2, bb_pct=22.2),
    dict(season=2022, age=23, pitches=2765, batted_balls=428, barrels=53, barrel_pct=12.4,
         barrel_per_pa=8.0, exit_velo=91.0, max_ev=113.2, launch_angle=9.1, la_sweet_spot_pct=28.5,
         xba=.263, xslg=.516, woba=.376, xwoba=.403, xwobacon=.405, hard_hit_pct=47.4, k_pct=14.5, bb_pct=20.3),
    dict(season=2023, age=24, pitches=2897, batted_balls=445, barrels=58, barrel_pct=13.1,
         barrel_per_pa=8.2, exit_velo=93.2, max_ev=115.3, launch_angle=6.7, la_sweet_spot_pct=28.5,
         xba=.279, xslg=.539, woba=.395, xwoba=.407, xwobacon=.445, hard_hit_pct=55.3, k_pct=18.2, bb_pct=18.6),
    dict(season=2024, age=25, pitches=2960, batted_balls=461, barrels=91, barrel_pct=19.8,
         barrel_per_pa=12.8, exit_velo=94.2, max_ev=115.7, launch_angle=10.7, la_sweet_spot_pct=35.4,
         xba=.310, xslg=.655, woba=.421, xwoba=.463, xwobacon=.518, hard_hit_pct=57.0, k_pct=16.7, bb_pct=18.1),
    dict(season=2025, age=26, pitches=2968, batted_balls=447, barrels=81, barrel_pct=18.2,
         barrel_per_pa=11.3, exit_velo=93.8, max_ev=115.0, launch_angle=12.0, la_sweet_spot_pct=32.9,
         xba=.288, xslg=.608, woba=.390, xwoba=.429, xwobacon=.491, hard_hit_pct=55.3, k_pct=19.2, bb_pct=17.8),
    dict(season=2026, age=27, pitches=1439, batted_balls=247, barrels=35, barrel_pct=14.3,
         barrel_per_pa=9.7, exit_velo=92.5, max_ev=114.2, launch_angle=16.3, la_sweet_spot_pct=31.6,
         xba=.297, xslg=.589, woba=.401, xwoba=.422, xwobacon=.444, hard_hit_pct=48.6, k_pct=13.4, bb_pct=17.5),
]

SOTO_CAREER = dict(
    pitches=21276, batted_balls=3300, barrels=478, barrel_pct=14.8, barrel_per_pa=9.3,
    exit_velo=92.6, max_ev=116.6, launch_angle=9.5, la_sweet_spot_pct=31.8,
    xba=.287, xslg=.571, woba=.402, xwoba=.420, xwobacon=.459, hard_hit_pct=51.3, k_pct=17.1, bb_pct=18.6,
)
