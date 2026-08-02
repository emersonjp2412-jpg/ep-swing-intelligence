"""
data/real_sample/langford_savant_2026.py
----------------------------------------
Real Baseball Savant data for Wyatt Langford, transcribed by hand from
screenshots the user captured directly from the Savant app. Bat Speed
and Squared-Up% are flagged "NOT QUALIFIED" on the 2026 percentile
chart (same situation as Dominguez -- insufficient qualifying swings,
consistent with a shortened 846-pitch season, the second-smallest 2026
sample in the roster after Dominguez). Raw values are real and
included; the two bat-tracking percentile fields are omitted rather
than guessed. Everything else on the chart (BB% 15th, xSLG 75th) is a
real, qualified percentile.
"""

LANGFORD_2026_SNAPSHOT = {
    "player_name": "Wyatt Langford",
    "season": 2026,
    "batting_run_value": 7, "batting_run_value_pctl": 70,
    "xwoba": 0.326, "xwoba_pctl": 56,
    "xba": 0.257, "xba_pctl": 62,
    "xslg": 0.450, "xslg_pctl": 75,
    "avg_exit_velo": 89.3, "avg_exit_velo_pctl": 49,
    "barrel_pct": 9.3, "barrel_pct_pctl": 57,
    "hard_hit_pct": 38.9, "hard_hit_pct_pctl": 38,
    "la_sweet_spot_pct": 35.2, "la_sweet_spot_pct_pctl": 60,
    "bat_speed": 72.8,  # NOT QUALIFIED
    "squared_up_pct": 26.7,  # NOT QUALIFIED
    "chase_pct": 28.4, "chase_pct_pctl": 60,
    "whiff_pct": 23.8, "whiff_pct_pctl": 52,
    "k_pct": 21.4, "k_pct_pctl": 51,
    "bb_pct": 5.8, "bb_pct_pctl": 15,
    "sprint_speed": 28.5, "sprint_speed_pctl": 83,
}

LANGFORD_SEASONS = [
    dict(season=2024, age=22, pitches=2256, batted_balls=387, barrels=36, barrel_pct=9.4,
         barrel_per_pa=6.5, exit_velo=89.6, max_ev=111.9, launch_angle=16.6, la_sweet_spot_pct=31.3,
         xba=.252, xslg=.435, woba=.321, xwoba=.332, xwobacon=.383, hard_hit_pct=43.4, k_pct=20.6, bb_pct=9.2),
    dict(season=2025, age=23, pitches=2335, batted_balls=343, barrels=48, barrel_pct=14.0,
         barrel_per_pa=8.4, exit_velo=91.4, max_ev=113.1, launch_angle=17.5, la_sweet_spot_pct=35.9,
         xba=.239, xslg=.448, woba=.337, xwoba=.346, xwobacon=.421, hard_hit_pct=48.4, k_pct=26.4, bb_pct=12.9),
    dict(season=2026, age=24, pitches=846, batted_balls=162, barrels=15, barrel_pct=9.3,
         barrel_per_pa=6.7, exit_velo=89.3, max_ev=111.3, launch_angle=17.9, la_sweet_spot_pct=35.2,
         xba=.257, xslg=.450, woba=.372, xwoba=.326, xwobacon=.390, hard_hit_pct=38.9, k_pct=21.4, bb_pct=5.8),
]

LANGFORD_CAREER = dict(
    pitches=5437, batted_balls=892, barrels=99, barrel_pct=11.1, barrel_per_pa=7.3,
    exit_velo=90.2, max_ev=113.1, launch_angle=17.2, la_sweet_spot_pct=33.7,
    xba=.247, xslg=.443, woba=.336, xwoba=.337, xwobacon=.399, hard_hit_pct=44.5, k_pct=23.2, bb_pct=10.2,
)
