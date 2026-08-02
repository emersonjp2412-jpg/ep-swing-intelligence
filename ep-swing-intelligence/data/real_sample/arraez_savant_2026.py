"""
data/real_sample/arraez_savant_2026.py
-----------------------------------------
Real Baseball Savant data for Luis Arraez, transcribed by hand from
screenshots the user captured directly from the Savant app. This is the
pure-contact archetype the sample was missing — lowest bat speed in the
collected roster (63.2 mph, 1st percentile) paired with the highest
Squared-Up% (42.4%, 100th percentile) and near-zero K% (100th percentile).
"""

ARRAEZ_2026_SNAPSHOT = {
    "player_name": "Luis Arraez",
    "season": 2026,
    "batting_run_value": 11, "batting_run_value_pctl": 78,
    "xwoba": 0.304, "xwoba_pctl": 30,
    "xba": 0.286, "xba_pctl": 91,
    "xslg": 0.371, "xslg_pctl": 28,
    "avg_exit_velo": 87.0, "avg_exit_velo_pctl": 17,
    "barrel_pct": 0.5, "barrel_pct_pctl": 1,
    "hard_hit_pct": 21.0, "hard_hit_pct_pctl": 1,
    "la_sweet_spot_pct": 40.4, "la_sweet_spot_pct_pctl": 94,
    "bat_speed": 63.2, "bat_speed_pctl": 1,
    "squared_up_pct": 42.4, "squared_up_pct_pctl": 100,
    "chase_pct": 32.3, "chase_pct_pctl": 34,
    "whiff_pct": 7.8, "whiff_pct_pctl": 100,
    "k_pct": 4.4, "k_pct_pctl": 100,
    "bb_pct": 5.8, "bb_pct_pctl": 15,
    "sprint_speed": 26.7, "sprint_speed_pctl": 32,
}

ARRAEZ_SEASONS = [
    dict(season=2019, age=22, pitches=1486, batted_balls=300, barrels=8, barrel_pct=2.8,
         barrel_per_pa=2.2, exit_velo=87.1, max_ev=102.2, launch_angle=11.4, la_sweet_spot_pct=41.7,
         xba=.287, xslg=.406, woba=.360, xwoba=.334, xwobacon=.324, hard_hit_pct=22.8, k_pct=7.9, bb_pct=9.8),
    dict(season=2020, age=23, pitches=512, batted_balls=102, barrels=4, barrel_pct=3.9,
         barrel_per_pa=3.3, exit_velo=87.5, max_ev=103.7, launch_angle=12.1, la_sweet_spot_pct=43.1,
         xba=.310, xslg=.453, woba=.335, xwoba=.357, xwobacon=.368, hard_hit_pct=30.4, k_pct=9.1, bb_pct=6.6),
    dict(season=2021, age=24, pitches=1975, batted_balls=386, barrels=9, barrel_pct=2.3,
         barrel_per_pa=1.9, exit_velo=88.4, max_ev=104.2, launch_angle=9.9, la_sweet_spot_pct=41.5,
         xba=.293, xslg=.419, woba=.321, xwoba=.340, xwobacon=.343, hard_hit_pct=30.6, k_pct=10.0, bb_pct=9.0),
    dict(season=2022, age=25, pitches=2413, batted_balls=507, barrels=18, barrel_pct=3.6,
         barrel_per_pa=3.0, exit_velo=88.9, max_ev=107.3, launch_angle=12.9, la_sweet_spot_pct=38.7,
         xba=.289, xslg=.429, woba=.350, xwoba=.341, xwobacon=.335, hard_hit_pct=30.2, k_pct=7.1, bb_pct=8.3),
    dict(season=2023, age=26, pitches=2161, batted_balls=544, barrels=19, barrel_pct=3.5,
         barrel_per_pa=3.1, exit_velo=88.3, max_ev=104.0, launch_angle=11.5, la_sweet_spot_pct=44.7,
         xba=.327, xslg=.461, woba=.369, xwoba=.355, xwobacon=.359, hard_hit_pct=25.7, k_pct=5.5, bb_pct=5.7),
    dict(season=2024, age=27, pitches=2416, batted_balls=611, barrels=10, barrel_pct=1.6,
         barrel_per_pa=1.5, exit_velo=86.3, max_ev=108.4, launch_angle=13.7, la_sweet_spot_pct=40.9,
         xba=.310, xslg=.408, woba=.323, xwoba=.330, xwobacon=.329, hard_hit_pct=23.7, k_pct=4.3, bb_pct=3.6),
    dict(season=2025, age=28, pitches=2467, batted_balls=618, barrels=7, barrel_pct=1.1,
         barrel_per_pa=1.0, exit_velo=86.1, max_ev=107.8, launch_angle=12.2, la_sweet_spot_pct=37.1,
         xba=.287, xslg=.363, woba=.313, xwoba=.303, xwobacon=.290, hard_hit_pct=16.7, k_pct=3.1, bb_pct=5.0),
    dict(season=2026, age=29, pitches=1600, batted_balls=386, barrels=2, barrel_pct=0.5,
         barrel_per_pa=0.5, exit_velo=87.0, max_ev=104.4, launch_angle=15.4, la_sweet_spot_pct=40.4,
         xba=.286, xslg=.371, woba=.349, xwoba=.304, xwobacon=.294, hard_hit_pct=21.0, k_pct=4.4, bb_pct=5.8),
]

ARRAEZ_CAREER = dict(
    pitches=15030, batted_balls=3454, barrels=77, barrel_pct=2.2, barrel_per_pa=1.9,
    exit_velo=87.4, max_ev=108.4, launch_angle=12.5, la_sweet_spot_pct=40.6,
    xba=.299, xslg=.410, woba=.339, xwoba=.331, xwobacon=.326, hard_hit_pct=24.3, k_pct=5.9, bb_pct=6.4,
)
