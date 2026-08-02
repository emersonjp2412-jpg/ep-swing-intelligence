"""
data/real_sample/delacruz_savant_2026.py
--------------------------------------------
Real Baseball Savant data for Elly De La Cruz, transcribed by hand from
screenshots the user captured directly from the Savant app.
"""

DELACRUZ_2026_SNAPSHOT = {
    "player_name": "Elly De La Cruz",
    "season": 2026,
    "batting_run_value": 17, "batting_run_value_pctl": 91,
    "xwoba": 0.368, "xwoba_pctl": 91,
    "xba": 0.277, "xba_pctl": 85,
    "xslg": 0.487, "xslg_pctl": 86,
    "avg_exit_velo": 94.1, "avg_exit_velo_pctl": 98,
    "barrel_pct": 14.5, "barrel_pct_pctl": 91,
    "hard_hit_pct": 52.1, "hard_hit_pct_pctl": 94,
    "la_sweet_spot_pct": 35.9, "la_sweet_spot_pct_pctl": 68,
    "bat_speed": 75.4, "bat_speed_pctl": 88,
    "squared_up_pct": 25.0, "squared_up_pct_pctl": 51,
    "chase_pct": 26.0, "chase_pct_pctl": 71,
    "whiff_pct": 27.4, "whiff_pct_pctl": 35,
    "k_pct": 26.9, "k_pct_pctl": 19,
    "bb_pct": 10.4, "bb_pct_pctl": 68,
    "sprint_speed": 28.3, "sprint_speed_pctl": 77,
}

DELACRUZ_SEASONS = [
    dict(season=2023, age=21, pitches=1755, batted_balls=246, barrels=21, barrel_pct=8.6,
         barrel_per_pa=4.9, exit_velo=91.2, max_ev=119.2, launch_angle=3.6, la_sweet_spot_pct=30.5,
         xba=.238, xslg=.396, woba=.305, xwoba=.305, xwobacon=.430, hard_hit_pct=45.9, k_pct=33.7, bb_pct=8.2),
    dict(season=2024, age=22, pitches=2751, batted_balls=403, barrels=51, barrel_pct=12.7,
         barrel_per_pa=7.3, exit_velo=91.8, max_ev=114.7, launch_angle=9.7, la_sweet_spot_pct=35.7,
         xba=.237, xslg=.437, woba=.349, xwoba=.330, xwobacon=.444, hard_hit_pct=45.7, k_pct=31.3, bb_pct=9.9),
    dict(season=2025, age=23, pitches=2678, batted_balls=449, barrels=46, barrel_pct=10.3,
         barrel_per_pa=6.6, exit_velo=91.0, max_ev=117.4, launch_angle=7.6, la_sweet_spot_pct=32.5,
         xba=.251, xslg=.424, woba=.333, xwoba=.322, xwobacon=.403, hard_hit_pct=44.2, k_pct=25.9, bb_pct=9.6),
    dict(season=2026, age=24, pitches=1515, batted_balls=234, barrels=33, barrel_pct=14.5,
         barrel_per_pa=8.8, exit_velo=94.1, max_ev=116.3, launch_angle=10.2, la_sweet_spot_pct=35.9,
         xba=.277, xslg=.487, woba=.368, xwoba=.368, xwobacon=.471, hard_hit_pct=52.1, k_pct=26.9, bb_pct=10.4),
]

DELACRUZ_CAREER = dict(
    pitches=8699, batted_balls=1332, barrels=151, barrel_pct=11.4, barrel_per_pa=6.9,
    exit_velo=91.8, max_ev=119.2, launch_angle=8.0, la_sweet_spot_pct=33.7,
    xba=.248, xslg=.433, woba=.338, xwoba=.329, xwobacon=.432, hard_hit_pct=46.4, k_pct=29.3, bb_pct=9.6,
)
