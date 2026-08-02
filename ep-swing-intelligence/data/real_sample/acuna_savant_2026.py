"""
data/real_sample/acuna_savant_2026.py
----------------------------------------
Real Baseball Savant data for Ronald Acuna Jr., transcribed by hand from
screenshots the user captured directly from the Savant app. Bat Speed
and Squared-Up% are both flagged "NOT QUALIFIED" on the percentile chart
(insufficient qualifying swings in 2026 for a rank, likely due to an
injury-shortened season -- 957 pitches vs. a full-season ~2500), so
those two percentile fields are omitted here rather than guessed; the
raw values (76.0 mph bat speed, 21.3% squared-up) are still real and
included. A "power that's currently underperforming its bat speed"
case for the model.
"""

ACUNA_2026_SNAPSHOT = {
    "player_name": "Ronald Acuna Jr.",
    "season": 2026,
    "batting_run_value": 6, "batting_run_value_pctl": 65,
    "xwoba": 0.378, "xwoba_pctl": 94,
    "xba": 0.253, "xba_pctl": 55,
    "xslg": 0.489, "xslg_pctl": 87,
    "avg_exit_velo": 90.1, "avg_exit_velo_pctl": 67,
    "barrel_pct": 13.1, "barrel_pct_pctl": 85,
    "hard_hit_pct": 43.4, "hard_hit_pct_pctl": 63,
    "la_sweet_spot_pct": 32.4, "la_sweet_spot_pct_pctl": 31,
    "bat_speed": 76.0,  # NOT QUALIFIED on percentile chart (insufficient swings in 2026)
    "squared_up_pct": 21.3,  # NOT QUALIFIED on percentile chart
    "chase_pct": 25.0, "chase_pct_pctl": 78,
    "whiff_pct": 29.3, "whiff_pct_pctl": 25,
    "k_pct": 22.0, "k_pct_pctl": 48,
    "bb_pct": 14.8, "bb_pct_pctl": 96,
    "sprint_speed": 27.3, "sprint_speed_pctl": 50,
}

ACUNA_SEASONS = [
    dict(season=2018, age=20, pitches=1985, batted_balls=313, barrels=42, barrel_pct=14.2,
         barrel_per_pa=8.6, exit_velo=90.9, max_ev=113.9, launch_angle=13.1, la_sweet_spot_pct=34.2,
         xba=.271, xslg=.535, woba=.388, xwoba=.372, xwobacon=.473, hard_hit_pct=46.6, k_pct=25.3, bb_pct=9.2),
    dict(season=2019, age=21, pitches=3048, batted_balls=439, barrels=66, barrel_pct=16.2,
         barrel_per_pa=9.2, exit_velo=90.6, max_ev=115.9, launch_angle=14.2, la_sweet_spot_pct=40.5,
         xba=.279, xslg=.574, woba=.369, xwoba=.390, xwobacon=.502, hard_hit_pct=47.4, k_pct=26.3, bb_pct=10.6),
    dict(season=2020, age=22, pitches=876, batted_balls=100, barrels=16, barrel_pct=16.2,
         barrel_per_pa=7.9, exit_velo=92.3, max_ev=114.8, launch_angle=18.1, la_sweet_spot_pct=34.0,
         xba=.256, xslg=.594, woba=.413, xwoba=.422, xwobacon=.565, hard_hit_pct=56.0, k_pct=29.7, bb_pct=18.8),
    dict(season=2021, age=23, pitches=1449, batted_balls=217, barrels=44, barrel_pct=20.4,
         barrel_per_pa=12.2, exit_velo=93.8, max_ev=117.9, launch_angle=18.2, la_sweet_spot_pct=39.6,
         xba=.290, xslg=.610, woba=.412, xwoba=.430, xwobacon=.530, hard_hit_pct=54.8, k_pct=23.6, bb_pct=13.6),
    dict(season=2022, age=24, pitches=2162, batted_balls=344, barrels=44, barrel_pct=12.9,
         barrel_per_pa=8.3, exit_velo=91.2, max_ev=116.6, launch_angle=10.8, la_sweet_spot_pct=32.8,
         xba=.270, xslg=.496, woba=.335, xwoba=.368, xwobacon=.448, hard_hit_pct=49.7, k_pct=23.6, bb_pct=9.9),
    dict(season=2023, age=25, pitches=2782, batted_balls=562, barrels=86, barrel_pct=15.3,
         barrel_per_pa=11.7, exit_velo=94.7, max_ev=121.2, launch_angle=7.4, la_sweet_spot_pct=33.6,
         xba=.351, xslg=.668, woba=.428, xwoba=.461, xwobacon=.494, hard_hit_pct=55.2, k_pct=11.4, bb_pct=10.9),
    dict(season=2024, age=26, pitches=905, batted_balls=139, barrels=13, barrel_pct=9.4,
         barrel_per_pa=5.9, exit_velo=92.2, max_ev=114.2, launch_angle=8.5, la_sweet_spot_pct=31.7,
         xba=.256, xslg=.430, woba=.322, xwoba=.350, xwobacon=.410, hard_hit_pct=48.2, k_pct=23.9, bb_pct=12.2),
    dict(season=2025, age=27, pitches=1741, batted_balls=236, barrels=37, barrel_pct=15.7,
         barrel_per_pa=9.0, exit_velo=92.7, max_ev=115.5, launch_angle=13.3, la_sweet_spot_pct=30.9,
         xba=.263, xslg=.535, woba=.403, xwoba=.397, xwobacon=.481, hard_hit_pct=52.5, k_pct=24.8, bb_pct=17.2),
    dict(season=2026, age=28, pitches=957, batted_balls=145, barrels=19, barrel_pct=13.1,
         barrel_per_pa=8.1, exit_velo=90.1, max_ev=113.3, launch_angle=17.6, la_sweet_spot_pct=32.4,
         xba=.253, xslg=.489, woba=.350, xwoba=.378, xwobacon=.431, hard_hit_pct=43.4, k_pct=22.0, bb_pct=14.8),
]

ACUNA_CAREER = dict(
    pitches=15905, batted_balls=2495, barrels=367, barrel_pct=15.0, barrel_per_pa=9.4,
    exit_velo=92.2, max_ev=121.2, launch_angle=12.4, la_sweet_spot_pct=34.9,
    xba=.286, xslg=.563, woba=.384, xwoba=.402, xwobacon=.483, hard_hit_pct=50.7, k_pct=22.4, bb_pct=12.1,
)
