"""
data/real_sample/freeman_savant_2026.py
----------------------------------------
Real Baseball Savant data for Freddie Freeman, transcribed by hand from
screenshots the user captured directly from the Savant app. The
"balance" data point of the contact-hitter subgroup: still 90th-pctl
xSLG and 63rd-pctl Squared-Up% despite a bottom-quartile Bat Speed
(25th) -- shows plus bat-to-ball skill can offset average bat speed at
the top of the aging curve (age 36, 12 real seasons on file).
"""

FREEMAN_2026_SNAPSHOT = {
    "player_name": "Freddie Freeman",
    "season": 2026,
    "batting_run_value": 18, "batting_run_value_pctl": 92,
    "xwoba": 0.385, "xwoba_pctl": 96,
    "xba": 0.299, "xba_pctl": 98,
    "xslg": 0.502, "xslg_pctl": 90,
    "avg_exit_velo": 90.2, "avg_exit_velo_pctl": 70,
    "barrel_pct": 10.1, "barrel_pct_pctl": 63,
    "hard_hit_pct": 43.7, "hard_hit_pct_pctl": 64,
    "la_sweet_spot_pct": 38.3, "la_sweet_spot_pct_pctl": 86,
    "bat_speed": 70.4, "bat_speed_pctl": 25,
    "squared_up_pct": 26.5, "squared_up_pct_pctl": 63,
    "chase_pct": 27.7, "chase_pct_pctl": 64,
    "whiff_pct": 21.7, "whiff_pct_pctl": 65,
    "k_pct": 16.5, "k_pct_pctl": 76,
    "bb_pct": 11.3, "bb_pct_pctl": 74,
    "sprint_speed": 25.3, "sprint_speed_pctl": 8,
}

FREEMAN_SEASONS = [
    dict(season=2015, age=25, pitches=1871, batted_balls=320, barrels=36, barrel_pct=12.2,
         barrel_per_pa=7.5, exit_velo=90.6, max_ev=110.0, launch_angle=14.4, la_sweet_spot_pct=43.4,
         xba=.305, xslg=.571, woba=.364, xwoba=.415, xwobacon=.492, hard_hit_pct=44.7, k_pct=20.4, bb_pct=11.6),
    dict(season=2016, age=26, pitches=2779, batted_balls=423, barrels=56, barrel_pct=14.6,
         barrel_per_pa=8.1, exit_velo=91.3, max_ev=114.6, launch_angle=17.3, la_sweet_spot_pct=44.7,
         xba=.280, xslg=.566, woba=.402, xwoba=.396, xwobacon=.501, hard_hit_pct=44.7, k_pct=24.7, bb_pct=12.8),
    dict(season=2017, age=27, pitches=1929, batted_balls=347, barrels=46, barrel_pct=14.3,
         barrel_per_pa=8.9, exit_velo=89.7, max_ev=109.0, launch_angle=16.0, la_sweet_spot_pct=40.1,
         xba=.289, xslg=.591, woba=.407, xwoba=.403, xwobacon=.465, hard_hit_pct=42.7, k_pct=18.5, bb_pct=12.6),
    dict(season=2018, age=28, pitches=2663, batted_balls=492, barrels=46, barrel_pct=9.7,
         barrel_per_pa=6.5, exit_velo=89.1, max_ev=109.6, launch_angle=14.5, la_sweet_spot_pct=44.7,
         xba=.295, xslg=.530, woba=.378, xwoba=.385, xwobacon=.444, hard_hit_pct=39.8, k_pct=18.7, bb_pct=10.7),
    dict(season=2019, age=29, pitches=2750, batted_balls=472, barrels=58, barrel_pct=12.9,
         barrel_per_pa=8.4, exit_velo=89.7, max_ev=112.0, launch_angle=14.4, la_sweet_spot_pct=40.0,
         xba=.291, xslg=.565, woba=.387, xwoba=.394, xwobacon=.448, hard_hit_pct=42.5, k_pct=18.4, bb_pct=12.6),
    dict(season=2020, age=30, pitches=1021, batted_balls=177, barrels=26, barrel_pct=14.8,
         barrel_per_pa=9.9, exit_velo=92.4, max_ev=109.3, launch_angle=17.2, la_sweet_spot_pct=49.2,
         xba=.339, xslg=.660, woba=.456, xwoba=.464, xwobacon=.506, hard_hit_pct=54.2, k_pct=14.1, bb_pct=17.2),
    dict(season=2021, age=31, pitches=2688, batted_balls=495, barrels=57, barrel_pct=11.5,
         barrel_per_pa=8.2, exit_velo=91.4, max_ev=113.6, launch_angle=12.0, la_sweet_spot_pct=37.2,
         xba=.309, xslg=.577, woba=.379, xwoba=.410, xwobacon=.453, hard_hit_pct=46.1, k_pct=15.4, bb_pct=12.2),
    dict(season=2022, age=32, pitches=2755, batted_balls=517, barrels=51, barrel_pct=9.9,
         barrel_per_pa=7.2, exit_velo=91.3, max_ev=112.3, launch_angle=13.6, la_sweet_spot_pct=42.9,
         xba=.308, xslg=.559, woba=.393, xwoba=.406, xwobacon=.444, hard_hit_pct=47.8, k_pct=14.4, bb_pct=11.9),
    dict(season=2023, age=33, pitches=2753, batted_balls=521, barrels=58, barrel_pct=11.2,
         barrel_per_pa=7.9, exit_velo=90.0, max_ev=110.6, launch_angle=15.2, la_sweet_spot_pct=46.6,
         xba=.315, xslg=.567, woba=.411, xwoba=.406, xwobacon=.457, hard_hit_pct=42.2, k_pct=16.6, bb_pct=9.9),
    dict(season=2024, age=34, pitches=2522, batted_balls=450, barrels=41, barrel_pct=9.1,
         barrel_per_pa=6.4, exit_velo=89.4, max_ev=112.3, launch_angle=14.3, la_sweet_spot_pct=43.1,
         xba=.272, xslg=.475, woba=.365, xwoba=.369, xwobacon=.394, hard_hit_pct=41.8, k_pct=15.7, bb_pct=12.2),
    dict(season=2025, age=35, pitches=2382, batted_balls=433, barrels=45, barrel_pct=10.4,
         barrel_per_pa=7.2, exit_velo=90.9, max_ev=114.1, launch_angle=14.3, la_sweet_spot_pct=36.7,
         xba=.268, xslg=.467, woba=.370, xwoba=.350, xwobacon=.407, hard_hit_pct=45.7, k_pct=20.4, bb_pct=9.6),
    dict(season=2026, age=36, pitches=1817, batted_balls=316, barrels=32, barrel_pct=10.1,
         barrel_per_pa=7.2, exit_velo=90.2, max_ev=110.3, launch_angle=13.3, la_sweet_spot_pct=38.3,
         xba=.299, xslg=.502, woba=.377, xwoba=.385, xwobacon=.422, hard_hit_pct=43.7, k_pct=16.5, bb_pct=11.3),
]

FREEMAN_CAREER = dict(
    pitches=27930, batted_balls=4963, barrels=552, barrel_pct=11.4, barrel_per_pa=7.7,
    exit_velo=90.4, max_ev=114.6, launch_angle=14.5, la_sweet_spot_pct=42.0,
    xba=.295, xslg=.547, woba=.388, xwoba=.395, xwobacon=.449, hard_hit_pct=44.2, k_pct=18.0, bb_pct=11.8,
)
