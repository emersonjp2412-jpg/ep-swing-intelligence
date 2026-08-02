"""
data/real_sample/stanton_savant_2026.py
------------------------------------------
Real Baseball Savant data for Giancarlo Stanton, transcribed by hand from
screenshots the user captured directly from the Savant app. Same two sources
as judge_savant_2026.py:

  1. 2026 MLB Percentile Rankings snapshot — real Bat Speed (79.3 mph) and
     Squared-Up% (19.4%). Percentile digits weren't legible/shown for most
     rows in this particular screenshot (his 2026 Batting Run Value shows
     "NOT QUALIFIED" — limited PA this season), so raw values are stored
     without percentile ranks here, unlike Judge's snapshot.
  2. Statcast Batting Statistics by season (2015-2026) — real EV, Barrel%,
     xBA/xSLG/wOBA/xwOBA/xwOBAcon, Hard-Hit%, K%, BB%.
"""

STANTON_2026_SNAPSHOT = {
    "player_name": "Giancarlo Stanton",
    "season": 2026,
    "xwoba": 0.326,
    "xba": 0.245,
    "xslg": 0.466,
    "avg_exit_velo": 94.1,
    "barrel_pct": 18.0,
    "hard_hit_pct": 44.3,
    "la_sweet_spot_pct": 37.7,
    "bat_speed": 79.3,
    "squared_up_pct": 19.4,
    "chase_pct": 30.3,
    "whiff_pct": 38.7,
    "k_pct": 30.2,
    "bb_pct": 6.3,
    "note": "Batting Run Value: NOT QUALIFIED (temporada 2026 con pocas PA); percentiles no legibles en la captura.",
}

STANTON_SEASONS = [
    dict(season=2015, age=25, pitches=1221, batted_balls=187, barrels=45, barrel_pct=28.7,
         barrel_per_pa=14.2, exit_velo=96.1, max_ev=120.3, launch_angle=15.7, la_sweet_spot_pct=28.9,
         xba=.275, xslg=.611, woba=.394, xwoba=.409, xwobacon=.574, hard_hit_pct=52.9, k_pct=29.9, bb_pct=10.7),
    dict(season=2016, age=26, pitches=1892, batted_balls=275, barrels=43, barrel_pct=17.5,
         barrel_per_pa=9.2, exit_velo=93.9, max_ev=120.1, launch_angle=13.9, la_sweet_spot_pct=29.5,
         xba=.235, xslg=.483, woba=.344, xwoba=.341, xwobacon=.454, hard_hit_pct=47.6, k_pct=29.9, bb_pct=10.7),
    dict(season=2017, age=27, pitches=2736, batted_balls=437, barrels=76, barrel_pct=19.9,
         barrel_per_pa=11.0, exit_velo=92.0, max_ev=122.2, launch_angle=11.2, la_sweet_spot_pct=31.6,
         xba=.273, xslg=.595, woba=.410, xwoba=.400, xwobacon=.496, hard_hit_pct=45.6, k_pct=23.6, bb_pct=12.3),
    dict(season=2018, age=28, pitches=2942, batted_balls=416, barrels=63, barrel_pct=16.5,
         barrel_per_pa=8.9, exit_velo=93.7, max_ev=121.7, launch_angle=11.7, la_sweet_spot_pct=30.0,
         xba=.237, xslg=.473, woba=.360, xwoba=.342, xwobacon=.455, hard_hit_pct=50.8, k_pct=29.9, bb_pct=9.9),
    dict(season=2019, age=29, pitches=315, batted_balls=36, barrels=9, barrel_pct=28.1,
         barrel_per_pa=12.5, exit_velo=92.7, max_ev=120.6, launch_angle=7.9, la_sweet_spot_pct=36.1,
         xba=.263, xslg=.515, woba=.379, xwoba=.393, xwobacon=.555, hard_hit_pct=47.2, k_pct=33.3, bb_pct=16.7),
    dict(season=2020, age=30, pitches=415, batted_balls=49, barrels=9, barrel_pct=18.4,
         barrel_per_pa=9.6, exit_velo=91.1, max_ev=121.3, launch_angle=8.3, la_sweet_spot_pct=38.8,
         xba=.290, xslg=.534, woba=.379, xwoba=.409, xwobacon=.539, hard_hit_pct=51.0, k_pct=28.7, bb_pct=16.0),
    dict(season=2021, age=31, pitches=2426, batted_balls=356, barrels=56, barrel_pct=15.9,
         barrel_per_pa=9.7, exit_velo=95.1, max_ev=122.2, launch_angle=10.3, la_sweet_spot_pct=32.6,
         xba=.254, xslg=.502, woba=.370, xwoba=.361, xwobacon=.461, hard_hit_pct=56.3, k_pct=27.1, bb_pct=10.9),
    dict(season=2022, age=32, pitches=1841, batted_balls=264, barrels=51, barrel_pct=19.4,
         barrel_per_pa=11.3, exit_velo=95.0, max_ev=119.8, launch_angle=10.8, la_sweet_spot_pct=26.9,
         xba=.236, xslg=.487, woba=.327, xwoba=.350, xwobacon=.471, hard_hit_pct=52.3, k_pct=30.3, bb_pct=11.1),
    dict(season=2023, age=33, pitches=1719, batted_balls=248, barrels=39, barrel_pct=15.8,
         barrel_per_pa=9.4, exit_velo=93.3, max_ev=119.5, launch_angle=12.5, la_sweet_spot_pct=27.4,
         xba=.212, xslg=.470, woba=.297, xwoba=.326, xwobacon=.429, hard_hit_pct=48.4, k_pct=29.9, bb_pct=9.9),
    dict(season=2024, age=34, pitches=1831, batted_balls=276, barrels=57, barrel_pct=20.9,
         barrel_per_pa=12.4, exit_velo=94.6, max_ev=120.0, launch_angle=14.7, la_sweet_spot_pct=34.8,
         xba=.243, xslg=.520, woba=.330, xwoba=.354, xwobacon=.492, hard_hit_pct=55.3, k_pct=31.2, bb_pct=8.3),
    dict(season=2025, age=35, pitches=1214, batted_balls=154, barrels=34, barrel_pct=22.1,
         barrel_per_pa=12.1, exit_velo=94.4, max_ev=118.0, launch_angle=17.5, la_sweet_spot_pct=35.7,
         xba=.235, xslg=.520, woba=.395, xwoba=.354, xwobacon=.516, hard_hit_pct=55.2, k_pct=34.2, bb_pct=10.3),
    dict(season=2026, age=36, pitches=384, batted_balls=61, barrels=11, barrel_pct=18.0,
         barrel_per_pa=11.5, exit_velo=94.1, max_ev=116.3, launch_angle=21.5, la_sweet_spot_pct=37.7,
         xba=.245, xslg=.466, woba=.316, xwoba=.326, xwobacon=.444, hard_hit_pct=44.3, k_pct=30.2, bb_pct=6.3),
]

STANTON_CAREER = dict(
    pitches=18936, batted_balls=2759, barrels=493, barrel_pct=19.0, barrel_per_pa=10.6,
    exit_velo=93.9, max_ev=122.2, launch_angle=12.7, la_sweet_spot_pct=31.1,
    xba=.246, xslg=.515, woba=.359, xwoba=.361, xwobacon=.479, hard_hit_pct=50.9, k_pct=29.1, bb_pct=10.6,
)
