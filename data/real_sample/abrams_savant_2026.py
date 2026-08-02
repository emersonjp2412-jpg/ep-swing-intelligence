"""
data/real_sample/abrams_savant_2026.py
----------------------------------------
Real Baseball Savant data for CJ Abrams (WSH), transcribed by hand from
screenshots the user captured directly from the Savant app. Closes out the
"Objetivo MLB" group (Phillies/Mets/Nationals). Notably strong 2026 season:
Batting Run Value 98th pctl, xSLG 81st, Barrel% 71st -- a breakout
bat-speed/power profile (72.9 mph, 60th pctl) paired with a low Chase%
percentile (15th) that's the outlier worth flagging in any Nationals-facing
writeup.
"""

ABRAMS_2026_SNAPSHOT = {
    "player_name": "CJ Abrams",
    "season": 2026,
    "batting_run_value": 29, "batting_run_value_pctl": 98,
    "baserunning_run_value": 1, "baserunning_run_value_pctl": 80,
    "fielding_run_value": -8, "fielding_run_value_pctl": 3,
    "xwoba": 0.350, "xwoba_pctl": 77,
    "xba": 0.262, "xba_pctl": 68,
    "xslg": 0.467, "xslg_pctl": 81,
    "avg_exit_velo": 89.8, "avg_exit_velo_pctl": 61,
    "barrel_pct": 11.0, "barrel_pct_pctl": 71,
    "hard_hit_pct": 42.3, "hard_hit_pct_pctl": 56,
    "la_sweet_spot_pct": 34.8, "la_sweet_spot_pct_pctl": 57,
    "bat_speed": 72.9, "bat_speed_pctl": 60,
    "squared_up_pct": 24.8, "squared_up_pct_pctl": 49,
    "chase_pct": 36.6, "chase_pct_pctl": 15,
    "whiff_pct": 27.6, "whiff_pct_pctl": 34,
    "k_pct": 21.3, "k_pct_pctl": 52,
    "bb_pct": 8.4, "bb_pct_pctl": 43,
    "range_oaa": -11, "range_oaa_pctl": 1,
    "arm_strength": 83.1, "arm_strength_pctl": 40,
    "sprint_speed": 28.5, "sprint_speed_pctl": 82,
}

ABRAMS_SEASONS = [
    dict(season=2022, age=21, pitches=1008, batted_balls=238, barrels=5, barrel_pct=2.1,
         barrel_per_pa=1.7, exit_velo=86.5, max_ev=109.6, launch_angle=6.8, la_sweet_spot_pct=28.6,
         xba=.244, xslg=.327, woba=.267, xwoba=.272, xwobacon=.304, hard_hit_pct=30.7, k_pct=16.6, bb_pct=1.7),
    dict(season=2023, age=22, pitches=2212, batted_balls=451, barrels=31, barrel_pct=6.9,
         barrel_per_pa=5.0, exit_velo=87.4, max_ev=112.5, launch_angle=13.5, la_sweet_spot_pct=32.6,
         xba=.243, xslg=.402, woba=.306, xwoba=.304, xwobacon=.345, hard_hit_pct=35.9, k_pct=19.2, bb_pct=5.2),
    dict(season=2024, age=23, pitches=2261, batted_balls=418, barrels=29, barrel_pct=7.0,
         barrel_per_pa=4.8, exit_velo=88.2, max_ev=110.0, launch_angle=15.1, la_sweet_spot_pct=33.0,
         xba=.243, xslg=.413, woba=.322, xwoba=.320, xwobacon=.370, hard_hit_pct=40.7, k_pct=21.3, bb_pct=6.6),
    dict(season=2025, age=24, pitches=2320, batted_balls=459, barrels=35, barrel_pct=7.6,
         barrel_per_pa=5.5, exit_velo=88.7, max_ev=112.7, launch_angle=13.3, la_sweet_spot_pct=34.4,
         xba=.245, xslg=.401, woba=.324, xwoba=.309, xwobacon=.350, hard_hit_pct=39.2, k_pct=19.7, bb_pct=5.8),
    dict(season=2026, age=25, pitches=1617, batted_balls=293, barrels=32, barrel_pct=11.0,
         barrel_per_pa=7.4, exit_velo=89.8, max_ev=110.8, launch_angle=18.9, la_sweet_spot_pct=34.8,
         xba=.262, xslg=.467, woba=.391, xwoba=.350, xwobacon=.407, hard_hit_pct=42.3, k_pct=21.3, bb_pct=8.4),
]

ABRAMS_CAREER = dict(
    pitches=9418, batted_balls=1859, barrels=132, barrel_pct=7.1, barrel_per_pa=5.1,
    exit_velo=88.2, max_ev=112.7, launch_angle=13.8, la_sweet_spot_pct=33.0,
    xba=.247, xslg=.406, woba=.324, xwoba=.313, xwobacon=.357,
    hard_hit_pct=38.1, k_pct=19.9, bb_pct=5.8,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, xba=.243, xslg=.407,
    woba=.316, xwoba=.316, xwobacon=.369, hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
