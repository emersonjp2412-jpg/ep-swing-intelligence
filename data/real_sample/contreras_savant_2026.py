"""
data/real_sample/contreras_savant_2026.py
----------------------------------------
Real Baseball Savant data for William Contreras (MIL), transcribed by hand
from screenshots the user captured directly from the Savant app. First
catcher in the dataset -- adds catching-specific fields (Blocks Above Avg,
CS Above Avg, Framing, Pop Time) not present for position players, kept
here for completeness even though the current model doesn't use them.
Squared-Up% 91st pctl is the standout: well above his Bat Speed percentile
(63rd), another contact-over-power data point.
"""

CONTRERAS_2026_SNAPSHOT = {
    "player_name": "William Contreras",
    "season": 2026,
    "batting_run_value": 0, "batting_run_value_pctl": 44,
    "baserunning_run_value": -2, "baserunning_run_value_pctl": 5,
    "fielding_run_value": -2, "fielding_run_value_pctl": 30,
    "xwoba": 0.334, "xwoba_pctl": 63,
    "xba": 0.269, "xba_pctl": 78,
    "xslg": 0.438, "xslg_pctl": 68,
    "avg_exit_velo": 90.0, "avg_exit_velo_pctl": 65,
    "barrel_pct": 7.2, "barrel_pct_pctl": 42,
    "hard_hit_pct": 42.6, "hard_hit_pct_pctl": 60,
    "la_sweet_spot_pct": 31.0, "la_sweet_spot_pct_pctl": 21,
    "bat_speed": 73.2, "bat_speed_pctl": 63,
    "squared_up_pct": 32.4, "squared_up_pct_pctl": 91,
    "chase_pct": 28.6, "chase_pct_pctl": 59,
    "whiff_pct": 19.1, "whiff_pct_pctl": 79,
    "k_pct": 13.9, "k_pct_pctl": 87,
    "bb_pct": 8.7, "bb_pct_pctl": 46,
    "range_oaa": None, "range_oaa_pctl": None,  # catcher, not a standard range metric
    "arm_strength": None, "arm_strength_pctl": None,
    "sprint_speed": 25.8, "sprint_speed_pctl": 15,
    # Catching-specific (not used by the current 2-feature model, kept for completeness)
    "blocks_above_avg": -5, "blocks_above_avg_pctl": 9,
    "cs_above_avg": 5, "cs_above_avg_pctl": 100,
    "framing": -5, "framing_pctl": 5,
    "pop_time": 1.92, "pop_time_pctl": 68,
}

CONTRERAS_SEASONS = [
    dict(season=2020, age=22, pitches=36, batted_balls=6, barrels=1, barrel_pct=16.7,
         barrel_per_pa=10.0, exit_velo=84.6, max_ev=104.9, launch_angle=18.0, la_sweet_spot_pct=83.3,
         xba=.320, xslg=.466, woba=.389, xwoba=.338, xwobacon=.563, hard_hit_pct=16.7, k_pct=40.0, bb_pct=0.0),
    dict(season=2021, age=23, pitches=708, batted_balls=110, barrels=12, barrel_pct=11.0,
         barrel_per_pa=6.5, exit_velo=92.5, max_ev=114.2, launch_angle=8.2, la_sweet_spot_pct=28.2,
         xba=.223, xslg=.417, woba=.303, xwoba=.317, xwobacon=.404, hard_hit_pct=44.5, k_pct=29.2, bb_pct=10.3),
    dict(season=2022, age=24, pitches=1546, batted_balls=232, barrels=31, barrel_pct=13.4,
         barrel_per_pa=8.2, exit_velo=90.4, max_ev=115.2, launch_angle=6.1, la_sweet_spot_pct=31.9,
         xba=.236, xslg=.482, woba=.370, xwoba=.343, xwobacon=.439, hard_hit_pct=46.6, k_pct=27.7, bb_pct=10.4),
    dict(season=2023, age=25, pitches=2419, batted_balls=417, barrels=39, barrel_pct=9.4,
         barrel_per_pa=6.4, exit_velo=91.3, max_ev=113.9, launch_angle=4.7, la_sweet_spot_pct=27.1,
         xba=.247, xslg=.434, woba=.357, xwoba=.332, xwobacon=.375, hard_hit_pct=48.7, k_pct=20.6, bb_pct=10.3),
    dict(season=2024, age=26, pitches=2677, batted_balls=459, barrels=46, barrel_pct=10.0,
         barrel_per_pa=6.8, exit_velo=92.8, max_ev=118.1, launch_angle=6.1, la_sweet_spot_pct=29.0,
         xba=.261, xslg=.471, woba=.359, xwoba=.356, xwobacon=.408, hard_hit_pct=49.5, k_pct=20.5, bb_pct=11.5),
    dict(season=2025, age=27, pitches=2556, batted_balls=452, barrels=29, barrel_pct=6.4,
         barrel_per_pa=4.4, exit_velo=91.1, max_ev=114.1, launch_angle=7.0, la_sweet_spot_pct=31.6,
         xba=.248, xslg=.393, woba=.332, xwoba=.328, xwobacon=.348, hard_hit_pct=48.5, k_pct=18.2, bb_pct=12.7),
    dict(season=2026, age=28, pitches=1439, batted_balls=319, barrels=23, barrel_pct=7.2,
         barrel_per_pa=5.5, exit_velo=90.0, max_ev=112.7, launch_angle=11.6, la_sweet_spot_pct=31.0,
         xba=.269, xslg=.438, woba=.320, xwoba=.334, xwobacon=.354, hard_hit_pct=42.6, k_pct=13.9, bb_pct=8.7),
]

CONTRERAS_CAREER = dict(
    pitches=11381, batted_balls=1995, barrels=181, barrel_pct=9.1, barrel_per_pa=6.2,
    exit_velo=91.4, max_ev=118.1, launch_angle=7.0, la_sweet_spot_pct=30.0,
    xba=.251, xslg=.440, woba=.345, xwoba=.337, xwobacon=.383,
    hard_hit_pct=47.3, k_pct=20.6, bb_pct=10.9,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, xba=.243, xslg=.407,
    woba=.316, xwoba=.316, xwobacon=.369, hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
