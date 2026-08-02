"""
data/real_sample/walker_savant_2026.py
----------------------------------------
Real Baseball Savant data for Jordan Walker, transcribed by hand from
screenshots the user captured directly from the Savant app. A textbook
"elite bat speed, well below-average bat control" case: Bat Speed 100th
percentile (79.2 mph, tied for the fastest raw reading in the roster
alongside Caminero) against Squared-Up% in the 19th -- and 2026 shows a
real breakout in production (Batting Run Value +20, 93rd pctl) despite
that gap, suggesting the power output is compensating for contact
quality rather than the two working together.
"""

WALKER_2026_SNAPSHOT = {
    "player_name": "Jordan Walker",
    "season": 2026,
    "batting_run_value": 20, "batting_run_value_pctl": 93,
    "xwoba": 0.364, "xwoba_pctl": 89,
    "xba": 0.282, "xba_pctl": 90,
    "xslg": 0.499, "xslg_pctl": 90,
    "avg_exit_velo": 93.6, "avg_exit_velo_pctl": 96,
    "barrel_pct": 13.8, "barrel_pct_pctl": 87,
    "hard_hit_pct": 49.8, "hard_hit_pct_pctl": 89,
    "la_sweet_spot_pct": 33.9, "la_sweet_spot_pct_pctl": 47,
    "bat_speed": 79.2, "bat_speed_pctl": 100,
    "squared_up_pct": 21.0, "squared_up_pct_pctl": 19,
    "chase_pct": 35.6, "chase_pct_pctl": 19,
    "whiff_pct": 30.6, "whiff_pct_pctl": 18,
    "k_pct": 24.7, "k_pct_pctl": 30,
    "bb_pct": 8.1, "bb_pct_pctl": 40,
    "sprint_speed": 29.1, "sprint_speed_pctl": 92,
}

WALKER_SEASONS = [
    dict(season=2023, age=21, pitches=1667, batted_balls=318, barrels=24, barrel_pct=7.5,
         barrel_per_pa=5.2, exit_velo=89.4, max_ev=114.3, launch_angle=10.2, la_sweet_spot_pct=33.6,
         xba=.263, xslg=.430, woba=.341, xwoba=.332, xwobacon=.391, hard_hit_pct=42.5, k_pct=22.4, bb_pct=8.0),
    dict(season=2024, age=22, pitches=669, batted_balls=116, barrels=11, barrel_pct=9.5,
         barrel_per_pa=6.2, exit_velo=91.2, max_ev=115.5, launch_angle=9.4, la_sweet_spot_pct=29.3,
         xba=.206, xslg=.366, woba=.268, xwoba=.278, xwobacon=.355, hard_hit_pct=43.1, k_pct=28.1, bb_pct=5.6),
    dict(season=2025, age=23, pitches=1541, batted_balls=238, barrels=26, barrel_pct=10.9,
         barrel_per_pa=6.6, exit_velo=92.3, max_ev=117.9, launch_angle=10.3, la_sweet_spot_pct=29.0,
         xba=.207, xslg=.363, woba=.260, xwoba=.278, xwobacon=.370, hard_hit_pct=50.0, k_pct=31.8, bb_pct=7.3),
    dict(season=2026, age=24, pitches=1564, batted_balls=289, barrels=40, barrel_pct=13.8,
         barrel_per_pa=9.2, exit_velo=93.6, max_ev=116.6, launch_angle=11.3, la_sweet_spot_pct=33.9,
         xba=.282, xslg=.499, woba=.372, xwoba=.364, xwobacon=.456, hard_hit_pct=49.8, k_pct=24.7, bb_pct=8.1),
]

WALKER_CAREER = dict(
    pitches=5441, batted_balls=961, barrels=101, barrel_pct=10.5, barrel_per_pa=6.9,
    exit_velo=91.6, max_ev=117.9, launch_angle=10.5, la_sweet_spot_pct=32.0,
    xba=.247, xslg=.424, woba=.320, xwoba=.320, xwobacon=.401, hard_hit_pct=46.6, k_pct=26.3, bb_pct=7.5,
)
