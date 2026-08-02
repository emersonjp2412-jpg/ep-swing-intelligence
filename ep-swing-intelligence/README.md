# EP Swing Intelligence

*[English version](README_EN.md)*

Sistema de punta a punta: base de datos SQL, limpieza automática, modelo
predictivo, dashboard (Streamlit + guía Power BI) y reporte PDF automático —
todo sobre la pregunta "¿qué métricas de swing predicen la calidad de
contacto?", en el dominio de EP-TSP (Emerson Performance).

## Arquitectura

```
data/generate_data.py   →  raw_players.csv, raw_batted_balls.csv
        │                   (simulado, calibrado contra distribuciones reales de Savant)
        ▼
etl/clean.py             →  data/ep_swing_intel.db   (SQLite)
        │                   valida nulos, rangos, duplicados
        │                   agrega a player_season_summary
        ▼
model/train_model.py     →  model/xwoba_model.pkl, barrel_model.pkl
        │                   XGBoost (xwOBA) + Random Forest (Barrel%)
        │                   escribe model_predictions de vuelta a la DB
        ▼
   ┌────┴─────┐
   ▼          ▼
app/app.py   report/generate_report.py    powerbi/ (CSVs + guía DAX)
(Streamlit)   (PDF automático)             (para Power BI Desktop)
```

## Cómo correrlo

```bash
pip install -r requirements.txt

python3 data/generate_data.py     # genera datos crudos (con errores intencionales)
python3 etl/clean.py              # limpia y carga a SQLite
python3 model/train_model.py      # entrena y guarda los modelos
python3 report/generate_report.py # genera el PDF
streamlit run app/app.py          # levanta el dashboard interactivo
```

## Los 6 componentes pedidos

| Componente | Dónde | Notas |
|---|---|---|
| Base de datos SQL | `sql/schema.sql`, `data/ep_swing_intel.db` | SQLite, portable a Postgres (notas al final del schema) |
| Limpieza automática en Python | `etl/clean.py` | Nulos, rangos imposibles, duplicados — con reporte de calidad de datos |
| Dashboard en Power BI | `powerbi/` | CSVs limpios + medidas DAX documentadas (no pude generar el .pbix desde este entorno — ver `POWERBI_SETUP.md`) |
| Modelo predictivo en Python | `model/train_model.py` (simulado) / `model/train_real_model.py` (real) | Simulado: XGBoost (xwOBA, R²=0.81) + Random Forest (Barrel%, R²=0.77), 4 features, miles de filas. Real: regresión lineal + LOO-CV, 2 features, n=43, R²=0.27 (xwOBA) / 0.51 (Barrel%) — ver sección "Sobre los datos" |
| Aplicación web (Streamlit) | `app/app.py` | Dashboard + vista por jugador + simulador "what-if" en vivo |
| Reporte automático en PDF | `report/generate_report.py` | HTML→PDF vía WeasyPrint, 100% generado desde la DB y el modelo, sin edición manual |

## Sobre los datos

**Actualización (capítulo 5): el modelo real de 4 features, con targets oficiales de Savant.**

Este es el hito que el proyecto venía persiguiendo desde el capítulo 2.
Cruzando por `player_id` (no por nombre, para evitar los problemas de
Jr./acentos de capítulos anteriores) cuatro descargas públicas de Savant:

- `data/real_sample/bat_tracking_leaders_2026.csv` → `avg_bat_speed`, `squared_up_per_swing`, `swing_length`
- `data/real_sample/bat_tracking_swing_path_2026.csv` → `attack_angle` (la 4ª variable que faltaba desde el capítulo 2)
- `data/real_sample/expected_stats_2026.csv` → `est_woba` (el **xwOBA oficial** de Savant, no una aproximación propia)
- `data/real_sample/exit_velocity_2026.csv` → `brl_percent` (Barrel% oficial)

El resultado, sobre los 205 jugadores que aparecen en las cuatro fuentes:

| Capítulo | n | Features | Target | R² |
|---|---|---|---|---|
| 2 | 43 | 2 (bat_speed, squared_up%) | xwOBA propio | 0.27 |
| 3 | 33 | 3 (+ swing_length real) | xwOBA propio | 0.38 |
| 4 | 205 | 3 | run_value real (Savant) | 0.13 |
| **5** | **205** | **4 (bat_speed, squared_up%, swing_length, attack_angle)** | **xwOBA OFICIAL (Savant)** | **0.42** |
| 5 | 205 | 4 | Barrel% OFICIAL (Savant) | **0.63** |
| — | miles (simulado) | 4 | xwOBA (simulado) | 0.81 |

Es el modelo real más comparable al simulado original: mismas 4 features,
población completa calificada (no curada por nosotros), target oficial de
Savant en vez de una aproximación. R²=0.42-0.63 con solo variables de swing
es un resultado creíble y defendible frente a alguien técnico — el
resultado simulado (0.81) sigue siendo una referencia, no una comparación
justa.

**Hallazgo dentro del capítulo 5:** `squared_up_per_swing` pesa más que
`avg_bat_speed` en ambos targets (coeficientes estandarizados) — la calidad
de contacto explica más varianza que la fuerza bruta del swing, contrario a
la intuición de "pegarle más fuerte = mejor resultado". Ver
`report/chart_capitulo5_coeficientes.png`.

Corre `python3 model/train_full_4feature_model.py` para reproducir todo,
incluyendo `data/real_sample/merged_4feature_dataset_2026.csv`, el dataset
combinado de 205 jugadores con las 4 variables + ambos targets oficiales.

---

**Actualización (capítulo 4): población completa vs. muestra curada.**

Usando el leaderboard completo de bat-tracking (n=205, sin selección de
jugadores por nuestra parte) y el `batter_run_value` real de Savant
(en vez de nuestra aproximación de xwOBA) como target, el R² cae a 0.13 —
tanto en la muestra de 33 curados (R²=0.15) como en los 205 completos
(R²=0.13). La caída **no es por tamaño de muestra**, es por el cambio de
métrica: xwOBA está mecánicamente ligado a contacto (exit velo + launch
angle), mientras que el valor ofensivo real incluye paciencia de bateo,
secuencia de conteo y más — cosas que el swing mecánico solo no explica.
Ver `model/train_full_leaderboard_model.py`.

---

**Actualización (capítulo 3): swing_length real desbloqueado, R² sube de verdad.**

Después del capítulo 2 (43 jugadores, solo 2 features, techo en R²=0.27-0.34),
conseguimos `avg_swing_length` real para 33 de esos 43 jugadores desde el
leaderboard público de Savant ("Statcast Bat Tracking Leaders", descarga CSV,
top 200 hitters por volumen de swings, 2026) — `data/real_sample/bat_tracking_leaders_2026.csv`.
`attack_angle` sigue sin estar disponible en esa descarga (aparece como eje
del gráfico pero no en el CSV exportable), así que sigue fuera del modelo,
no fabricada.

Resultado, con el modelo de 3 features corriendo sobre los 33 jugadores que
sí tienen swing_length real:

| Modelo | n | R² xwOBA | R² Barrel% |
|---|---|---|---|
| 2 features (bat_speed, squared_up_pct) | 43 | 0.27 | 0.51 |
| **3 features (+ swing_length real)** | **33** | **0.38** | **0.61** |

Esto confirma la hipótesis del capítulo 2: **la variable que faltaba, no el
tamaño de la muestra, era el techo del modelo.** Swing_length aporta más
señal que 12 jugadores adicionales.

Corre `python3 data/build_real_summary.py && python3 model/train_real_model.py`
para reproducir ambos modelos (2 y 3 features) en la misma corrida.

---

**Actualización (capítulo 2): 43 jugadores reales, modelo real entrenado, resultados honestos.**

Reemplacé la fase de "un solo jugador" por un dataset real de 43 jugadores MLB
2026, transcritos a mano desde capturas de pantalla de Baseball Savant
(percentile rankings + Statcast Batting Statistics). Todo el proceso está en
`data/real_sample/` (un archivo `*_savant_2026.py` por jugador) y
`data/real_data_validation.py` corre la validación completa.

De ese registry, `data/build_real_summary.py` construye
`data/real_player_season_summary.csv` — y ahí está la limitación honesta que
hay que decir de entrada: **Baseball Savant solo publica 2 de las 4 variables
de swing que el modelo simulado usa**. `bat_speed` y `squared_up_pct` están en
la página pública de percentiles; `attack_angle` y `swing_length` viven en el
leaderboard de bat-tracking, que este proyecto no scrapeó. En vez de
inventarlas, `model/train_real_model.py` entrena un modelo real de **solo 2
features**, con regresión lineal + leave-one-out cross-validation (lo correcto
a este tamaño de muestra — Random Forest/XGBoost sobreajustarían con n=43).

Resultado, sin maquillar:

| n jugadores | R² xwOBA | R² Barrel% |
|---|---|---|
| 31 | 0.16 | 0.57 |
| 35 | 0.29 | 0.51 |
| 40 | 0.34 | 0.51 |
| 43 | 0.27 | 0.51 |

El R² de xwOBA **subió con perfiles extremos** (Ohtani, Olson, Ozuna, Devers —
poder/contacto en los bordes de la distribución) y **bajó al agregar jugadores
que no siguen la relación lineal simple** (Contreras y Betts tienen contacto de
alta calidad con bat speed moderado; Perez 2026 es una temporada de declive
real por edad que bat_speed/squared_up_pct no explican). Esto no es ruido a
esconder — es la señal de que **más jugadores por sí solo no rompe el techo
del modelo; hacen falta las 2 features que faltan** (attack_angle,
swing_length), vía `pybaseball` en una máquina con acceso a internet
(`data/fetch_real_data.py`) o el leaderboard de bat-tracking de Savant.

Corre `python3 data/build_real_summary.py && python3 model/train_real_model.py`
para reproducir estos números.

**Lo que NO es esto**: un reemplazo del modelo simulado de 4 features
(R²=0.81, miles de filas). Es un modelo distinto, más chico, 100% real, y
honesto sobre sus límites — que es justo lo que hace falta para presentarlo
sin que se caiga ante alguien técnico.

---

### Historia previa (capítulo 1, un solo jugador)

**Este sandbox no tiene acceso a baseballsavant.mlb.com ni a Kaggle** — lo confirmé
directamente (`curl` devuelve `403: Host not in allowlist`). Reuní datos reales
de tres fuentes:

- **`data/real_sample/judge.csv`, `stanton.csv`**: temporadas completas reales
  (2015-2017) desde un repo de GitHub — EV, Launch Angle y xwOBA oficiales.
  ⚠️ Bug que encontré y corregí: mi primer cálculo incluía foul balls (también
  traen `launch_speed` registrado) mezclados con bolas en juego reales, lo que
  bajaba el promedio de EV de Judge a 85.4 mph — muy por debajo de su cifra
  real (~95 mph). Filtrando por `type=='X'` (solo bolas puestas en juego,
  la misma definición que usa Savant) el promedio corregido es 94.6 mph,
  consistente con los datos oficiales.
- **`data/real_sample/judge_savant_2026.py`**: 11 temporadas reales de Judge
  (2016-2026) transcritas a mano de capturas de pantalla que tomaste
  directamente en la app de Savant — incluye su Bat Speed real (76.1 mph,
  percentil 92) y Squared-Up% real (21.9%, percentil 24) de 2026.
- Esto también sirvió para detectar que mi Sweet-Spot% simulado estaba
  inflado (50% simulado vs. 29-38% real).

Los datos simulados (todavía usados por el pipeline SQL/XGBoost original)
siguen calibrados contra puntos de referencia reales:

- Bat speed: distribución centrada en ~70.5 mph, calibrada para que el máximo
  se acerque a 79.9 mph (dato real: percentil 100 en Baseball Savant, temporada 2026).
- Barrel%: clasificador que replica la forma pública del criterio real de Statcast
  (ventana de ángulo de lanzamiento que se ensancha sobre 98 mph de EV).
- Exit velocity promedio calibrado a ~88.5 mph (promedio real de MLB).
- xwOBA es una **aproximación simplificada** (no el modelo propietario de MLB),
  etiquetada como tal en cada tabla, gráfico y reporte donde aparece.

### Para usar datos reales completos (con bat-tracking)

En una máquina con acceso normal a internet (no en este sandbox):

```bash
pip install pybaseball
python3 data/fetch_real_data.py
```

Ese script pull real 2024-2025 Statcast + Bat Tracking vía `pybaseball.statcast()`,
y escribe `raw_players.csv`/`raw_batted_balls.csv` en el formato exacto que espera
`etl/clean.py` — el resto del pipeline (SQL, modelo, Streamlit, PDF, Power BI)
corre sin tocar una línea. Esto es lo que resolvería la limitación de
attack_angle/swing_length mencionada arriba.

## Para el portafolio

Este proyecto demuestra: modelado de base de datos relacional, ingeniería de
ETL con validación de calidad de datos, feature engineering informado por
dominio (biomecánica del swing), modelado predictivo con evaluación honesta
(R², MAE, importancia de variables), una aplicación web interactiva, y
generación automatizada de reportes — el ciclo completo de un producto de
datos, no solo un notebook de análisis exploratorio.
