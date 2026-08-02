"""
data/real_sample/wood_savant_2026.py
----------------------------------------
Real Baseball Savant data for James Wood, transcribed by hand from
screenshots the user captured directly from the Savant app. The fourth
and final EP-TSP case-study player (swing-plane matching analysis using
Cade Cavin's framework, three seasons of Statcast data). The strongest
pure damage profile in the entire 19-player roster to date: Avg Exit
Velo, Barrel%, and Hard-Hit% all at the 100th percentile, alongside a
genuine swing-and-miss cost (Whiff% 16th, K% 12th) -- textbook
power-for-contact tradeoff at its most extreme.
"""

WOOD_2026_SNAPSHOT = {
    "player_name": "James Wood",
    "season": 2026,
    "batting_run_value": 27, "batting_run_value_pctl": 97,
    "xwoba": 0.420, "xwoba_pctl": 99,
    "xba": 0.275, "xba_pctl": 85,
    "xslg": 0.592, "xslg_pctl": 99,
    "avg_exit_velo": 95.1, "avg_exit_velo_pctl": 100,
    "barrel_pct": 21.7, "barrel_pct_pctl": 100,
    "hard_hit_pct": 58.6, "hard_hit_pct_pctl": 100,
    "la_sweet_spot_pct": 40.7, "la_sweet_spot_pct_pctl": 96,
    "bat_speed": 76.8, "bat_speed_pctl": 95,
    "squared_up_pct": 24.2, "squared_up_pct_pctl": 43,
    "chase_pct": 22.4, "chase_pct_pctl": 91,
    "whiff_pct": 31.1, "whiff_pct_pctl": 16,
    "k_pct": 29.4, "k_pct_pctl": 12,
    "bb_pct": 16.4, "bb_pct_pctl": 98,
    "sprint_speed": 27.4, "sprint_speed_pctl": 51,
}

WOOD_SEASONS = [
    dict(season=2024, age=21, pitches=1404, batted_balls=198, barrels=21, barrel_pct=10.7,
         barrel_per_pa=6.3, exit_velo=92.8, max_ev=111.6, launch_angle=2.4, la_sweet_spot_pct=31.3,
         xba=.265, xslg=.449, woba=.342, xwoba=.354, xwobacon=.461, hard_hit_pct=52.0, k_pct=28.9, bb_pct=11.6),
    dict(season=2025, age=22, pitches=2887, batted_balls=380, barrels=62, barrel_pct=16.4,
         barrel_per_pa=9.0, exit_velo=94.3, max_ev=118.0, launch_angle=6.3, la_sweet_spot_pct=36.3,
         xba=.259, xslg=.493, woba=.353, xwoba=.361, xwobacon=.502, hard_hit_pct=56.3, k_pct=32.1, bb_pct=12.3),
    dict(season=2026, age=23, pitches=2065, batted_balls=263, barrels=57, barrel_pct=21.7,
         barrel_per_pa=11.6, exit_velo=95.1, max_ev=116.3, launch_angle=9.9, la_sweet_spot_pct=40.7,
         xba=.275, xslg=.592, woba=.398, xwoba=.420, xwobacon=.570, hard_hit_pct=58.6, k_pct=29.4, bb_pct=16.4),
]

WOOD_CAREER = dict(
    pitches=6356, batted_balls=841, barrels=140, barrel_pct=16.7, barrel_per_pa=9.2,
    exit_velo=94.2, max_ev=118.0, launch_angle=6.5, la_sweet_spot_pct=36.5,
    xba=.265, xslg=.514, woba=.365, xwoba=.378, xwobacon=.513, hard_hit_pct=56.0, k_pct=30.5, bb_pct=13.5,
)
