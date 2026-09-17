# Ejercicio 1 — Comparar BFS, UCS, DFS, DLS e IDS en el mapa de Rumania

Contexto: Se presenta los resultados de ejecutar múltiples algoritmos de búsqueda no informada y de costo uniforme sobre el mapa de Rumania, partiendo de **Lugoj** con destino a **Hirsova**.

Subgrafo de la Ruta Encontrada

```text
(Lugoj) --70-- (Mehadia) --75-- (Drobeta) --120-- (Craiova)
                                                      |
                                                     138
                                                      |
(Hirsova) --98-- (Urziceni) --85-- (Bucharest) --101-- (Pitesti)
```

## Tabla Comparativa de Algoritmos

| Algoritmo | Status | Path | Depth (roads) | Cost (km) | Expanded |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BFS** | success | Lugoj → Mehadia → Drobeta → Craiova → Pitesti → Bucharest → Urziceni → Hirsova | 7 | 687 | 15 |
| **UCS** | success | Lugoj → Mehadia → Drobeta → Craiova → Pitesti → Bucharest → Urziceni → Hirsova | 7 | 687 | 15 |
| **DFS** | success | Lugoj → Mehadia → Drobeta → Craiova → Pitesti → Bucharest → Urziceni → Hirsova | 7 | 687 | 13 |
| **DLS (`--limit 3`)** | cutoff | *N/A* | *N/A* | *N/A* | 5 |
| **DLS (`--limit 7`)** | success | Lugoj → Mehadia → Drobeta → Craiova → Pitesti → Bucharest → Urziceni → Hirsova | 7 | 687 | 9 |
| **IDS** | success | Lugoj → Mehadia → Drobeta → Craiova → Pitesti → Bucharest → Urziceni → Hirsova | 7 | 687 | 63 |

## Análisis de Resultados

### 1. ¿BFS encontró el camino con menos carreteras? ¿UCS el de menos km?
Sí. BFS busca el camino que tenga la menor cantidad de conexiones o carreteras, mientras que UCS busca el camino que tenga el menor costo acumulado, que en este caso corresponde a la distancia en kilómetros. En el caso de Lugoj a Hirsova, los dos algoritmos encontraron la misma ruta. Esto se debe a que esa ruta tiene tanto la menor cantidad de carreteras, que son 7, como la menor distancia total, que es de 687 km

### 2. ¿Por qué DFS puede devolver un camino más largo aunque el grafo sea el mismo?
Esto sucede porque DFS va recorriendo una rama del grafo hasta llegar al final antes de regresar y probar otra opción. Por esta razón, no compara todas las rutas para saber cuál es la más corta o la que tiene menor costo. Cuando encuentra una ruta que llega al objetivo, termina la búsqueda. En este caso encontró la ruta óptima debido al orden en que se fueron revisando los nodos, pero esto no significa que DFS siempre encuentre la mejor ruta. Dependiendo del orden de los nodos, podría encontrar primero una ruta mucho más larga.

### 3. ¿Con qué límite DLS pasó de cutoff a solución, y cómo se relaciona esto con la profundidad del camino de BFS/IDS?
DLS tuvo un resultado de cutoff cuando se utilizó un límite de 3, ya que no podía llegar hasta la meta con esa profundidad. Después, al aumentar el límite a 7, la búsqueda terminó con success porque la solución se encuentra a una profundidad de 7 carreteras. Esto coincide con el resultado obtenido mediante BFS. También se relaciona con IDS, ya que este algoritmo va aumentando poco a poco el límite de profundidad hasta encontrar la solución. De esta manera, puede obtener una solución con la menor profundidad sin utilizar tanta memoria como BFS.