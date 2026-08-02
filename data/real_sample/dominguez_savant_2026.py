"""
data/real_sample/dominguez_savant_2026.py
----------------------------------------
Real Baseball Savant data for Jasson Dominguez, transcribed by hand from
screenshots the user captured directly from the Savant app. Almost the
entire 2026 percentile chart is flagged "NOT QUALIFIED" (only Arm
Strength and Sprint Speed carry real percentiles) -- 2026 was a limited,
injury/role-affected sample (630 pitches seen, 128 batted balls, the
smallest of any player in the roster). Raw values are real and included
throughout; percentiles are only included for the two fields Savant
actually ranked. Treat this player's 2026 row with that caveat when
using it for model training.
"""

DOMINGUEZ_2026_SNAPSHOT = {
    "player_name": "Jasson Dominguez",
    "season": 2026,
    "batting_run_value": -2,  # NOT QUALIFIED
    "xwoba": 0.302,  # NOT QUALIFIED
    "xba": 0.266,  # NOT QUALIFIED
    "xslg": 0.388,  # NOT QUALIFIED
    "avg_exit_velo": 88.3,  # NOT QUALIFIED
    "barrel_pct": 5.5,  # NOT QUALIFIED
    "hard_hit_pct": 38.3,  # NOT QUALIFIED
    "la_sweet_spot_pct": 30.5,  # NOT QUALIFIED
    "bat_speed": 74.5,  # NOT QUALIFIED
    "squared_up_pct": 22.2,  # NOT QUALIFIED
    "chase_pct": 36.2,  # NOT QUALIFIED
    "whiff_pct": 24.5,  # NOT QUALIFIED
    "k_pct": 20.3,  # NOT QUALIFIED
    "bb_pct": 4.1,  # NOT QUALIFIED
    "arm_strength": 93.6, "arm_strength_pctl": 95,  # the only qualified fielding metric
    "sprint_speed": 28.5, "sprint_speed_pctl": 82,  # the only qualified running metric
}

DOMINGUEZ_SEASONS = [
    dict(season=2023, age=20, pitches=120, batted_balls=23, barrels=4, barrel_pct=17.4,
         barrel_per_pa=12.1, exit_velo=89.6, max_ev=110.2, launch_angle=-0.8, la_sweet_spot_pct=43.5,
         xba=.274, xslg=.539, woba=.403, xwoba=.363, xwobacon=.460, hard_hit_pct=56.5, k_pct=24.2, bb_pct=6.1),
    dict(season=2024, age=21, pitches=278, batted_balls=37, barrels=4, barrel_pct=11.1,
         barrel_per_pa=6.0, exit_velo=89.4, max_ev=109.3, launch_angle=5.1, la_sweet_spot_pct=24.3,
         xba=.202, xslg=.338, woba=.285, xwoba=.309, xwobacon=.355, hard_hit_pct=45.9, k_pct=28.4, bb_pct=16.4),
    dict(season=2025, age=22, pitches=1692, batted_balls=270, barrels=19, barrel_pct=7.0,
         barrel_per_pa=4.4, exit_velo=90.6, max_ev=112.1, launch_angle=13.0, la_sweet_spot_pct=28.9,
         xba=.237, xslg=.370, woba=.316, xwoba=.306, xwobacon=.375, hard_hit_pct=49.6, k_pct=26.8, bb_pct=9.6),
    dict(season=2026, age=23, pitches=630, batted_balls=128, barrels=7, barrel_pct=5.5,
         barrel_per_pa=4.1, exit_velo=88.3, max_ev=110.8, launch_angle=15.3, la_sweet_spot_pct=30.5,
         xba=.266, xslg=.388, woba=.293, xwoba=.302, xwobacon=.360, hard_hit_pct=38.3, k_pct=20.3, bb_pct=4.1),
]

DOMINGUEZ_CAREER = dict(
    pitches=2720, batted_balls=458, barrels=34, barrel_pct=7.4, barrel_per_pa=4.9,
    exit_velo=89.8, max_ev=112.1, launch_angle=12.3, la_sweet_spot_pct=29.7,
    xba=.243, xslg=.380, woba=.311, xwoba=.308, xwobacon=.373, hard_hit_pct=46.5, k_pct=25.2, bb_pct=8.7,
)
