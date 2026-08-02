-- ============================================================================
-- EP Swing Intelligence — SQL Schema
-- SQLite (portable to Postgres/MySQL with minor type adjustments — noted inline)
-- ============================================================================

DROP TABLE IF EXISTS batted_balls;
DROP TABLE IF EXISTS player_season_summary;
DROP TABLE IF EXISTS model_predictions;
DROP TABLE IF EXISTS players;

-- ----------------------------------------------------------------------------
-- Dimension: players
-- ----------------------------------------------------------------------------
CREATE TABLE players (
    player_id     INTEGER PRIMARY KEY,
    player_name   TEXT NOT NULL,
    team          TEXT NOT NULL,
    position      TEXT NOT NULL,
    bats          TEXT CHECK (bats IN ('R','L','S')) NOT NULL
);

-- ----------------------------------------------------------------------------
-- Fact table: batted_balls (grain: one row per batted-ball event)
-- ----------------------------------------------------------------------------
CREATE TABLE batted_balls (
    bb_id           INTEGER PRIMARY KEY,
    player_id       INTEGER NOT NULL REFERENCES players(player_id),
    bat_speed       REAL NOT NULL CHECK (bat_speed > 0),
    attack_angle    REAL NOT NULL,
    squared_up_pct  REAL NOT NULL CHECK (squared_up_pct BETWEEN 0 AND 100),
    swing_length    REAL NOT NULL CHECK (swing_length > 0),
    pitch_speed     REAL NOT NULL,
    exit_velocity   REAL NOT NULL CHECK (exit_velocity > 0),
    launch_angle    REAL NOT NULL,
    is_barrel       INTEGER NOT NULL CHECK (is_barrel IN (0,1)),
    is_hard_hit     INTEGER NOT NULL CHECK (is_hard_hit IN (0,1)),
    is_sweet_spot   INTEGER NOT NULL CHECK (is_sweet_spot IN (0,1)),
    xwoba_est       REAL NOT NULL CHECK (xwoba_est BETWEEN 0 AND 2.5)
);

CREATE INDEX idx_batted_balls_player ON batted_balls(player_id);

-- ----------------------------------------------------------------------------
-- Derived: player_season_summary (grain: one row per player)
-- This is the table the predictive model and the dashboards read from.
-- Populated by etl/clean.py after aggregating batted_balls.
-- ----------------------------------------------------------------------------
CREATE TABLE player_season_summary (
    player_id           INTEGER PRIMARY KEY REFERENCES players(player_id),
    n_bbe                INTEGER NOT NULL,
    avg_bat_speed        REAL NOT NULL,
    avg_attack_angle     REAL NOT NULL,
    avg_squared_up_pct   REAL NOT NULL,
    avg_swing_length     REAL NOT NULL,
    avg_exit_velocity    REAL NOT NULL,
    barrel_pct           REAL NOT NULL,
    hard_hit_pct         REAL NOT NULL,
    sweet_spot_pct       REAL NOT NULL,
    avg_xwoba_est         REAL NOT NULL
);

-- ----------------------------------------------------------------------------
-- Model output: predictions written by model/train_model.py
-- ----------------------------------------------------------------------------
CREATE TABLE model_predictions (
    player_id           INTEGER PRIMARY KEY REFERENCES players(player_id),
    predicted_xwoba      REAL NOT NULL,
    actual_xwoba          REAL NOT NULL,
    residual              REAL NOT NULL,
    predicted_barrel_pct REAL NOT NULL,
    actual_barrel_pct     REAL NOT NULL,
    model_version         TEXT NOT NULL,
    scored_at              TEXT NOT NULL
);

-- Postgres notes:
--   INTEGER PRIMARY KEY -> SERIAL PRIMARY KEY / GENERATED ALWAYS AS IDENTITY
--   TEXT                -> VARCHAR / TEXT (same)
--   REAL                -> DOUBLE PRECISION
--   CHECK (x IN (0,1))  -> works identically, or use BOOLEAN with TRUE/FALSE
