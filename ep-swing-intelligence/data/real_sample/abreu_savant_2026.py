"""
data/real_sample/abreu_savant_2026.py
----------------------------------------
Real Baseball Savant data for Wilyer Abreu, transcribed by hand from
screenshots the user captured directly from the Savant app. The second
of the four EP-TSP case-study players (SRI methodology validation case
study). A near-even Bat Speed/Squared-Up% profile (70th / 43rd) with
plus fielding value (89th) and elite arm strength (98th) -- a genuine
all-around tools case rather than a bat-only one.
"""

ABREU_2026_SNAPSHOT = {
    "player_name": "Wilyer Abreu",
    "season": 2026,
    "batting_run_value": 4, "batting_run_value_pctl": 58,
    "xwoba": 0.343, "xwoba_pctl": 72,
    "xba": 0.256, "xba_pctl": 60,
    "xslg": 0.468, "xslg_pctl": 82,
    "avg_exit_velo": 89.8, "avg_exit_velo_pctl": 61,
    "barrel_pct": 12.6, "barrel_pct_pctl": 83,
    "hard_hit_pct": 42.1, "hard_hit_pct_pctl": 54,
    "la_sweet_spot_pct": 36.1, "la_sweet_spot_pct_pctl": 70,
    "bat_speed": 73.8, "bat_speed_pctl": 70,
    "squared_up_pct": 24.2, "squared_up_pct_pctl": 43,
    "chase_pct": 31.5, "chase_pct_pctl": 38,
    "whiff_pct": 24.2, "whiff_pct_pctl": 49,
    "k_pct": 20.8, "k_pct_pctl": 56,
    "bb_pct": 9.6, "bb_pct_pctl": 59,
    "sprint_speed": 28.1, "sprint_speed_pctl": 70,
}

ABREU_SEASONS = [
    dict(season=2023, age=24, pitches=361, batted_balls=53, barrels=5, barrel_pct=9.6,
         barrel_per_pa=5.9, exit_velo=91.3, max_ev=109.4, launch_angle=11.9, la_sweet_spot_pct=35.8,
         xba=.263, xslg=.483, woba=.375, xwoba=.356, xwobacon=.455, hard_hit_pct=49.1, k_pct=27.1, bb_pct=10.6),
    dict(season=2024, age=25, pitches=1806, batted_balls=279, barrels=31, barrel_pct=11.2,
         barrel_per_pa=6.9, exit_velo=91.6, max_ev=114.4, launch_angle=19.2, la_sweet_spot_pct=33.7,
         xba=.229, xslg=.433, woba=.336, xwoba=.324, xwobacon=.413, hard_hit_pct=50.5, k_pct=28.0, bb_pct=8.9),
    dict(season=2025, age=26, pitches=1600, batted_balls=276, barrels=34, barrel_pct=12.3,
         barrel_per_pa=8.2, exit_velo=90.8, max_ev=111.7, launch_angle=23.0, la_sweet_spot_pct=31.9,
         xba=.243, xslg=.475, woba=.334, xwoba=.335, xwobacon=.413, hard_hit_pct=44.9, k_pct=24.2, bb_pct=9.6),
    dict(season=2026, age=27, pitches=1733, batted_balls=302, barrels=38, barrel_pct=12.6,
         barrel_per_pa=8.7, exit_velo=89.8, max_ev=113.1, launch_angle=18.6, la_sweet_spot_pct=36.1,
         xba=.256, xslg=.468, woba=.331, xwoba=.343, xwobacon=.398, hard_hit_pct=42.1, k_pct=20.8, bb_pct=9.6),
]

ABREU_CAREER = dict(
    pitches=5500, batted_balls=910, barrels=108, barrel_pct=11.9, barrel_per_pa=7.8,
    exit_velo=90.7, max_ev=114.4, launch_angle=19.7, la_sweet_spot_pct=34.1,
    xba=.244, xslg=.460, woba=.336, xwoba=.335, xwobacon=.410, hard_hit_pct=45.9, k_pct=24.5, bb_pct=9.4,
)
