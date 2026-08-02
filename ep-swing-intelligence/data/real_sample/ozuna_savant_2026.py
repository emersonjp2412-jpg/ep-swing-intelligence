"""
data/real_sample/ozuna_savant_2026.py
----------------------------------------
Real Baseball Savant data for Marcell Ozuna (ATL), transcribed by hand from
screenshots the user captured directly from the Savant app. Full-time DH
in 2026 -- Fielding Run Value, Range (OAA), and Arm Strength are not
applicable/not qualified, left as None rather than fabricated. Notable
contrast point: Squared-Up% only 12th pctl despite a fully-qualified 68th
pctl Bat Speed -- a bat-speed-without-contact-quality profile the dataset
was missing.
"""

OZUNA_2026_SNAPSHOT = {
    "player_name": "Marcell Ozuna",
    "season": 2026,
    "batting_run_value": -12, "batting_run_value_pctl": 5,
    "baserunning_run_value": -1, "baserunning_run_value_pctl": 32,
    "fielding_run_value": None, "fielding_run_value_pctl": None,  # DH, not applicable
    "xwoba": 0.307, "xwoba_pctl": 34,
    "xba": 0.221, "xba_pctl": 15,
    "xslg": 0.394, "xslg_pctl": 46,
    "avg_exit_velo": 89.3, "avg_exit_velo_pctl": 49,
    "barrel_pct": 8.3, "barrel_pct_pctl": 52,
    "hard_hit_pct": 38.1, "hard_hit_pct_pctl": 35,
    "la_sweet_spot_pct": 39.4, "la_sweet_spot_pct_pctl": 91,
    "bat_speed": 73.6, "bat_speed_pctl": 68,
    "squared_up_pct": 19.9, "squared_up_pct_pctl": 12,
    "chase_pct": 26.2, "chase_pct_pctl": 70,
    "whiff_pct": 30.3, "whiff_pct_pctl": 19,
    "k_pct": 29.7, "k_pct_pctl": 11,
    "bb_pct": 10.0, "bb_pct_pctl": 63,
    "range_oaa": None, "range_oaa_pctl": None,  # DH, not applicable
    "arm_strength": None, "arm_strength_pctl": None,
    "sprint_speed": 24.9, "sprint_speed_pctl": 5,
}

OZUNA_SEASONS = [
    dict(season=2015, age=24, pitches=1832, batted_balls=351, barrels=21, barrel_pct=6.7,
         barrel_per_pa=4.3, exit_velo=91.8, max_ev=114.5, launch_angle=7.2, la_sweet_spot_pct=29.3,
         xba=.261, xslg=.420, woba=.302, xwoba=.321, xwobacon=.389, hard_hit_pct=45.0, k_pct=22.3, bb_pct=6.1),
    dict(season=2016, age=25, pitches=2225, batted_balls=446, barrels=35, barrel_pct=8.6,
         barrel_per_pa=5.8, exit_velo=90.8, max_ev=113.8, launch_angle=10.9, la_sweet_spot_pct=32.3,
         xba=.272, xslg=.465, woba=.330, xwoba=.340, xwobacon=.392, hard_hit_pct=42.2, k_pct=18.9, bb_pct=7.1),
    dict(season=2017, age=26, pitches=2560, batted_balls=471, barrels=44, barrel_pct=10.2,
         barrel_per_pa=6.5, exit_velo=90.9, max_ev=114.5, launch_angle=10.2, la_sweet_spot_pct=31.0,
         xba=.279, xslg=.514, woba=.388, xwoba=.364, xwobacon=.434, hard_hit_pct=45.6, k_pct=21.2, bb_pct=9.4),
    dict(season=2018, age=27, pitches=2322, batted_balls=476, barrels=46, barrel_pct=10.4,
         barrel_per_pa=7.3, exit_velo=91.5, max_ev=117.2, launch_angle=10.8, la_sweet_spot_pct=30.3,
         xba=.280, xslg=.492, woba=.327, xwoba=.354, xwobacon=.408, hard_hit_pct=45.1, k_pct=17.5, bb_pct=6.1),
    dict(season=2019, age=28, pitches=2260, batted_balls=372, barrels=45, barrel_pct=13.1,
         barrel_per_pa=8.2, exit_velo=91.8, max_ev=115.3, launch_angle=13.5, la_sweet_spot_pct=32.8,
         xba=.280, xslg=.528, woba=.336, xwoba=.375, xwobacon=.440, hard_hit_pct=49.2, k_pct=20.8, bb_pct=11.3),
    dict(season=2020, age=29, pitches=1074, batted_balls=169, barrels=26, barrel_pct=15.4,
         barrel_per_pa=9.7, exit_velo=93.0, max_ev=115.6, launch_angle=16.4, la_sweet_spot_pct=39.1,
         xba=.310, xslg=.632, woba=.444, xwoba=.434, xwobacon=.533, hard_hit_pct=54.4, k_pct=22.5, bb_pct=14.2),
    dict(season=2021, age=30, pitches=758, batted_balls=142, barrels=14, barrel_pct=9.9,
         barrel_per_pa=6.7, exit_velo=89.7, max_ev=114.3, launch_angle=14.5, la_sweet_spot_pct=35.2,
         xba=.262, xslg=.464, woba=.284, xwoba=.346, xwobacon=.409, hard_hit_pct=40.8, k_pct=22.1, bb_pct=9.1),
    dict(season=2022, age=31, pitches=2023, batted_balls=352, barrels=46, barrel_pct=13.1,
         barrel_per_pa=9.1, exit_velo=89.4, max_ev=113.9, launch_angle=16.5, la_sweet_spot_pct=31.8,
         xba=.250, xslg=.490, woba=.298, xwoba=.337, xwobacon=.421, hard_hit_pct=43.8, k_pct=24.1, bb_pct=6.1),
    dict(season=2023, age=32, pitches=2366, batted_balls=398, barrels=66, barrel_pct=16.7,
         barrel_per_pa=11.1, exit_velo=91.8, max_ev=115.3, launch_angle=15.6, la_sweet_spot_pct=34.9,
         xba=.277, xslg=.585, woba=.381, xwoba=.395, xwobacon=.483, hard_hit_pct=49.0, k_pct=22.6, bb_pct=9.6),
    dict(season=2024, age=33, pitches=2875, batted_balls=440, barrels=68, barrel_pct=15.5,
         barrel_per_pa=9.9, exit_velo=92.1, max_ev=114.8, launch_angle=14.4, la_sweet_spot_pct=40.5,
         xba=.283, xslg=.583, woba=.395, xwoba=.404, xwobacon=.512, hard_hit_pct=53.4, k_pct=24.7, bb_pct=10.8),
    dict(season=2025, age=34, pitches=2635, batted_balls=350, barrels=40, barrel_pct=11.5,
         barrel_per_pa=6.8, exit_velo=89.9, max_ev=112.1, launch_angle=14.1, la_sweet_spot_pct=35.1,
         xba=.239, xslg=.448, woba=.334, xwoba=.354, xwobacon=.407, hard_hit_pct=44.6, k_pct=24.3, bb_pct=15.9),
    dict(season=2026, age=35, pitches=1186, batted_balls=160, barrels=13, barrel_pct=8.3,
         barrel_per_pa=4.8, exit_velo=89.3, max_ev=111.2, launch_angle=19.9, la_sweet_spot_pct=39.4,
         xba=.221, xslg=.394, woba=.275, xwoba=.307, xwobacon=.394, hard_hit_pct=38.1, k_pct=29.7, bb_pct=10.0),
]

OZUNA_CAREER = dict(
    pitches=24116, batted_balls=4127, barrels=464, barrel_pct=11.8, barrel_per_pa=7.6,
    exit_velo=91.1, max_ev=117.2, launch_angle=13.0, la_sweet_spot_pct=33.7,
    xba=.269, xslg=.505, woba=.345, xwoba=.362, xwobacon=.435,
    hard_hit_pct=46.3, k_pct=22.2, bb_pct=9.5,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, xba=.243, xslg=.407,
    woba=.316, xwoba=.316, xwobacon=.369, hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
