"""
data/real_sample/judge_savant_2026.py
---------------------------------------
Real Baseball Savant data for Aaron Judge, transcribed by hand from
screenshots the user captured directly from the Savant app (since this
sandbox cannot reach baseballsavant.mlb.com itself). Two real, official
sources merged here:

  1. 2026 MLB Percentile Rankings snapshot — includes real Bat Speed and
     Squared-Up%, which is the bat-tracking data this project otherwise
     can't obtain in bulk.
  2. Statcast Batting Statistics by season (2016-2026) — real EV, Barrel%,
     xBA/xSLG/wOBA/xwOBA, Hard-Hit%, K%, BB%.

Everything in this file is REAL, official MLB data — not simulated, not
approximated. The one limitation: the year-by-year table does not break out
bat_speed/squared_up_pct per season, only the current 2026 percentile
snapshot does — so we have 11 real seasons of outcome data, but only one
real season of swing-mechanics data, for this one player.
"""

# 2026 season percentile snapshot (includes real bat-tracking metrics)
JUDGE_2026_SNAPSHOT = {
    "player_name": "Aaron Judge",
    "season": 2026,
    "batting_run_value": 19, "batting_run_value_pctl": 93,
    "xwoba": 0.415, "xwoba_pctl": 99,
    "xba": 0.270, "xba_pctl": 79,
    "xslg": 0.600, "xslg_pctl": 100,
    "avg_exit_velo": 94.1, "avg_exit_velo_pctl": 98,
    "barrel_pct": 21.7, "barrel_pct_pctl": 100,
    "hard_hit_pct": 57.3, "hard_hit_pct_pctl": 98,
    "la_sweet_spot_pct": 33.6, "la_sweet_spot_pct_pctl": 42,
    "bat_speed": 76.1, "bat_speed_pctl": 92,
    "squared_up_pct": 21.9, "squared_up_pct_pctl": 24,
    "chase_pct": 25.8, "chase_pct_pctl": 73,
    "whiff_pct": 32.2, "whiff_pct_pctl": 11,
    "k_pct": 27.6, "k_pct_pctl": 16,
    "bb_pct": 16.1, "bb_pct_pctl": 98,
    "sprint_speed": 26.7, "sprint_speed_pctl": 32,
}

# Statcast Batting Statistics by season, 2016-2026 (real, from Savant player page)
JUDGE_SEASONS = [
    # season, age, pitches, batted_balls, barrels, barrel_pct, barrel_per_pa,
    # exit_velo, max_ev, launch_angle, la_sweet_spot_pct, xba, xslg, woba,
    # xwoba, xwobacon, hard_hit_pct, k_pct, bb_pct
    dict(season=2016, age=24, pitches=408, batted_balls=43, barrels=5, barrel_pct=11.9,
         barrel_per_pa=5.3, exit_velo=95.1, max_ev=115.2, launch_angle=20.6, la_sweet_spot_pct=32.6,
         xba=.184, xslg=.366, woba=.267, xwoba=.281, xwobacon=.460, hard_hit_pct=58.1, k_pct=44.2, bb_pct=9.5),
    dict(season=2017, age=25, pitches=2989, batted_balls=338, barrels=87, barrel_pct=27.6,
         barrel_per_pa=12.8, exit_velo=95.0, max_ev=121.1, launch_angle=15.8, la_sweet_spot_pct=38.2,
         xba=.287, xslg=.668, woba=.430, xwoba=.450, xwobacon=.641, hard_hit_pct=54.7, k_pct=30.7, bb_pct=18.7),
    dict(season=2018, age=26, pitches=2124, batted_balls=266, barrels=43, barrel_pct=16.6,
         barrel_per_pa=8.6, exit_velo=94.7, max_ev=119.9, launch_angle=12.4, la_sweet_spot_pct=35.7,
         xba=.273, xslg=.527, woba=.391, xwoba=.393, xwobacon=.532, hard_hit_pct=54.1, k_pct=30.5, bb_pct=15.3),
    dict(season=2019, age=27, pitches=1914, batted_balls=238, barrels=48, barrel_pct=21.2,
         barrel_per_pa=10.7, exit_velo=96.0, max_ev=118.1, launch_angle=11.6, la_sweet_spot_pct=40.3,
         xba=.278, xslg=.582, woba=.382, xwoba=.402, xwobacon=.563, hard_hit_pct=58.4, k_pct=31.5, bb_pct=14.3),
    dict(season=2020, age=28, pitches=487, batted_balls=69, barrels=8, barrel_pct=11.9,
         barrel_per_pa=7.0, exit_velo=92.2, max_ev=113.1, launch_angle=15.7, la_sweet_spot_pct=36.2,
         xba=.265, xslg=.545, woba=.375, xwoba=.378, xwobacon=.500, hard_hit_pct=40.6, k_pct=28.1, bb_pct=8.8),
    dict(season=2021, age=29, pitches=2654, batted_balls=397, barrels=70, barrel_pct=17.8,
         barrel_per_pa=11.1, exit_velo=95.8, max_ev=119.0, launch_angle=11.6, la_sweet_spot_pct=38.5,
         xba=.302, xslg=.601, woba=.387, xwoba=.418, xwobacon=.532, hard_hit_pct=58.4, k_pct=25.0, bb_pct=11.8),
    dict(season=2022, age=30, pitches=2906, batted_balls=400, barrels=106, barrel_pct=26.6,
         barrel_per_pa=15.2, exit_velo=95.9, max_ev=118.4, launch_angle=15.0, la_sweet_spot_pct=39.0,
         xba=.304, xslg=.732, woba=.458, xwoba=.468, xwobacon=.619, hard_hit_pct=61.9, k_pct=25.1, bb_pct=15.9),
    dict(season=2023, age=31, pitches=1901, batted_balls=240, barrels=66, barrel_pct=27.6,
         barrel_per_pa=14.4, exit_velo=97.6, max_ev=116.9, launch_angle=20.4, la_sweet_spot_pct=37.1,
         xba=.286, xslg=.729, woba=.420, xwoba=.466, xwobacon=.643, hard_hit_pct=64.2, k_pct=28.4, bb_pct=19.2),
    dict(season=2024, age=32, pitches=2885, batted_balls=390, barrels=105, barrel_pct=27.1,
         barrel_per_pa=14.9, exit_velo=96.2, max_ev=117.5, launch_angle=19.0, la_sweet_spot_pct=40.8,
         xba=.304, xslg=.739, woba=.476, xwoba=.480, xwobacon=.625, hard_hit_pct=61.0, k_pct=24.3, bb_pct=18.9),
    dict(season=2025, age=33, pitches=2631, batted_balls=388, barrels=96, barrel_pct=24.8,
         barrel_per_pa=14.1, exit_velo=95.4, max_ev=118.1, launch_angle=19.0, la_sweet_spot_pct=39.4,
         xba=.300, xslg=.708, woba=.463, xwoba=.460, xwobacon=.592, hard_hit_pct=58.2, k_pct=23.6, bb_pct=18.3),
    dict(season=2026, age=34, pitches=1114, batted_balls=143, barrels=31, barrel_pct=21.7,
         barrel_per_pa=11.9, exit_velo=94.1, max_ev=116.2, launch_angle=14.6, la_sweet_spot_pct=33.6,
         xba=.270, xslg=.600, woba=.385, xwoba=.415, xwobacon=.546, hard_hit_pct=57.3, k_pct=27.6, bb_pct=16.1),
]

JUDGE_CAREER = dict(
    pitches=22013, batted_balls=2912, barrels=665, barrel_pct=23.3, barrel_per_pa=12.6,
    exit_velo=95.6, max_ev=121.1, launch_angle=15.7, la_sweet_spot_pct=38.4,
    xba=.289, xslg=.654, woba=.423, xwoba=.439, xwobacon=.588, hard_hit_pct=58.4, k_pct=27.4, bb_pct=16.3,
)

MLB_LEAGUE_AVG_REFERENCE = dict(
    barrel_pct=7.6, barrel_per_pa=4.9, exit_velo=88.6, max_ev=122.9, launch_angle=12.5,
    la_sweet_spot_pct=33.3, xba=.243, xslg=.407, woba=.316, xwoba=.316, xwobacon=.369,
    hard_hit_pct=37.1, k_pct=22.2, bb_pct=8.4,
)
