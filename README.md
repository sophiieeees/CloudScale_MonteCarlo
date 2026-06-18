# CloudScale_MonteCarlo

## PARTE 1
La simulación Monte Carlo del porblema, se ejecutó en dos plataformas diferentes: Minitab y Python. Los resultados obtenidos en ambas herramientas fueron muy similares. 

<li>Minitab:  Se obtuvo un tiempo promedio de implementación de 12.62 días y una tasa de fallas del 0.771 (es decir 77.1%).  </li>

<li>Python: El tiempo promedio fue de aproximadamente 12.49 días y la tasa de fallas de 75.4% (aunque los datos varian cada que se corre el código).   </li>

### Tabla Comparativa
| Plataforma | Tiempo promedio (días) | Tasa de fallas |
|------------|----------------------|----------------|
| Minitab | 12.62 | 77.1% |
| Python | 12.49 | 75.4% |

### Análisis: 
Dado que el SLA establecido por CloudScale es de 10 días, los resultados muestran que el tiempo promedio de implementación supera dicho límite. Además, entre tres cuartas partes de los clientes (75%–77%) exceden el plazo permitido, lo que implica un alto riesgo de incumplimiento y, por lo tanto, una elevada probabilidad de generar penalizaciones económicas para la empresa.


## PARTE 2 

Para evaluar las posibles soluciones al problema identificado en el modelo base, se desarrollaron dos nuevas iteraciones mediante simulación Monte Carlo utilizando tanto Minitab como Python. Los resultados obtenidos fueron los siguientes:

<li>Minitab: tiempo promedio de 12.62 días y tasa de fallas de 77%. </li>

<li>Python: tiempo promedio de 12.49 días y tasa de fallas de 75.4%.  </li>

### Opción A – Incremento de personal en Tech Provisioning

<li>Minitab: tiempo promedio de 10.58 días y tasa de fallas de 53.1%.  </li>
<li>Python: tiempo promedio de 10.53 días y tasa de fallas de 51.3%. </li>

### Opción B – Automatización mediante API

<li>Minitab: tasa de fallas de 6.5%. </li>
<li>Python: tasa de fallas de 5.2%. </li>

### Tabla Comparativa
| Escenario | Minitab (Dias) | Minitab (Fallos) | Python (Dias) | Python (Fallos) |
|-----------|---------------|----------------------|--------------|----------------------|
| Baseline | 12.62 | 77.1% | 12.49 | 75.4% |
| Option A | 10.58 | 53.1% | 10.53 | 51.3% |
| Option B | 7.591 | 6.5% | 7.59 | 5.2% |


### Análisis:
<br>Los resultados muestran que la Opción B ofrece el mejor desempeño operativo, ya que reduce la tasa de fallas a aproximadamente un 5%, mientras que la Opción A la reduce a cerca del 52%. Esto indica que la automatización es mucho más efectiva para disminuir la variabilidad del proceso y mejorar el cumplimiento del SLA.

Sin embargo, los resultados de la simulación por sí solos no son suficientes para determinar cuál alternativa es la mejor decisión financiera. El caso no proporciona información sobre el costo de contratar personal adicional, el costo de desarrollar e implementar la solución tecnológica ni el monto exacto de las penalizaciones por incumplimiento. Por esta razón, no es posible calcular el retorno de inversión de cada alternativa.

Lo que sí puede concluirse es que la Opción B genera los mejores resultados operativos y la menor cantidad de incumplimientos. No obstante, la decisión final debería complementarse con un análisis económico que compare el costo de implementación de la automatización con los ahorros generados por la reducción de penalizaciones. Dependiendo de esos costos, tanto la Opción A como la Opción B podrían ser alternativas viables en distintos escenarios empresariales.