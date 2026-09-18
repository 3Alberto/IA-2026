# Ejercicio 1 — Comparar Greedy y A* en el mapa de Rumania

Contexto: Se presenta los resultados de ejecutar dos algoritmos de búsqueda informada (Greedy y A*) para encontrar una ruta entre dos ciudades del mapa carretero de Rumania. Además, ambos algoritmos comparten el mismo grafo, el mismo RouteFindingProblem y la misma heurística h(n).

## Las ciudades seleccionadas para este ejercicio fueron: Oradea (origen) y Eforie (destino).

## Subgrafo de la Ruta Encontrada

```text
Oradea (h≈513)
  |
(151)
  |
Sibiu (h≈391) --------- (99) --------- Fagaras (h≈301)
  |                                        |
(80)                                       |
  |                                        |
Rimnicu Vilcea (h≈349)                   (211)
  |                                        |
(97)                                       |
  |                                        |
Pitesti (h≈253) ------ (101) ----------Bucharest (h≈166)
                                           |
                                          (85)
                                           |
                                        Urziceni (h≈120)
                                           |
                                         (98)
                                           |
                                        Hirsova (h≈64)
                                           |
                                         (86)
                                           |
                                        Eforie (h=0)
```

## Tabla Comparativa de Algoritmos

| **Algorithm** | **Path (Route Found)** | **Depth** | **Cost (km)** | **Expanded Nodes (Approx.)** | **Heuristic Used** | 
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Greedy Best-First** | Oradea → Sibiu → Fagaras → Bucharest → Urziceni → Hirsova → Eforie | 6 roads | 730 km | 6 |  Distancia Euclidiana | 
| **A\*** | Oradea → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest → Urziceni → Hirsova → Eforie | 7 roads | 698 km | 11 | EDistancia Euclidiana | 

## Análisis de Resultados

### ¿A* encontró el camino de menos km? ¿Greedy coincidió o se desvió?

Sí, **A*** encontró el camino con la menor distancia, que fue de **698 km**. Por otro lado, **Greedy Best-First Search** tomó una ruta diferente y terminó recorriendo **730 km**. Esto muestra que, aunque Greedy puede encontrar una solución rápidamente, no siempre obtiene el camino más corto, mientras que A* toma en cuenta más información para buscar una ruta óptima.

### ¿Por qué Greedy puede devolver un camino más caro aunque h sea admisible?

Greedy puede encontrar un camino más caro porque solamente se fija en el valor de la **heurística h**, es decir, en qué tan cerca parece estar cada ciudad del objetivo. No toma en cuenta los kilómetros que ya se han recorrido para llegar hasta ese punto.
Por ejemplo, desde **Sibiu**, Greedy eligió ir hacia **Fagaras** en lugar de **Rimnicu Vilcea**, porque Fagaras parecía estar más cerca de Bucarest según la distancia en línea recta. Sin embargo, al tomar en cuenta las distancias reales de las carreteras, la ruta por Fagaras terminó siendo más larga. Por Fagaras se recorren **310 km**, mientras que por Rimnicu Vilcea y Pitesti se recorren aproximadamente **278 km**. Por eso, aunque la heurística sea admisible, Greedy puede terminar escogiendo una ruta que no sea la más económica.

### En el camino de A*, ¿f tiende a no disminuir a lo largo de la ruta? Relaciónalo con que h sea consistente (en particular si el destino es Bucharest y se usa la tabla AIMA).

Sí, en el recorrido de **A*** el valor de **f** tiende a mantenerse igual o aumentar conforme se avanza por la ruta. Esto se debe a que la heurística utilizada es **consistente**.
Cuando el destino es **Bucarest** y se utiliza la tabla de distancias en línea recta de AIMA, la heurística cumple con esta propiedad. En términos sencillos, significa que la estimación de lo que falta por recorrer no puede ser mayor que el costo de llegar al siguiente nodo más la estimación desde ese nuevo nodo. Por esta razón, al avanzar en el camino, el valor de **f = g + h** normalmente no disminuye. Esto ayuda a que A* pueda encontrar una solución óptima sin tener que reconsiderar constantemente los caminos que ya fueron evaluados.
