# Post para LinkedIn — EP Swing Intelligence (Capítulo 2: datos reales)

---

## Versión 1 (directa, técnica)

Actualización de un proyecto que vengo construyendo: reemplacé el dataset simulado por datos 100% reales de Baseball Savant — 43 jugadores MLB, temporada 2026, transcritos a mano (percentile rankings + Statcast Batting Statistics) porque este entorno no tiene acceso directo a Savant.

La pregunta sigue siendo la misma: ¿qué tan bien predicen las métricas de swing (bat speed, squared-up%) la calidad de contacto de un bateador (xwOBA, Barrel%)?

Con datos reales, la respuesta es más chica y más honesta que con datos simulados:
📊 R² = 0.27 (xwOBA) y R² = 0.51 (Barrel%) — con solo 2 variables reales disponibles públicamente en Savant (bat_speed, squared_up_pct)
🔍 Las otras 2 variables que mi modelo simulado usaba (attack_angle, swing_length) viven en el leaderboard de bat-tracking, no en la página pública — así que el modelo real es honestamente más simple
📉 Un hallazgo que no escondí: agregar jugadores no siempre sube el R² — jugadores como Contreras o Betts (contacto de alta calidad con bat speed moderado) o Salvador Perez en año de declive por edad no siguen la relación lineal simple, y eso baja el R² aunque el dataset mejore

Por qué comparto esto en vez de solo el número bonito: en analítica deportiva real, saber leer cuándo un modelo simple no alcanza —y por qué— vale más que un R² inflado con datos fabricados. El pipeline completo (SQL → limpieza → modelo → app → reporte) sigue corriendo idéntico sobre este dataset real.

#Baseball #DataScience #SportsAnalytics #MachineLearning #Python

---

## Versión 2 (más corta, para feed)

Reemplacé el dataset simulado de mi proyecto de swing analytics por datos 100% reales: 43 jugadores MLB, transcritos a mano de Baseball Savant.

Resultado honesto: R²=0.27 prediciendo xwOBA con solo 2 variables reales de swing (bat speed, squared-up%) — más chico que mi modelo simulado, pero real de punta a punta, incluyendo el hallazgo de que más jugadores no siempre mejora el modelo.

Stack completo y metodología en los comentarios / link.

#Baseball #DataScience #SportsAnalytics

---

## Sugerencias de imágenes para acompañar el post

1. **La tabla de R² por tamaño de muestra** (31→35→40→43 jugadores) — cuenta la historia de una mirada, incluida la caída.
2. **Captura del dashboard de Streamlit** (scatter Bat Speed vs xwOBA) si quieres mostrar el pipeline en acción.
3. Si quieres una tercera: alguna de las capturas de Savant que transcribiste, como evidencia visual del proceso manual.

## Nota sobre honestidad de datos

El párrafo sobre la caída de R² (40→43) es el más importante para dejar en el post, no el que más tentación da de cortar. Un analista o scout que lea esto va a confiar más en un R²=0.27 explicado que en un R²=0.81 sin contexto — es la diferencia entre "entiendo los límites de mi modelo" y "hice números bonitos".
