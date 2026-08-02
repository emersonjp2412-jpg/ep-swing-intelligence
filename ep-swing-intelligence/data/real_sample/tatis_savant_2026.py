"""
data/real_sample/tatis_savant_2026.py
----------------------------------------
Real Baseball Savant data for Fernando Tatis Jr., transcribed by hand from
screenshots the user captured directly from the Savant app. Note: 2022 is
missing from the season table (real gap — PED suspension, missed the
whole season), so this player's SEASONS list has a real jump from 2021 to 2023.
"""

TATIS_2026_SNAPSHOT = {
    "player_name": "Fernando Tatis Jr.",
    "season": 2026,
    "batting_run_value": 8, "batting_run_value_pctl": 71,
    "xwoba": 0.356, "xwoba_pctl": 82,
    "xba": 0.287, "xba_pctl": 92,
    "xslg": 0.441, "xslg_pctl": 70,
    "avg_exit_velo": 92.2, "avg_exit_velo_pctl": 89,
    "barrel_pct": 10.9, "barrel_pct_pctl": 69,
    "hard_hit_pct": 53.6, "hard_hit_pct_pctl": 96,
    "la_sweet_spot_pct": 30.8, "la_sweet_spot_pct_pctl": 19,
    "bat_speed": 76.0, "bat_speed_pctl": 91,
    "squared_up_pct": 27.2, "squared_up_pct_pctl": 70,
    "chase_pct": 27.5, "chase_pct_pctl": 64,
    "whiff_pct": 28.7, "whiff_pct_pctl": 27,
    "k_pct": 20.0, "k_pct_pctl": 60,
    "bb_pct": 8.9, "bb_pct_pctl": 49,
    "sprint_speed": 28.9, "sprint_speed_pctl": 89,
}

TATIS_SEASONS = [
    dict(season=2019, age=20, pitches=1399, batted_balls=227, barrels=30, barrel_pct=14.2,
         barrel_per_pa=8.1, exit_velo=90.4, max_ev=115.9, launch_angle=6.7, la_sweet_spot_pct=33.5,
         xba=.256, xslg=.491, woba=.398, xwoba=.347, xwobacon=.463, hard_hit_pct=44.1, k_pct=29.6, bb_pct=8.1),
    dict(season=2020, age=21, pitches=988, batted_balls=164, barrels=32, barrel_pct=19.5,
         barrel_per_pa=12.5, exit_velo=95.9, max_ev=113.4, launch_angle=8.7, la_sweet_spot_pct=32.3,
         xba=.297, xslg=.614, woba=.392, xwoba=.422, xwobacon=.526, hard_hit_pct=62.2, k_pct=23.7, bb_pct=10.5),
    dict(season=2021, age=22, pitches=2141, batted_balls=329, barrels=70, barrel_pct=21.3,
         barrel_per_pa=12.8, exit_velo=93.9, max_ev=116.6, launch_angle=13.8, la_sweet_spot_pct=33.1,
         xba=.274, xslg=.620, woba=.403, xwoba=.407, xwobacon=.545, hard_hit_pct=55.6, k_pct=28.0, bb_pct=11.4),
    # 2022 missing on purpose — Tatis served a PED suspension and did not play that season.
    dict(season=2023, age=24, pitches=2335, batted_balls=438, barrels=48, barrel_pct=11.0,
         barrel_per_pa=7.6, exit_velo=91.9, max_ev=113.4, launch_angle=11.0, la_sweet_spot_pct=31.5,
         xba=.276, xslg=.513, woba=.332, xwoba=.364, xwobacon=.439, hard_hit_pct=49.3, k_pct=22.2, bb_pct=8.3),
    dict(season=2024, age=25, pitches=1551, batted_balls=303, barrels=44, barrel_pct=14.6,
         barrel_per_pa=10.0, exit_velo=93.5, max_ev=116.7, launch_angle=10.0, la_sweet_spot_pct=33.7,
         xba=.294, xslg=.548, woba=.359, xwoba=.390, xwobacon=.475, hard_hit_pct=55.8, k_pct=21.9, bb_pct=7.3),
    dict(season=2025, age=26, pitches=2636, batted_balls=467, barrels=51, barrel_pct=11.0,
         barrel_per_pa=7.4, exit_velo=93.3, max_ev=113.4, launch_angle=9.4, la_sweet_spot_pct=28.9,
         xba=.272, xslg=.488, woba=.353, xwoba=.370, xwobacon=.412, hard_hit_pct=51.8, k_pct=18.7, bb_pct=12.9),
    dict(season=2026, age=27, pitches=1656, batted_balls=321, barrels=35, barrel_pct=10.9,
         barrel_per_pa=7.6, exit_velo=92.2, max_ev=115.7, launch_angle=4.7, la_sweet_spot_pct=30.8,
         xba=.287, xslg=.441, woba=.329, xwoba=.356, xwobacon=.411, hard_hit_pct=53.6, k_pct=20.0, bb_pct=8.9),
]

TATIS_CAREER = dict(
    pitches=12706, batted_balls=2249, barrels=310, barrel_pct=13.9, barrel_per_pa=9.1,
    exit_velo=92.9, max_ev=116.7, launch_angle=9.4, la_sweet_spot_pct=31.7,
    xba=.278, xslg=.525, woba=.362, xwoba=.377, xwobacon=.459, hard_hit_pct=52.6, k_pct=23.0, bb_pct=9.8,
)
