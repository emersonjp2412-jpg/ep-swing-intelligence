# EP Swing Intelligence — Guía de armado en Power BI Desktop

No pude generar el `.pbix` directamente (Power BI Desktop es una app de Windows,
no corre en este entorno). Lo que sí te dejo aquí es todo lo que necesitas para
armarlo en 15-20 minutos: los datos ya limpios en formato estrella, las
relaciones, y las medidas DAX ya escritas.

## 1. Archivos a importar

Carga estos 4 CSV en Power BI (`Obtener datos` → `Texto/CSV`):

| Archivo | Rol | Grano |
|---|---|---|
| `dim_players.csv` | Dimensión | 1 fila por jugador |
| `fact_player_season_summary.csv` | Hecho principal | 1 fila por jugador (agregado) |
| `fact_model_predictions.csv` | Hecho — salida del modelo | 1 fila por jugador |
| `fact_batted_balls.csv` | Hecho detallado (opcional, pesado: ~44k filas) | 1 fila por batazo |

## 2. Relaciones (Vista de modelo)

```
dim_players (player_id) ──1───* fact_player_season_summary (player_id)
dim_players (player_id) ──1───* fact_model_predictions (player_id)
dim_players (player_id) ──1───* fact_batted_balls (player_id)
```

Todas 1-a-muchos, dirección única, desde `dim_players`. Si vas a usar
`fact_batted_balls`, considera cargarlo en Modo DirectQuery o agregarlo antes
si el archivo se siente pesado en Import mode.

## 3. Medidas DAX

Crear estas medidas sobre `fact_player_season_summary` (salvo que se indique otra tabla):

```dax
Bat Speed Promedio = AVERAGE(fact_player_season_summary[avg_bat_speed])

Barrel % Promedio =
DIVIDE(
    SUMX(fact_player_season_summary, fact_player_season_summary[barrel_pct] * fact_player_season_summary[n_bbe]),
    SUM(fact_player_season_summary[n_bbe])
)

xwOBA Promedio (est.) =
DIVIDE(
    SUMX(fact_player_season_summary, fact_player_season_summary[avg_xwoba_est] * fact_player_season_summary[n_bbe]),
    SUM(fact_player_season_summary[n_bbe])
)

Jugadores Calificados = DISTINCTCOUNT(fact_player_season_summary[player_id])

-- Sobre fact_model_predictions:
Error Promedio del Modelo (MAE) = AVERAGE(fact_model_predictions[residual])

xwOBA Predicho vs Real (delta) =
AVERAGE(fact_model_predictions[predicted_xwoba]) - AVERAGE(fact_model_predictions[actual_xwoba])

-- Percentil de un jugador dentro del roster cargado (usar en tarjeta con slicer de jugador):
Percentil Bat Speed =
VAR CurrentValue = SELECTEDVALUE(fact_player_season_summary[avg_bat_speed])
RETURN
DIVIDE(
    COUNTROWS(FILTER(ALL(fact_player_season_summary), fact_player_season_summary[avg_bat_speed] <= CurrentValue)),
    COUNTROWS(ALL(fact_player_season_summary))
) * 100
```

## 4. Layout sugerido (una página, estilo el dashboard de Streamlit)

- **Fila superior:** 4 tarjetas (KPI cards) — Jugadores Calificados, Bat Speed
  Promedio, Barrel % Promedio, xwOBA Promedio.
- **Fila media, dos columnas:**
  - Gráfico de dispersión: `avg_bat_speed` (eje X) vs `avg_xwoba_est` (eje Y),
    tamaño = `n_bbe`, color = `barrel_pct`.
  - Gráfico de dispersión: `avg_squared_up_pct` vs `barrel_pct`, color = `avg_bat_speed`.
- **Fila inferior:** tabla con Top 15 por `avg_xwoba_est` (columnas: nombre,
  equipo, posición, bat speed, barrel%, xwOBA real, xwOBA predicho).
- **Slicer lateral:** por `team` y por `position` (desde `dim_players`).

## 5. Estilo EP (tema de Power BI)

`Vista` → `Temas` → `Personalizar tema actual` → pegar estos colores:

- Fondo: `#0B1B33`
- Acento primario: `#D4A53A`
- Texto: `#F5F3EC`
- Acento secundario: `#5BA8E0`

## 6. Actualización automática

Como los 4 CSV los regenera `etl/clean.py` + `model/train_model.py` cada vez
que corres el pipeline, puedes:
- Apuntar Power BI a la carpeta `powerbi/` con "Actualizar" manual, o
- Publicar a Power BI Service y configurar un gateway con actualización
  programada apuntando a la misma carpeta (si automatizas el pipeline con un
  cron/task scheduler que regenere los CSV).
