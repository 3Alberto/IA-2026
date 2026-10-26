# Ejercicio 1 — Q-learning en Cliff Walking

---

## Archivos del Repositorio

| Archivo | Descripción |
| :--- | :--- |
| `cliff_walking.py` | Script principal en Python que implementa el entorno $4 \times 12$, el agente Q-learning, la evaluación *greedy* y la exportación de métricas. |
| `cliff_book.yaml` | Archivo declarativo con la definición geométrica del entorno, recompensas e hiperparámetros del experimento. |
| `recompensas_500_episodios.csv` | Serie histórica generada automáticamente al ejecutar el script con la recompensa acumulada y la media móvil de los 500 episodios. |

---

## Ejecución del Programa

Para correr el entrenamiento con los parámetros por defecto del ejercicio:

```bash
python cliff_walking.py
```

También soporta argumentos por línea de comandos para experimentar con otros hiperparámetros:

```bash
python cliff_walking.py --seed 1 --episodes 500 --epsilon 0.1 --alpha 0.5 --gamma 1.0
```

### Salida Obtenida (`seed = 1`)

```text
Cliff Walking 4×12 (Sutton & Barto)  (kind = grid, 4×12)
start = (3, 0)    goal = (3, 11)    cliffs = (3,1)..(3,10) -> reset to S
actions = ['N', 'E', 'S', 'W'] (tie-break order)
r_step = -1    r_cliff = -100    r_goal = -1
α = 0.5    γ = 1    ε = 0.1    episodes = 500    max_steps = 200    seed = 1

method = q-learning (off-policy)    behaviour = ε-greedy

Greedy policy (arrows)
------------------------------------------------------------------------
row\col  0  1  2  3  4  5  6  7  8  9 10 11
0        →  →  →  →  →  →  →  →  ↓  →  →  ↓
1        →  →  →  →  →  →  →  →  →  →  →  ↓
2        →  →  →  →  →  →  →  →  →  →  →  ↓
3        ↑  C  C  C  C  C  C  C  C  C  C  G

Greedy rollout from S (ε = 0)
------------------------------------------------------------------------
Actions (13 steps): N -> E -> E -> E -> E -> E -> E -> E -> E -> E -> E -> E -> S
States:  (3, 0) -> (2, 0) -> (2, 1) -> (2, 2) -> (2, 3) -> (2, 4) -> (2, 5) -> (2, 6) -> (2, 7) -> (2, 8) -> (2, 9) -> (2, 10) -> (2, 11) -> (3, 11)
greedy return from start (ε = 0): -13

Training returns summary (ε = 0.1)
------------------------------------------------------------------------
   Episodios    Retorno medio       Mín       Máx  Media móvil (últ. 10)
       1..10          -191.50      -922       -29                 -191.50
      11..50           -64.08      -250       -15                  -45.90
     51..100           -44.78      -223       -13                  -35.80
    101..200           -35.85      -214       -13                  -43.10
    201..300           -35.42      -217       -13                  -34.00
    301..400           -32.16      -125       -13                  -24.20
    401..500           -38.16      -215       -13                  -43.50
```

---

## Reporte: 

**Parámetros de ejecución:** $\alpha = 0.5$, $\gamma = 1.0$, $\epsilon = 0.1$, $500$ episodios, $Q_0 = 0$, semilla (`seed`) = $1$.  
**Orden de desempate en $\arg\max$:** `['N', 'E', 'S', 'W']`.

### 1. ¿Por qué el camino de 13 pasos, pegado al acantilado, es óptimo?

En la formulación de *Cliff Walking* de Sutton y Barto, el factor de descuento es $\gamma = 1$, por lo que se trata de una tarea episódica sin descuento donde el retorno total es simplemente la suma directa de las recompensas obtenidas hasta llegar a la meta `G` en `(3, 11)`. Dado que cada transición ordinaria (incluyendo chocar contra un borde o entrar a `G`) tiene un costo de $r = -1$ y caer en el acantilado (`(3, 1)` a `(3, 10)`) penaliza con $r = -100$, maximizar el retorno acumulado equivale exactamente a encontrar la ruta válida con el menor número de pasos posibles entre la salida `S = (3, 0)` y la meta `G = (3, 11)` sin pisar el acantilado.

Como toda la fila 3 entre las columnas 1 y 10 está bloqueada por el acantilado, el agente no puede caminar en línea recta hacia el este desde `S`. Forzosamente debe subir al menos hasta la fila 2 para rodear la zona de peligro. El recorrido geométricamente más corto consiste en:
1. Dar **1 paso al norte (`N`)** desde `(3, 0)` hacia `(2, 0)`.
2. Avanzar **11 pasos al este (`E`)** a lo largo de la fila 2 (bordeando el acantilado desde `(2, 0)` hasta `(2, 11)`).
3. Dar **1 paso al sur (`S`)** desde `(2, 11)` para entrar a `G = (3, 11)`.

Esto suma un total de $1 + 11 + 1 = 13$ pasos, generando un retorno acumulado de $13 \times (-1) = -13$. Cualquier camino más "seguro" (por ejemplo, subir a la fila 1 o a la fila 0) agregaría pasos verticales adicionales de subida y bajada, reduciendo el retorno a $-15$ o $-17$. Por ende, la trayectoria de 13 pasos pegada al borde es la única política óptima.

### 2. ¿Por qué la curva de entrenamiento queda por debajo de −13 aunque la política greedy ya sea óptima?

Esta diferencia se debe a la naturaleza **off-policy** de Q-learning y a que durante los 500 episodios de entrenamiento la conducta del agente mantiene activa la exploración **$\epsilon$-greedy con $\epsilon = 0.1$**. 

Q-learning aprende el valor de la política óptima porque su regla de actualización utiliza $\max_{a'} Q(s', a')$, asumiendo que en el futuro se tomarán únicamente decisiones óptimas. Sin embargo, las recompensas que se grafican en la curva de entrenamiento corresponden a lo que el agente realmente experimenta siguiendo su política de comportamiento ($\epsilon = 0.1$). 

Aunque la tabla $Q$ ya haya convergido al camino óptimo de 13 pasos por la fila 2, en cada una de las 11 casillas junto al borde del acantilado el agente tiene un $10\%$ de probabilidad de elegir una acción completamente al azar. Como hay 4 acciones posibles (`N`, `E`, `S`, `W`), en cada paso junto al borde existe un $2.5\%$ de probabilidad ($0.10 \times 0.25$) de elegir la acción `S` (sur) y caer accidentalmente al acantilado. A lo largo de los 11 pasos en el borde, la probabilidad de sufrir al menos una caída en un episodio es considerable ($\approx 24.3\%$). Cada vez que esto ocurre, el episodio suma una penalización de $-100$ y el agente debe volver a empezar desde `S`, haciendo que la media móvil de entrenamiento oscile alrededor de $-30$ a $-45$. El retorno óptimo de $-13$ solo se observa cuando evaluamos la política apagando la exploración ($\epsilon = 0$).

### 3. En el paso que cae al acantilado, ¿cuál es `s'` en el backup de Q-learning, y por qué ese backup no trata el acantilado como estado terminal?

Cuando el agente ejecuta una acción que lo lleva hacia cualquiera de las casillas del acantilado `(3, 1)` … `(3, 10)`, el estado siguiente que devuelve el entorno para el *backup* de Q-learning es **`s' = S = (3, 0)`** (la casilla de inicio), acompañado de una recompensa inmediata de $r = -100$.

El *backup* no trata esta transición como un estado terminal porque, de acuerdo con la definición del problema en el libro, caer por el acantilado **no termina el episodio**, sino que únicamente penaliza al agente y lo regresa a la salida `S` dentro del mismo episodio para que vuelva a intentarlo. 

En el algoritmo de Q-learning, solo cuando `s'` es verdaderamente terminal (es decir, al entrar a la meta `G`) el valor futuro se fija en $0$. Al caer al acantilado, como el episodio continúa desde `S`, el agente todavía tendrá que caminar desde `S` hasta `G` acumulando más pasos negativos. Por lo tanto, el blanco de actualización (*target*) debe incluir la estimación de lo que costará llegar a la meta a partir de `S`, quedando expresado como:

$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[ -100 + \gamma \max_{a'} Q(S, a') - Q(s, a) \right]$$

Una vez que los valores de la tabla $Q$ convergen (donde $\max_{a'} Q(S, a') = -13$), el valor $Q$ de cualquier acción que arroje al agente al acantilado converge correctamente a $-100 + 1.0(-13) = -113$. Si se tratara erróneamente como terminal, convergería a $-100$, subestimando el costo real de tener que recorrer todo el mapa nuevamente desde el inicio.