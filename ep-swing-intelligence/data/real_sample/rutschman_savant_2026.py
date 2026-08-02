"""
data/real_sample/rutschman_savant_2026.py
----------------------------------------
Real Baseball Savant data for Adley Rutschman, transcribed by hand from
screenshots the user captured directly from the Savant app. The
inverse-of-Henderson case: Bat Speed only 29th pctl but Squared-Up% 90th
-- pure bat-to-ball skill compensating for well-below-average bat speed,
closer in shape to the "contact puro" group despite batting as a middle-
of-order catcher. Also the only catcher in the roster, so includes
Savant's Catching percentile block (Framing 97th, CS Above Avg 99th)
for context even though those aren't used by the swing model.
"""

RUTSCHMAN_2026_SNAPSHOT = {
    "player_name": "Adley Rutschman",
    "season": 2026,
    "batting_run_value": 3, "batting_run_value_pctl": 58,
    "xwoba": 0.348, "xwoba_pctl": 75,
    "xba": 0.274, "xba_pctl": 84,
    "xslg": 0.432, "xslg_pctl": 64,
    "avg_exit_velo": 89.4, "avg_exit_velo_pctl": 51,
    "barrel_pct": 7.1, "barrel_pct_pctl": 40,
    "hard_hit_pct": 42.0, "hard_hit_pct_pctl": 53,
    "la_sweet_spot_pct": 40.6, "la_sweet_spot_pct_pctl": 95,
    "bat_speed": 70.8, "bat_speed_pctl": 29,
    "squared_up_pct": 32.3, "squared_up_pct_pctl": 90,
    "chase_pct": 25.1, "chase_pct_pctl": 78,
    "whiff_pct": 15.8, "whiff_pct_pctl": 91,
    "k_pct": 14.1, "k_pct_pctl": 86,
    "bb_pct": 10.6, "bb_pct_pctl": 70,
    "sprint_speed": 26.2, "sprint_speed_pctl": 23,
    # Catching-specific percentiles (not used by the swing model, kept for context)
    "catching_blocks_above_avg_pctl": 78, "catching_blocks_above_avg": 3,
    "catching_cs_above_avg_pctl": 99, "catching_cs_above_avg": 5,
    "catching_framing_pctl": 97, "catching_framing": 5,
    "catching_pop_time_pctl": 47, "catching_pop_time": 1.95,
}

RUTSCHMAN_SEASONS = [
    dict(season=2022, age=24, pitches=2009, batted_balls=315, barrels=25, barrel_pct=7.9,
         barrel_per_pa=5.3, exit_velo=87.9, max_ev=110.9, launch_angle=15.6, la_sweet_spot_pct=35.6,
         xba=.243, xslg=.417, woba=.354, xwoba=.341, xwobacon=.357, hard_hit_pct=36.8, k_pct=18.3, bb_pct=13.8),
    dict(season=2023, age=25, pitches=2904, batted_balls=492, barrels=37, barrel_pct=7.5,
         barrel_per_pa=5.4, exit_velo=88.4, max_ev=111.1, launch_angle=12.6, la_sweet_spot_pct=37.0,
         xba=.289, xslg=.473, woba=.352, xwoba=.374, xwobacon=.393, hard_hit_pct=38.6, k_pct=14.7, bb_pct=13.4),
    dict(season=2024, age=26, pitches=2593, batted_balls=475, barrels=29, barrel_pct=6.1,
         barrel_per_pa=4.5, exit_velo=88.2, max_ev=109.3, launch_angle=18.8, la_sweet_spot_pct=35.4,
         xba=.254, xslg=.405, woba=.309, xwoba=.320, xwobacon=.346, hard_hit_pct=36.6, k_pct=16.1, bb_pct=9.1),
    dict(season=2025, age=27, pitches=1491, batted_balls=267, barrels=20, barrel_pct=7.5,
         barrel_per_pa=5.5, exit_velo=89.4, max_ev=111.3, launch_angle=13.7, la_sweet_spot_pct=33.7,
         xba=.241, xslg=.410, woba=.298, xwoba=.325, xwobacon=.338, hard_hit_pct=38.6, k_pct=15.6, bb_pct=11.0),
    dict(season=2026, age=28, pitches=1162, batted_balls=212, barrels=15, barrel_pct=7.1,
         barrel_per_pa=5.3, exit_velo=89.4, max_ev=110.3, launch_angle=14.9, la_sweet_spot_pct=40.6,
         xba=.274, xslg=.432, woba=.333, xwoba=.348, xwobacon=.361, hard_hit_pct=42.0, k_pct=14.1, bb_pct=10.6),
]

RUTSCHMAN_CAREER = dict(
    pitches=10159, batted_balls=1761, barrels=126, barrel_pct=7.2, barrel_per_pa=5.2,
    exit_velo=88.5, max_ev=111.3, launch_angle=15.2, la_sweet_spot_pct=36.2,
    xba=.262, xslg=.430, woba=.331, xwoba=.343, xwobacon=.362, hard_hit_pct=38.2, k_pct=15.8, bb_pct=11.7,
)
