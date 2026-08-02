"""
data/real_sample/henderson_savant_2026.py
----------------------------------------
Real Baseball Savant data for Gunnar Henderson, transcribed by hand from
screenshots the user captured directly from the Savant app. Bat Speed
75th pctl but Squared-Up% only 30th -- the inverse of the "quality over
speed" pattern seen in the contact-hitter group, and a 2026 season that
shows real across-the-board decline from a strong 2024 peak (Barrel%
11.2 -> 7.2, xwOBA .375 -> .303), useful within-player variance for the
model.
"""

HENDERSON_2026_SNAPSHOT = {
    "player_name": "Gunnar Henderson",
    "season": 2026,
    "batting_run_value": 3, "batting_run_value_pctl": 55,
    "xwoba": 0.303, "xwoba_pctl": 28,
    "xba": 0.235, "xba_pctl": 28,
    "xslg": 0.383, "xslg_pctl": 38,
    "avg_exit_velo": 89.4, "avg_exit_velo_pctl": 51,
    "barrel_pct": 7.2, "barrel_pct_pctl": 42,
    "hard_hit_pct": 44.2, "hard_hit_pct_pctl": 70,
    "la_sweet_spot_pct": 29.3, "la_sweet_spot_pct_pctl": 11,
    "bat_speed": 74.4, "bat_speed_pctl": 75,
    "squared_up_pct": 22.8, "squared_up_pct_pctl": 30,
    "chase_pct": 32.0, "chase_pct_pctl": 36,
    "whiff_pct": 24.1, "whiff_pct_pctl": 51,
    "k_pct": 23.3, "k_pct_pctl": 40,
    "bb_pct": 7.6, "bb_pct_pctl": 34,
    "sprint_speed": 28.2, "sprint_speed_pctl": 75,
}

HENDERSON_SEASONS = [
    dict(season=2022, age=21, pitches=539, batted_balls=82, barrels=8, barrel_pct=9.8,
         barrel_per_pa=6.1, exit_velo=92.4, max_ev=111.1, launch_angle=2.0, la_sweet_spot_pct=25.6,
         xba=.247, xslg=.442, woba=.343, xwoba=.339, xwobacon=.416, hard_hit_pct=53.7, k_pct=25.8, bb_pct=12.1),
    dict(season=2023, age=22, pitches=2405, batted_balls=404, barrels=46, barrel_pct=11.4,
         barrel_per_pa=7.4, exit_velo=92.0, max_ev=113.8, launch_angle=11.4, la_sweet_spot_pct=32.9,
         xba=.257, xslg=.479, woba=.346, xwoba=.347, xwobacon=.433, hard_hit_pct=52.0, k_pct=25.6, bb_pct=9.0),
    dict(season=2024, age=23, pitches=2896, batted_balls=475, barrels=53, barrel_pct=11.2,
         barrel_per_pa=7.4, exit_velo=92.8, max_ev=113.1, launch_angle=9.2, la_sweet_spot_pct=34.5,
         xba=.279, xslg=.499, woba=.381, xwoba=.375, xwobacon=.444, hard_hit_pct=53.9, k_pct=22.1, bb_pct=10.8),
    dict(season=2025, age=24, pitches=2506, batted_balls=445, barrels=38, barrel_pct=8.6,
         barrel_per_pa=5.8, exit_velo=92.1, max_ev=113.9, launch_angle=9.5, la_sweet_spot_pct=29.9,
         xba=.276, xslg=.425, woba=.339, xwoba=.341, xwobacon=.396, hard_hit_pct=49.2, k_pct=21.0, bb_pct=9.5),
    dict(season=2026, age=25, pitches=1860, batted_balls=321, barrels=23, barrel_pct=7.2,
         barrel_per_pa=4.8, exit_velo=89.4, max_ev=111.9, launch_angle=11.5, la_sweet_spot_pct=29.3,
         xba=.235, xslg=.383, woba=.306, xwoba=.303, xwobacon=.355, hard_hit_pct=44.2, k_pct=23.3, bb_pct=7.6),
]

HENDERSON_CAREER = dict(
    pitches=10206, batted_balls=1727, barrels=168, barrel_pct=9.8, barrel_per_pa=6.5,
    exit_velo=91.8, max_ev=113.9, launch_angle=9.9, la_sweet_spot_pct=31.6,
    xba=.263, xslg=.451, woba=.347, xwoba=.345, xwobacon=.411, hard_hit_pct=50.4, k_pct=23.1, bb_pct=9.5,
)
