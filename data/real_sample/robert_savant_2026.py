"""
data/real_sample/robert_savant_2026.py
----------------------------------------
Real Baseball Savant data for Luis Robert Jr. (CHW), transcribed by hand
from screenshots the user captured directly from the Savant app. 2026 is a
small, injury-affected sample (449 pitches, 77 batted balls) -- Batting
Run Value and most Batting-section stats are NOT QUALIFIED, only raw
values shown. Kept in for the power-profile/injury-risk variance it adds
even though most 2026 percentiles are unavailable.
"""

ROBERT_2026_SNAPSHOT = {
    "player_name": "Luis Robert Jr.",
    "season": 2026,
    "batting_run_value": 0, "batting_run_value_pctl": None,  # NOT QUALIFIED
    "baserunning_run_value": -1, "baserunning_run_value_pctl": None,
    "fielding_run_value": 0, "fielding_run_value_pctl": None,
    "xwoba": 0.323, "xwoba_pctl": None,
    "xba": 0.235, "xba_pctl": None,
    "xslg": 0.390, "xslg_pctl": None,
    "avg_exit_velo": 89.2, "avg_exit_velo_pctl": None,
    "barrel_pct": 3.9, "barrel_pct_pctl": None,
    "hard_hit_pct": 41.6, "hard_hit_pct_pctl": None,
    "la_sweet_spot_pct": 22.1, "la_sweet_spot_pct_pctl": None,
    "bat_speed": 75.9, "bat_speed_pctl": None,
    "squared_up_pct": 20.0, "squared_up_pct_pctl": None,
    "chase_pct": 33.7, "chase_pct_pctl": None,
    "whiff_pct": 26.6, "whiff_pct_pctl": None,
    "k_pct": 20.0, "k_pct_pctl": None,
    "bb_pct": 13.0, "bb_pct_pctl": None,
    "range_oaa": -1, "range_oaa_pctl": None,
    "arm_strength": 84.8, "arm_strength_pctl": 52,
    "sprint_speed": 29.1, "sprint_speed_pctl": 91,
}

ROBERT_SEASONS = [
    dict(season=2020, age=22, pitches=882, batted_balls=131, barrels=17, barrel_pct=13.2,
         barrel_per_pa=7.5, exit_velo=87.9, max_ev=115.8, launch_angle=16.7, la_sweet_spot_pct=36.6,
         xba=.225, xslg=.466, woba=.316, xwoba=.329, xwobacon=.455, hard_hit_pct=40.5, k_pct=32.2, bb_pct=8.8),
    dict(season=2021, age=23, pitches=963, batted_balls=216, barrels=27, barrel_pct=12.8,
         barrel_per_pa=9.1, exit_velo=91.2, max_ev=117.7, launch_angle=13.8, la_sweet_spot_pct=39.4,
         xba=.300, xslg=.555, woba=.399, xwoba=.385, xwobacon=.470, hard_hit_pct=45.1, k_pct=20.6, bb_pct=4.7),
    dict(season=2022, age=24, pitches=1349, batted_balls=304, barrels=27, barrel_pct=8.9,
         barrel_per_pa=6.7, exit_velo=89.3, max_ev=117.8, launch_angle=10.0, la_sweet_spot_pct=32.6,
         xba=.277, xslg=.470, woba=.324, xwoba=.336, xwobacon=.399, hard_hit_pct=42.8, k_pct=19.2, bb_pct=4.2),
    dict(season=2023, age=25, pitches=2200, batted_balls=376, barrels=58, barrel_pct=15.5,
         barrel_per_pa=9.7, exit_velo=89.1, max_ev=113.6, launch_angle=16.1, la_sweet_spot_pct=38.0,
         xba=.256, xslg=.516, woba=.358, xwoba=.347, xwobacon=.470, hard_hit_pct=42.3, k_pct=28.9, bb_pct=5.0),
    dict(season=2024, age=26, pitches=1609, batted_balls=253, barrels=25, barrel_pct=9.9,
         barrel_per_pa=5.9, exit_velo=90.1, max_ev=113.0, launch_angle=13.5, la_sweet_spot_pct=35.6,
         xba=.211, xslg=.378, woba=.285, xwoba=.283, xwobacon=.395, hard_hit_pct=40.7, k_pct=33.2, bb_pct=6.6),
    dict(season=2025, age=27, pitches=1524, batted_balls=274, barrels=28, barrel_pct=10.3,
         barrel_per_pa=6.5, exit_velo=89.4, max_ev=115.8, launch_angle=18.2, la_sweet_spot_pct=34.7,
         xba=.246, xslg=.426, woba=.289, xwoba=.321, xwobacon=.401, hard_hit_pct=41.6, k_pct=26.0, bb_pct=9.3),
    dict(season=2026, age=28, pitches=449, batted_balls=77, barrels=3, barrel_pct=3.9,
         barrel_per_pa=2.6, exit_velo=89.2, max_ev=112.4, launch_angle=14.6, la_sweet_spot_pct=22.1,
         xba=.235, xslg=.390, woba=.303, xwoba=.323, xwobacon=.346, hard_hit_pct=41.6, k_pct=20.0, bb_pct=13.0),
]

ROBERT_CAREER = dict(
    pitches=8976, batted_balls=1631, barrels=185, barrel_pct=11.4, barrel_per_pa=7.4,
    exit_velo=89.5, max_ev=117.8, launch_angle=14.6, la_sweet_spot_pct=35.4,
    xba=.252, xslg=.464, woba=.327, xwoba=.331, xwobacon=.426,
    hard_hit_pct=42.2, k_pct=26.5, bb_pct=6.6,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, xba=.243, xslg=.407,
    woba=.316, xwoba=.316, xwobacon=.369, hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
