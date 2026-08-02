"""
data/real_sample/ohtani_savant_2026.py
----------------------------------------
Real Baseball Savant data for Shohei Ohtani (LAD), transcribed by hand
from screenshots the user captured directly from the Savant app. Full-time
DH in 2026 (pitching only) -- Fielding Run Value, Range (OAA), and Arm
Strength are not applicable. Elite across the board: xwOBA 98th pctl,
xSLG 98th, Bat Speed 79th, Squared-Up% 75th -- one of the few players in
the set with both elite power AND elite contact quality, an important
anchor point at the top of the swing-quality distribution.
"""

OHTANI_2026_SNAPSHOT = {
    "player_name": "Shohei Ohtani",
    "season": 2026,
    "batting_run_value": 21, "batting_run_value_pctl": 94,
    "baserunning_run_value": 0, "baserunning_run_value_pctl": 56,
    "fielding_run_value": None, "fielding_run_value_pctl": None,  # DH, not applicable
    "xwoba": 0.406, "xwoba_pctl": 98,
    "xba": 0.290, "xba_pctl": 94,
    "xslg": 0.566, "xslg_pctl": 98,
    "avg_exit_velo": 93.6, "avg_exit_velo_pctl": 96,
    "barrel_pct": 16.5, "barrel_pct_pctl": 96,
    "hard_hit_pct": 53.5, "hard_hit_pct_pctl": 96,
    "la_sweet_spot_pct": 38.5, "la_sweet_spot_pct_pctl": 87,
    "bat_speed": 74.7, "bat_speed_pctl": 79,
    "squared_up_pct": 27.9, "squared_up_pct_pctl": 75,
    "chase_pct": 29.2, "chase_pct_pctl": 55,
    "whiff_pct": 29.6, "whiff_pct_pctl": 24,
    "k_pct": 22.8, "k_pct_pctl": 44,
    "bb_pct": 14.0, "bb_pct_pctl": 94,
    "range_oaa": None, "range_oaa_pctl": None,
    "arm_strength": None, "arm_strength_pctl": None,
    "sprint_speed": 27.6, "sprint_speed_pctl": 56,
}

OHTANI_SEASONS = [
    dict(season=2018, age=23, pitches=1455, batted_balls=225, barrels=36, barrel_pct=16.7,
         barrel_per_pa=9.8, exit_velo=92.9, max_ev=113.9, launch_angle=12.4, la_sweet_spot_pct=35.6,
         xba=.272, xslg=.542, woba=.390, xwoba=.381, xwobacon=.502, hard_hit_pct=51.1, k_pct=27.9, bb_pct=10.1),
    dict(season=2019, age=24, pitches=1683, batted_balls=278, barrels=34, barrel_pct=13.1,
         barrel_per_pa=8.0, exit_velo=92.8, max_ev=115.1, launch_angle=6.8, la_sweet_spot_pct=31.7,
         xba=.280, xslg=.487, woba=.352, xwoba=.350, xwobacon=.446, hard_hit_pct=47.1, k_pct=25.9, bb_pct=7.8),
    dict(season=2020, age=25, pitches=739, batted_balls=103, barrels=11, barrel_pct=10.7,
         barrel_per_pa=6.3, exit_velo=89.1, max_ev=111.9, launch_angle=9.2, la_sweet_spot_pct=32.0,
         xba=.234, xslg=.423, woba=.290, xwoba=.331, xwobacon=.413, hard_hit_pct=42.7, k_pct=28.6, bb_pct=12.6),
    dict(season=2021, age=26, pitches=2594, batted_balls=350, barrels=78, barrel_pct=22.4,
         barrel_per_pa=12.2, exit_velo=93.6, max_ev=119.0, launch_angle=16.6, la_sweet_spot_pct=35.4,
         xba=.262, xslg=.622, woba=.393, xwoba=.410, xwobacon=.569, hard_hit_pct=53.6, k_pct=29.6, bb_pct=15.0),
    dict(season=2022, age=27, pitches=2546, batted_balls=428, barrels=72, barrel_pct=16.9,
         barrel_per_pa=10.8, exit_velo=92.9, max_ev=119.1, launch_angle=12.1, la_sweet_spot_pct=35.0,
         xba=.274, xslg=.569, woba=.370, xwoba=.387, xwobacon=.488, hard_hit_pct=49.8, k_pct=24.2, bb_pct=10.8),
    dict(season=2023, age=28, pitches=2321, batted_balls=357, barrels=70, barrel_pct=19.7,
         barrel_per_pa=11.7, exit_velo=94.4, max_ev=118.6, launch_angle=13.2, la_sweet_spot_pct=35.6,
         xba=.290, xslg=.646, woba=.433, xwoba=.428, xwobacon=.545, hard_hit_pct=54.2, k_pct=23.9, bb_pct=15.2),
    dict(season=2024, age=29, pitches=2838, batted_balls=479, barrels=103, barrel_pct=21.5,
         barrel_per_pa=14.1, exit_velo=95.8, max_ev=119.2, launch_angle=16.2, la_sweet_spot_pct=37.8,
         xba=.310, xslg=.672, woba=.431, xwoba=.444, xwobacon=.554, hard_hit_pct=60.1, k_pct=22.2, bb_pct=11.1),
    dict(season=2025, age=30, pitches=2865, batted_balls=426, barrels=100, barrel_pct=23.5,
         barrel_per_pa=13.8, exit_velo=94.9, max_ev=120.0, launch_angle=15.0, la_sweet_spot_pct=35.9,
         xba=.274, xslg=.649, woba=.418, xwoba=.425, xwobacon=.554, hard_hit_pct=58.7, k_pct=25.7, bb_pct=15.0),
    dict(season=2026, age=31, pitches=1676, batted_balls=273, barrels=45, barrel_pct=16.5,
         barrel_per_pa=10.2, exit_velo=93.6, max_ev=114.6, launch_angle=12.8, la_sweet_spot_pct=38.5,
         xba=.290, xslg=.566, woba=.383, xwoba=.406, xwobacon=.498, hard_hit_pct=53.5, k_pct=22.8, bb_pct=14.0),
]

OHTANI_CAREER = dict(
    pitches=18717, batted_balls=2919, barrels=549, barrel_pct=19.0, barrel_per_pa=11.5,
    exit_velo=93.9, max_ev=120.0, launch_angle=13.3, la_sweet_spot_pct=35.7,
    xba=.280, xslg=.598, woba=.396, xwoba=.405, xwobacon=.520,
    hard_hit_pct=53.7, k_pct=25.3, bb_pct=12.6,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, xba=.243, xslg=.407,
    woba=.316, xwoba=.316, xwobacon=.369, hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
