# EP Swing Intelligence

End-to-end system: SQL database, automated cleaning, predictive model,
dashboard (Streamlit + Power BI guide), and automated PDF report — all
built around the question "which swing metrics predict contact quality?",
under the EP-TSP framework (Emerson Performance).

*[Versión en español](README.md)*

## Architecture

```
data/generate_data.py   →  raw_players.csv, raw_batted_balls.csv
        │                   (simulated, calibrated against real Savant distributions)
        ▼
etl/clean.py             →  data/ep_swing_intel.db   (SQLite)
        │                   validates nulls, ranges, duplicates
        │                   aggregates into player_season_summary
        ▼
model/train_model.py     →  model/xwoba_model.pkl, barrel_model.pkl
        │                   XGBoost (xwOBA) + Random Forest (Barrel%)
        │                   writes model_predictions back to the DB
        ▼
   ┌────┴─────┐
   ▼          ▼
app/app.py   report/generate_report.py    powerbi/ (CSVs + DAX guide)
(Streamlit)   (automated PDF)             (for Power BI Desktop)
```

## How to run it

```bash
pip install -r requirements.txt

python3 data/generate_data.py     # generates raw data (with intentional errors)
python3 etl/clean.py              # cleans and loads into SQLite
python3 model/train_model.py      # trains and saves the models
python3 report/generate_report.py # generates the PDF
streamlit run app/app.py          # launches the interactive dashboard
```

## The 6 required components

| Component | Where | Notes |
|---|---|---|
| SQL database | `sql/schema.sql`, `data/ep_swing_intel.db` | SQLite, portable to Postgres (notes at the end of the schema) |
| Automated cleaning in Python | `etl/clean.py` | Nulls, impossible ranges, duplicates — with a data quality report |
| Power BI dashboard | `powerbi/` | Clean CSVs + documented DAX measures (couldn't generate the .pbix from this environment — see `POWERBI_SETUP.md`) |
| Predictive model in Python | `model/train_model.py` (simulated) / `model/train_real_model.py` (real) | Simulated: XGBoost (xwOBA, R²=0.81) + Random Forest (Barrel%, R²=0.77), 4 features, thousands of rows. Real: linear regression + LOO-CV, 2 features, n=43, R²=0.27 (xwOBA) / 0.51 (Barrel%) — see "About the data" section |
| Web application (Streamlit) | `app/app.py` | Dashboard + per-player view + live "what-if" simulator |
| Automated PDF report | `report/generate_report.py` | HTML→PDF via WeasyPrint, 100% generated from the DB and the model, no manual editing |

## About the data

**Update (chapter 5): the real 4-feature model, with official Savant targets.**

This is the milestone the project had been building toward since chapter 2.
Merging four public Savant downloads by `player_id` (not by name, to avoid
the Jr./accent mismatches from earlier chapters):

- `data/real_sample/bat_tracking_leaders_2026.csv` → `avg_bat_speed`, `squared_up_per_swing`, `swing_length`
- `data/real_sample/bat_tracking_swing_path_2026.csv` → `attack_angle` (the 4th variable that had been missing since chapter 2)
- `data/real_sample/expected_stats_2026.csv` → `est_woba` (Savant's **official xwOBA**, not our own approximation)
- `data/real_sample/exit_velocity_2026.csv` → `brl_percent` (official Barrel%)

Results, across the 205 players present in all four sources:

| Chapter | n | Features | Target | R² |
|---|---|---|---|---|
| 2 | 43 | 2 (bat_speed, squared_up%) | our own xwOBA | 0.27 |
| 3 | 33 | 3 (+ real swing_length) | our own xwOBA | 0.38 |
| 4 | 205 | 3 | real run_value (Savant) | 0.13 |
| **5** | **205** | **4 (bat_speed, squared_up%, swing_length, attack_angle)** | **OFFICIAL xwOBA (Savant)** | **0.42** |
| 5 | 205 | 4 | OFFICIAL Barrel% (Savant) | **0.63** |
| — | thousands (simulated) | 4 | xwOBA (simulated) | 0.81 |

This is the real model most comparable to the original simulated one: same
4 features, full qualified population (not curated by us), official Savant
target instead of an approximation. R²=0.42-0.63 using only swing-mechanics
variables is a credible, defensible result in front of a technical
audience — the simulated result (0.81) remains a reference point, not a
fair comparison.

**Correction (post-chapter 5):** the original version of this finding
claimed `squared_up_per_swing` outweighed `avg_bat_speed` on both targets.
That was a scaling bug, not a real finding: `train_and_eval()` fit
`LinearRegression` on the features in their native units (mph for
bat_speed, a 0-1 proportion for squared_up_per_swing) without standardizing
first, so the raw coefficients were not comparable — squared_up_per_swing's
coefficient came out numerically larger only because its scale is ~65x
smaller than bat_speed's, not because it mattered more.

With features standardized (z-scored) before fitting -- which is what
"standardized coefficients" should mean -- the result flips: **`avg_bat_speed`
has the larger coefficient on both targets** (xwOBA: 0.032 vs. 0.021;
Barrel%: 3.45 vs. 0.49). The model's R² did not change (0.42 / 0.63 -- the
predictions were always correct, only the coefficient interpretation was
wrong).

What does still hold, and replicates in an external sample of 177 MLB
hitters: `avg_bat_speed` and `squared_up_per_swing` are negatively
correlated with each other (r≈-0.65, the power/contact trade-off), which
produces a suppression effect -- squared_up_per_swing's raw correlation
with xwOBA is close to zero (r=0.07, n.s.), but its standardized
coefficient, once you control for bat_speed, is substantial (about 40% of
the two features' combined effect). In short: squared_up_per_swing does
matter -- just less than bat_speed, not more, and only visible once you
control for the trade-off rather than in the simple correlation.

Run `python3 model/train_full_4feature_model.py` to reproduce everything,
including `data/real_sample/merged_4feature_dataset_2026.csv`, the combined
dataset of 205 players with all 4 variables plus both official targets.

---

**Update (chapter 4): full population vs. curated sample.**

Using the complete bat-tracking leaderboard (n=205, no player selection on
our part) and Savant's real `batter_run_value` (instead of our xwOBA
approximation) as the target, R² drops to 0.13 — both in the 33-player
curated sample (R²=0.15) and across the full 205 (R²=0.13). The drop **is
not about sample size** — it's about the metric change: xwOBA is
mechanically tied to contact (exit velo + launch angle), while real
offensive value includes plate discipline, count sequencing, and more —
things swing mechanics alone don't explain. See
`model/train_full_leaderboard_model.py`.

---

**Update (chapter 3): real swing_length unlocked, R² actually rises.**

After chapter 2 (43 players, only 2 features, ceiling at R²=0.27-0.34), we
obtained real `avg_swing_length` for 33 of those 43 players from Savant's
public leaderboard ("Statcast Bat Tracking Leaders," CSV download, top 200
hitters by swing volume, 2026) — `data/real_sample/bat_tracking_leaders_2026.csv`.
`attack_angle` was still not available in that download (it appears as a
chart axis but not in the exportable CSV), so it stayed out of the model —
not fabricated.

Result, running the 3-feature model on the 33 players who do have real
swing_length:

| Model | n | R² xwOBA | R² Barrel% |
|---|---|---|---|
| 2 features (bat_speed, squared_up_pct) | 43 | 0.27 | 0.51 |
| **3 features (+ real swing_length)** | **33** | **0.38** | **0.61** |

This confirms the chapter 2 hypothesis: **the missing variable, not sample
size, was the model's ceiling.** Swing_length adds more signal than 12
additional players.

Run `python3 data/build_real_summary.py && python3 model/train_real_model.py`
to reproduce both models (2 and 3 features) in the same run.

---

**Update (chapter 2): 43 real players, real model trained, honest results.**

I replaced the "single player" phase with a real dataset of 43 2026 MLB
players, hand-transcribed from Baseball Savant screenshots (percentile
rankings + Statcast Batting Statistics). The whole process lives in
`data/real_sample/` (one `*_savant_2026.py` file per player) and
`data/real_data_validation.py` runs the full validation.

From that registry, `data/build_real_summary.py` builds
`data/real_player_season_summary.csv` — and here's the honest limitation
worth stating up front: **Baseball Savant only publishes 2 of the 4 swing
variables the simulated model uses**. `bat_speed` and `squared_up_pct` are
on the public percentile page; `attack_angle` and `swing_length` live on
the bat-tracking leaderboard, which this project hadn't scraped yet.
Rather than invent them, `model/train_real_model.py` trains a real
**2-feature-only** model, using linear regression + leave-one-out
cross-validation (the right call at this sample size — Random
Forest/XGBoost would overfit at n=43).

Results, unvarnished:

| n players | R² xwOBA | R² Barrel% |
|---|---|---|
| 31 | 0.16 | 0.57 |
| 35 | 0.29 | 0.51 |
| 40 | 0.34 | 0.51 |
| 43 | 0.27 | 0.51 |

xwOBA's R² **rose with extreme profiles** (Ohtani, Olson, Ozuna, Devers —
power/contact at the edges of the distribution) and **fell when adding
players who don't follow the simple linear relationship** (Contreras and
Betts have high-quality contact with moderate bat speed; Perez's 2026 is a
real age-decline season that bat_speed/squared_up_pct don't explain). This
isn't noise to hide — it's the signal that **more players alone doesn't
break the model's ceiling; the 2 missing features do** (attack_angle,
swing_length), via `pybaseball` on a machine with internet access
(`data/fetch_real_data.py`) or Savant's bat-tracking leaderboard.

Run `python3 data/build_real_summary.py && python3 model/train_real_model.py`
to reproduce these numbers.

**What this is NOT**: a replacement for the simulated 4-feature model
(R²=0.81, thousands of rows). It's a different, smaller, 100% real model,
honest about its limits — which is exactly what's needed to present it
without it falling apart in front of someone technical.

---

### Earlier history (chapter 1, a single player)

**This sandbox has no access to baseballsavant.mlb.com or Kaggle** — I
confirmed this directly (`curl` returns `403: Host not in allowlist`). I
gathered real data from three sources:

- **`data/real_sample/judge.csv`, `stanton.csv`**: real full seasons
  (2015-2017) from a GitHub repo — official EV, Launch Angle, and xwOBA.
  ⚠️ Bug I found and fixed: my first calculation mixed foul balls (which
  also carry a recorded `launch_speed`) in with real balls in play, which
  dragged Judge's average EV down to 85.4 mph — well below his real figure
  (~95 mph). Filtering by `type=='X'` (balls in play only, the same
  definition Savant uses) the corrected average is 94.6 mph, consistent
  with official data.
- **`data/real_sample/judge_savant_2026.py`**: 11 real Judge seasons
  (2016-2026) hand-transcribed from screenshots taken directly in the
  Savant app — includes his real Bat Speed (76.1 mph, 92nd percentile) and
  real Squared-Up% (21.9%, 24th percentile) for 2026.
- This also helped catch that my simulated Sweet-Spot% was inflated (50%
  simulated vs. 29-38% real).

The simulated data (still used by the original SQL/XGBoost pipeline)
remains calibrated against real reference points:

- Bat speed: distribution centered around ~70.5 mph, calibrated so the max
  approaches 79.9 mph (real data point: 100th percentile on Baseball
  Savant, 2026 season).
- Barrel%: a classifier replicating the public shape of Statcast's real
  criterion (a launch-angle window that widens above 98 mph EV).
- Average exit velocity calibrated to ~88.5 mph (real MLB average).
- xwOBA is a **simplified approximation** (not MLB's proprietary model),
  labeled as such in every table, chart, and report where it appears.

### To use complete real data (with bat-tracking)

On a machine with normal internet access (not this sandbox):

```bash
pip install pybaseball
python3 data/fetch_real_data.py
```

That script pulls real 2024-2025 Statcast + Bat Tracking data via
`pybaseball.statcast()`, and writes `raw_players.csv`/`raw_batted_balls.csv`
in the exact format `etl/clean.py` expects — the rest of the pipeline (SQL,
model, Streamlit, PDF, Power BI) runs without touching a line. This is what
would resolve the attack_angle/swing_length limitation mentioned above.

## For the portfolio

This project demonstrates: relational database modeling, ETL engineering
with data quality validation, domain-informed feature engineering (swing
biomechanics), predictive modeling with honest evaluation (R², MAE,
feature importance), an interactive web application, and automated report
generation — the full cycle of a data product, not just an exploratory
analysis notebook.
