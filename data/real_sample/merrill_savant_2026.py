"""
data/real_sample/merrill_savant_2026.py
----------------------------------------
Real Baseball Savant data for Jackson Merrill, transcribed by hand from
screenshots the user captured directly from the Savant app. A real
2026 regression case: Batting Run Value fell to the 9th percentile
despite a still-plus Bat Speed (67th) and strong power indicators
(xSLG 66th, Barrel% 64th) -- Squared-Up% (15th) and BB% (22nd) are the
clear drag, useful signal for the model that bat speed alone doesn't
guarantee batting production.
"""

MERRILL_2026_SNAPSHOT = {
    "player_name": "Jackson Merrill",
    "season": 2026,
    "batting_run_value": -10, "batting_run_value_pctl": 9,
    "xwoba": 0.317, "xwoba_pctl": 45,
    "xba": 0.249, "xba_pctl": 47,
    "xslg": 0.434, "xslg_pctl": 66,
    "avg_exit_velo": 89.7, "avg_exit_velo_pctl": 59,
    "barrel_pct": 10.2, "barrel_pct_pctl": 64,
    "hard_hit_pct": 45.9, "hard_hit_pct_pctl": 77,
    "la_sweet_spot_pct": 38.1, "la_sweet_spot_pct_pctl": 85,
    "bat_speed": 73.4, "bat_speed_pctl": 67,
    "squared_up_pct": 20.5, "squared_up_pct_pctl": 15,
    "chase_pct": 36.3, "chase_pct_pctl": 18,
    "whiff_pct": 26.7, "whiff_pct_pctl": 38,
    "k_pct": 24.5, "k_pct_pctl": 31,
    "bb_pct": 6.8, "bb_pct_pctl": 22,
    "sprint_speed": 29.0, "sprint_speed_pctl": 90,
}

MERRILL_SEASONS = [
    dict(season=2024, age=21, pitches=2214, batted_balls=462, barrels=52, barrel_pct=11.3,
         barrel_per_pa=8.8, exit_velo=90.4, max_ev=111.6, launch_angle=14.6, la_sweet_spot_pct=39.6,
         xba=.300, xslg=.547, woba=.352, xwoba=.375, xwobacon=.438, hard_hit_pct=43.9, k_pct=17.0, bb_pct=4.9),
    dict(season=2025, age=22, pitches=1703, batted_balls=338, barrels=44, barrel_pct=13.0,
         barrel_per_pa=9.1, exit_velo=89.7, max_ev=110.9, launch_angle=15.2, la_sweet_spot_pct=42.6,
         xba=.263, xslg=.490, woba=.331, xwoba=.347, xwobacon=.421, hard_hit_pct=42.9, k_pct=22.4, bb_pct=6.8),
    dict(season=2026, age=23, pitches=1707, batted_balls=294, barrels=30, barrel_pct=10.2,
         barrel_per_pa=7.0, exit_velo=89.7, max_ev=109.7, launch_angle=13.8, la_sweet_spot_pct=38.1,
         xba=.249, xslg=.434, woba=.289, xwoba=.317, xwobacon=.394, hard_hit_pct=45.9, k_pct=24.5, bb_pct=6.8),
]

MERRILL_CAREER = dict(
    pitches=5624, batted_balls=1094, barrels=126, barrel_pct=11.5, barrel_per_pa=8.4,
    exit_velo=90.0, max_ev=111.6, launch_angle=14.6, la_sweet_spot_pct=40.1,
    xba=.273, xslg=.497, woba=.327, xwoba=.350, xwobacon=.421, hard_hit_pct=44.1, k_pct=20.9, bb_pct=6.0,
)
