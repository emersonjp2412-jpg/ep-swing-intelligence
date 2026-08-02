"""
data/real_sample/albies_savant_2026.py
----------------------------------------
Real Baseball Savant data for Ozzie Albies (ATL), transcribed by hand from
screenshots the user captured directly from the Savant app. Low-power /
contact-lean profile: Bat Speed only 14th pctl, but Squared-Up% 70th and
K% 83rd (low) -- another data point (alongside Turang) supporting the
"correct contact quality can outrun raw bat speed" pattern from the
original EP-TSP work.
"""

ALBIES_2026_SNAPSHOT = {
    "player_name": "Ozzie Albies",
    "season": 2026,
    "batting_run_value": 3, "batting_run_value_pctl": 56,
    "baserunning_run_value": -1, "baserunning_run_value_pctl": 36,
    "fielding_run_value": 1, "fielding_run_value_pctl": 53,
    "xwoba": 0.285, "xwoba_pctl": 12,
    "xba": 0.236, "xba_pctl": 30,
    "xslg": 0.361, "xslg_pctl": 23,
    "avg_exit_velo": 86.8, "avg_exit_velo_pctl": 14,
    "barrel_pct": 4.3, "barrel_pct_pctl": 17,
    "hard_hit_pct": 27.4, "hard_hit_pct_pctl": 5,
    "la_sweet_spot_pct": 34.0, "la_sweet_spot_pct_pctl": 49,
    "bat_speed": 69.0, "bat_speed_pctl": 14,
    "squared_up_pct": 27.2, "squared_up_pct_pctl": 70,
    "chase_pct": 38.1, "chase_pct_pctl": 9,
    "whiff_pct": 22.0, "whiff_pct_pctl": 63,
    "k_pct": 14.8, "k_pct_pctl": 83,
    "bb_pct": 6.6, "bb_pct_pctl": 20,
    "range_oaa": 3, "range_oaa_pctl": 83,
    "arm_strength": 70.6, "arm_strength_pctl": 2,
    "sprint_speed": 27.0, "sprint_speed_pctl": 40,
}

ALBIES_SEASONS = [
    dict(season=2017, age=20, pitches=912, batted_balls=184, barrels=9, barrel_pct=5.2,
         barrel_per_pa=3.7, exit_velo=87.3, max_ev=107.0, launch_angle=15.9, la_sweet_spot_pct=35.9,
         xba=.273, xslg=.442, woba=.347, xwoba=.339, xwobacon=.360, hard_hit_pct=26.6, k_pct=14.8, bb_pct=8.6),
    dict(season=2018, age=21, pitches=2386, batted_balls=527, barrels=25, barrel_pct=5.2,
         barrel_per_pa=3.7, exit_velo=86.8, max_ev=109.9, launch_angle=16.1, la_sweet_spot_pct=34.0,
         xba=.246, xslg=.398, woba=.324, xwoba=.301, xwobacon=.337, hard_hit_pct=29.4, k_pct=17.0, bb_pct=5.3),
    dict(season=2019, age=22, pitches=2494, batted_balls=532, barrels=35, barrel_pct=7.1,
         barrel_per_pa=5.0, exit_velo=88.9, max_ev=110.8, launch_angle=15.6, la_sweet_spot_pct=36.8,
         xba=.282, xslg=.482, woba=.354, xwoba=.346, xwobacon=.385, hard_hit_pct=34.0, k_pct=16.0, bb_pct=7.7),
    dict(season=2020, age=23, pitches=444, batted_balls=88, barrels=8, barrel_pct=9.1,
         barrel_per_pa=6.5, exit_velo=86.7, max_ev=106.5, launch_angle=17.8, la_sweet_spot_pct=35.2,
         xba=.234, xslg=.411, woba=.329, xwoba=.294, xwobacon=.367, hard_hit_pct=28.4, k_pct=24.2, bb_pct=4.0),
    dict(season=2021, age=24, pitches=2608, batted_balls=508, barrels=47, barrel_pct=9.3,
         barrel_per_pa=6.9, exit_velo=89.6, max_ev=111.4, launch_angle=21.1, la_sweet_spot_pct=37.0,
         xba=.250, xslg=.461, woba=.336, xwoba=.327, xwobacon=.375, hard_hit_pct=37.2, k_pct=18.7, bb_pct=6.9),
    dict(season=2022, age=25, pitches=1027, batted_balls=204, barrels=11, barrel_pct=5.4,
         barrel_per_pa=4.1, exit_velo=87.1, max_ev=106.6, launch_angle=16.9, la_sweet_spot_pct=34.8,
         xba=.238, xslg=.396, woba=.305, xwoba=.299, xwobacon=.333, hard_hit_pct=26.5, k_pct=17.5, bb_pct=5.9),
    dict(season=2023, age=26, pitches=2563, batted_balls=497, barrels=41, barrel_pct=8.3,
         barrel_per_pa=6.2, exit_velo=88.7, max_ev=110.7, launch_angle=16.6, la_sweet_spot_pct=37.4,
         xba=.263, xslg=.474, woba=.358, xwoba=.341, xwobacon=.377, hard_hit_pct=39.0, k_pct=16.2, bb_pct=7.0),
    dict(season=2024, age=27, pitches=1649, batted_balls=338, barrels=21, barrel_pct=6.2,
         barrel_per_pa=4.8, exit_velo=88.4, max_ev=113.7, launch_angle=18.4, la_sweet_spot_pct=33.4,
         xba=.246, xslg=.404, woba=.307, xwoba=.308, xwobacon=.330, hard_hit_pct=32.0, k_pct=14.9, bb_pct=6.2),
    dict(season=2025, age=28, pitches=2402, batted_balls=514, barrels=25, barrel_pct=4.9,
         barrel_per_pa=3.7, exit_velo=87.5, max_ev=109.9, launch_angle=18.7, la_sweet_spot_pct=33.5,
         xba=.243, xslg=.366, woba=.295, xwoba=.299, xwobacon=.310, hard_hit_pct=30.7, k_pct=14.1, bb_pct=8.2),
    dict(season=2026, age=29, pitches=1608, batted_balls=350, barrels=15, barrel_pct=4.3,
         barrel_per_pa=3.3, exit_velo=86.8, max_ev=108.7, launch_angle=17.8, la_sweet_spot_pct=34.0,
         xba=.236, xslg=.361, woba=.325, xwoba=.285, xwobacon=.300, hard_hit_pct=27.4, k_pct=14.8, bb_pct=6.6),
]

ALBIES_CAREER = dict(
    pitches=18093, batted_balls=3742, barrels=237, barrel_pct=6.5, barrel_per_pa=4.8,
    exit_velo=88.0, max_ev=113.7, launch_angle=17.6, la_sweet_spot_pct=35.3,
    xba=.253, xslg=.424, woba=.329, xwoba=.317, xwobacon=.348,
    hard_hit_pct=32.3, k_pct=16.3, bb_pct=6.8,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, xba=.243, xslg=.407,
    woba=.316, xwoba=.316, xwobacon=.369, hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
