"""
data/real_sample/chourio_savant_2026.py
----------------------------------------
Real Baseball Savant data for Jackson Chourio, transcribed by hand from
screenshots the user captured directly from the Savant app. One of the
original Player Intelligence Report subjects from earlier EP work,
now with real bat-tracking data. A near-balanced Bat Speed/Squared-Up%
profile (77th / 57th) with a real 2026 breakout in Avg Exit Velo
(89.3 -> 92.3) and Barrel% (9.7 -> 12.7) year over year.
"""

CHOURIO_2026_SNAPSHOT = {
    "player_name": "Jackson Chourio",
    "season": 2026,
    "batting_run_value": 6, "batting_run_value_pctl": 66,
    "xwoba": 0.330, "xwoba_pctl": 60,
    "xba": 0.250, "xba_pctl": 49,
    "xslg": 0.458, "xslg_pctl": 77,
    "avg_exit_velo": 92.3, "avg_exit_velo_pctl": 89,
    "barrel_pct": 12.7, "barrel_pct_pctl": 84,
    "hard_hit_pct": 46.2, "hard_hit_pct_pctl": 78,
    "la_sweet_spot_pct": 32.4, "la_sweet_spot_pct_pctl": 31,
    "bat_speed": 74.6, "bat_speed_pctl": 77,
    "squared_up_pct": 25.7, "squared_up_pct_pctl": 57,
    "chase_pct": 33.4, "chase_pct_pctl": 27,
    "whiff_pct": 23.7, "whiff_pct_pctl": 53,
    "k_pct": 24.8, "k_pct_pctl": 29,
    "bb_pct": 7.5, "bb_pct_pctl": 32,
    "sprint_speed": 28.7, "sprint_speed_pctl": 87,
}

CHOURIO_SEASONS = [
    dict(season=2024, age=20, pitches=2103, batted_balls=410, barrels=32, barrel_pct=7.8,
         barrel_per_pa=5.6, exit_velo=89.7, max_ev=111.6, launch_angle=7.6, la_sweet_spot_pct=33.2,
         xba=.267, xslg=.431, woba=.339, xwoba=.327, xwobacon=.390, hard_hit_pct=44.9, k_pct=21.1, bb_pct=6.8),
    dict(season=2025, age=21, pitches=2108, batted_balls=435, barrels=42, barrel_pct=9.7,
         barrel_per_pa=7.1, exit_velo=89.3, max_ev=113.7, launch_angle=10.6, la_sweet_spot_pct=34.0,
         xba=.247, xslg=.426, woba=.328, xwoba=.307, xwobacon=.364, hard_hit_pct=42.3, k_pct=20.5, bb_pct=5.1),
    dict(season=2026, age=22, pitches=1251, batted_balls=213, barrels=27, barrel_pct=12.7,
         barrel_per_pa=8.5, exit_velo=92.3, max_ev=113.3, launch_angle=13.0, la_sweet_spot_pct=32.4,
         xba=.250, xslg=.458, woba=.346, xwoba=.330, xwobacon=.411, hard_hit_pct=46.2, k_pct=24.8, bb_pct=7.5),
]

CHOURIO_CAREER = dict(
    pitches=5462, batted_balls=1058, barrels=101, barrel_pct=9.6, barrel_per_pa=6.8,
    exit_velo=90.1, max_ev=113.7, launch_angle=9.9, la_sweet_spot_pct=33.4,
    xba=.255, xslg=.435, woba=.336, xwoba=.320, xwobacon=.383, hard_hit_pct=44.1, k_pct=21.7, bb_pct=6.3,
)
