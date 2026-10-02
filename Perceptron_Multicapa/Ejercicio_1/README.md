
# Archivos modificados:

## 04 Multilayer perceptron-Modificado:
https://colab.research.google.com/drive/1-DiqStR5UvUfMNyocvSz2SJOkIhpqzVI?usp=sharing

## 05 Keras - multilayer perceptron - iris-Modificado:
https://colab.research.google.com/drive/1ihxIbrlrHpGDZlkBVaIvc-Ezt33HI3FN?usp=sharing


## Reporte
### 1. Sobre si el error baja o se estanca con más capas:
La verdad es que al meterle las dos capas extras, la red no mejoró para nada; de hecho, se estancó horrible. Corriendo las mismas 500 épocas con la tasa de 0.03, la red profunda se quedó "planchada" con un error altísimo y no logró converger.

### 2. Sobre las curvas de NumPy vs Keras y sus diferencias:
Aunque en ambos casos la red quedó atorada, las curvas de error no se ven exactamente iguales. Esto pasa por las diferencias de implementación que hay por debajo en las librerías. Primero, la inicialización: del script de NumPy sacamos pesos aleatorios simples (entre -0.5 y 0.5), pero Keras nos hace el paro usando la inicialización por defecto, lo que ayuda a que las neuronas no se saturen tan rápido en la primera iteración.Otra diferencia clave es cómo le pasamos los datos. En NumPy armamos el ciclo para que actualice muestra por muestra pasando siempre en el mismo orden, mientras que Keras por defecto agarra batches de 32 y revuelve los datos por época, lo que hace que su curva baje de forma mucho menos caótica. 

###3. Por qué fallan las sigmoides apiladas con MSE en Iris:
Acá hubo un problema de desvanecimiento de gradiente. La derivada máxima de la función sigmoide es de apenas 0.25. Cuando tiramos el backpropagation para actualizar los pesos, la regla de la cadena nos obliga a multiplicar esas derivadas capa por capa ($0.25 \times 0.25 \times 0.25$).Para cuando el gradiente logra cruzar hasta la primera capa oculta, el número ya es pequeñisimo. Como resultado, los pesos iniciales casi no se actualizan y la red entera se congela; por eso en las gráficas el error baja tantito al inicio y de repente se vuelve una línea plana. Además, el dataset de Iris es facilísimo de clasificar; meterle cuatro capas ocultas es una exageración de complejidad que solo nos llenó la función de pérdida de zonas planas donde el gradiente se muere.