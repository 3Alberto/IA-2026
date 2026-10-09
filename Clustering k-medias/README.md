# Ejercicio 1 — Separar los blobs y volver a elegir (k)

# Centros modificados:




# Archivo modificado:
https://colab.research.google.com/drive/1E5eJ0dFXIh4YddHdrPoIUU4VHAMcB36Q?usp=sharing

## En la carpeta capturas se encuentran las imagenes de las graficas originales y modificadas.

# Reporte:

### 1. En los datos de Géron, ¿por qué el codo “prefiere” $k = 4$ si se usaron 5 centros?

Básicamente porque dos de los grupitos de la izquierda estaban casi pegados.
Tenían centros en $y = 1.8$ y $y = 1.3$ (separados por apenas $0.5$) y además eran muy chiquitos y compactos ($\text{std} = 0.1$). La inercia lo único que hace es sumar qué tan lejos están los puntos de su centroide; entonces, cuando el algoritmo junta esos dos grupitos en uno solo, los puntos siguen estando bastante cerca y la inercia casi no sube.
El codo busca dónde se da la última "gran mejora". Como separar esos dos grupos pequeños apenas baja la inercia, la gráfica no hace un quiebre notorio entre 4 y 5, y el codo visual se queda atorado en **$k = 4$**.

### 2. Con los blobs separados, ¿el codo y la silueta coinciden en el mismo $k$? ¿Ese $k$ es 5?

Sí, en la versión separada los dos coinciden en $k = 5$:
* **El codo:** Al pasar de 4 a 5 clusters, la inercia baja un montón (más de 400 puntos), pero al pasar de 5 a 6 apenas baja unos 24 puntos. Ahí se ve clarísimo el doblez en **$k = 5$**.
* **La silueta:** La gráfica tiene su punto más alto justo en **$k = 5$** (llega a casi $0.72$, mientras que con 4 se queda abajo de $0.60$).
Al estar los cinco grupos bien repartidos, las dos herramientas dan la respuesta correcta.

### 3. Si el codo sigue saliendo en 4, ¿qué falta mover?

Significa que el algoritmo todavía "siente" que dos grupos son en realidad uno solo. La relación clave aquí es distancia entre centros vs. dispersión (`blob_std`):
* **O alejas más los centros:** Aumentas la distancia en $x$ o en $y$ para que no queden tan vecinos.
* **O reduces el `blob_std`:** Haces las nubes más concentradas y apretaditas para que no se mezclen las orillas.
Para que K-Means no se confunda, la distancia entre cualquier par de centros tiene que ser bastante mayor que la suma de sus radios de dispersión ($\text{distancia} \gg \text{std}_1 + \text{std}_2$). Si la distancia es chica comparada con el tamaño de las nubes, el codo siempre va a preferir fusionarlas.

# Ejecutado desde google colab

![alt text](image.png)