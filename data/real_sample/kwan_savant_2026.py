"""
data/real_sample/kwan_savant_2026.py
---------------------------------------
Real Baseball Savant data for Steven Kwan, transcribed by hand from
screenshots the user captured directly from the Savant app. A second
pure-contact data point alongside Arraez — nearly identical bat speed
(62.8 vs 63.2 mph) and Squared-Up% (both 100th percentile).
"""

KWAN_2026_SNAPSHOT = {
    "player_name": "Steven Kwan",
    "season": 2026,
    "batting_run_value": -3, "batting_run_value_pctl": 30,
    "xwoba": 0.322, "xwoba_pctl": 53,
    "xba": 0.270, "xba_pctl": 79,
    "xslg": 0.331, "xslg_pctl": 11,
    "avg_exit_velo": 83.4, "avg_exit_velo_pctl": 1,
    "barrel_pct": 0.3, "barrel_pct_pctl": 1,
    "hard_hit_pct": 9.5, "hard_hit_pct_pctl": 1,
    "la_sweet_spot_pct": 40.7, "la_sweet_spot_pct_pctl": 96,
    "bat_speed": 62.8, "bat_speed_pctl": 1,
    "squared_up_pct": 42.4, "squared_up_pct_pctl": 100,
    "chase_pct": 21.3, "chase_pct_pctl": 94,
    "whiff_pct": 8.7, "whiff_pct_pctl": 100,
    "k_pct": 9.8, "k_pct_pctl": 97,
    "bb_pct": 13.1, "bb_pct_pctl": 89,
    "sprint_speed": 27.0, "sprint_speed_pctl": 40,
}

KWAN_SEASONS = [
    dict(season=2022, age=24, pitches=2643, batted_balls=509, barrels=7, barrel_pct=1.4,
         barrel_per_pa=1.1, exit_velo=85.1, max_ev=107.1, launch_angle=11.8, la_sweet_spot_pct=34.6,
         xba=.269, xslg=.350, woba=.341, xwoba=.315, xwobacon=.302, hard_hit_pct=20.8, k_pct=9.4, bb_pct=9.7),
    dict(season=2023, age=25, pitches=2843, batted_balls=570, barrels=6, barrel_pct=1.1,
         barrel_per_pa=0.8, exit_velo=86.0, max_ev=105.2, launch_angle=10.7, la_sweet_spot_pct=37.7,
         xba=.281, xslg=.362, woba=.313, xwoba=.319, xwobacon=.314, hard_hit_pct=18.8, k_pct=10.4, bb_pct=9.7),
    dict(season=2024, age=26, pitches=2165, batted_balls=431, barrels=11, barrel_pct=2.6,
         barrel_per_pa=2.0, exit_velo=86.3, max_ev=105.6, launch_angle=14.9, la_sweet_spot_pct=38.5,
         xba=.283, xslg=.392, woba=.349, xwoba=.337, xwobacon=.329, hard_hit_pct=23.7, k_pct=9.4, bb_pct=9.8),
    dict(season=2025, age=27, pitches=2786, batted_balls=575, barrels=11, barrel_pct=1.9,
         barrel_per_pa=1.6, exit_velo=86.2, max_ev=104.2, launch_angle=15.6, la_sweet_spot_pct=39.7,
         xba=.273, xslg=.366, woba=.310, xwoba=.310, xwobacon=.305, hard_hit_pct=19.3, k_pct=8.7, bb_pct=7.9),
    dict(season=2026, age=28, pitches=1524, batted_balls=295, barrels=1, barrel_pct=0.3,
         barrel_per_pa=0.3, exit_velo=83.4, max_ev=101.1, launch_angle=14.1, la_sweet_spot_pct=40.7,
         xba=.270, xslg=.331, woba=.304, xwoba=.322, xwobacon=.295, hard_hit_pct=9.5, k_pct=9.8, bb_pct=13.1),
]

KWAN_CAREER = dict(
    pitches=11961, batted_balls=2380, barrels=36, barrel_pct=1.5, barrel_per_pa=1.2,
    exit_velo=85.6, max_ev=107.1, launch_angle=13.3, la_sweet_spot_pct=38.0,
    xba=.276, xslg=.362, woba=.324, xwoba=.320, xwobacon=.310, hard_hit_pct=19.1, k_pct=9.5, bb_pct=9.8,
)
