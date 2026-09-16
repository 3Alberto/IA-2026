# Ejercicio 2 — Descripción PEAS de agentes inteligentes

## 1. Asistente virtual de voz

* **Performance:** Lograr el reconocimiento correcto de las órdenes, ejecutar correctamente las acciones solicitadas y respetar las restricciones de privacidad.
* **Environment:** Hogar u oficina con personas, ruido ambiental, diferentes acentos y formas de hablar, dispositivos inteligentes y conexión a internet. Es **parcialmente observable** y **estocástico**.
* **Actuators:** Reproducir respuestas de voz; enviar mensajes; realizar llamadas; controlar luces, televisores, cerraduras u otros dispositivos; reproducir música; crear alarmas y recordatorios; realizar búsquedas o ejecutar comandos mediante servicios conectados.
* **Sensors:** Micrófono; detección de palabra de activación; historial de conversaciones; texto y contexto de la conversación; hora y ubicación configuradas; información obtenida mediante APIs y servicios externos; estados de dispositivos inteligentes conectados.

**Justificación:** Es parcialmente observable porque el asistente únicamente recibe la información disponible mediante sus sensores y servicios conectados. También es estocástico porque el habla humana puede ser ambigua y las respuestas de servicios externos no siempre son iguales.

---

## 2. Robot aspirador doméstico

* **Performance:** Minimizar polvo y suciedad residual, evitar colisiones y caídas, completar la limpieza en el menor tiempo posible, reducir el consumo de batería, regresar correctamente a la estación de carga y minimizar interrupciones.
* **Environment:** Habitaciones, pasillos, muebles, paredes, escaleras, personas, mascotas y objetos que pueden estar en el piso. Es **parcialmente observable** y **dinámico**.
* **Actuators:** Motores de las ruedas; sistema de dirección y movimiento; motor de aspiración; cepillos; mecanismo de navegación; emisión de alertas o mensajes.
* **Sensors:** Sensores de proximidad; sensores infrarrojos o LiDAR; cámaras en modelos que las incorporan; sensores de caída; sensores de contacto; sensores de suciedad; sensores de ruedas y odometría; nivel de batería.

**Justificación:** El robot no tiene una visión completa del departamento desde el principio, por lo que el entorno es parcialmente observable. También es dinámico porque puede haber personas o mascotas moviéndose.

---

## 3. Sistema de recomendación de streaming

* **Performance:** Maximizar la probabilidad de que el usuario seleccione una recomendación; aumentar el tiempo de reproducción; mantener la diversidad y relevancia de las recomendaciones.
* **Environment:** Plataforma digital con grandes catálogos de contenido y usuarios con preferencias cambiantes. Es **estocástico** y **secuencial**.
* **Actuators:** Mostrar películas, series o canciones recomendadas; ordenar y priorizar contenidos; personalizar listas y páginas principales; generar playlists; modificar automáticamente la selección de contenido mostrado.
* **Sensors:** Historial de reproducciones; búsquedas; contenidos completados o abandonados; calificaciones; canciones omitidas; duración de reproducción; clics; listas creadas; dispositivo utilizado; horario y frecuencia de consumo.

**Justificación:** Es estocástico porque el comportamiento humano y los gustos son inciertos e impredecibles. También es secuencial, ya que las recomendaciones de hoy y la forma en que el usuario reaccione a ellas entrenarán y condicionarán las recomendaciones del futuro.

---

## 4. Vehículo autónomo en ciudad

* **Performance:** Minimizar accidentes y situaciones de riesgo; cumplir las normas de tránsito; llegar al destino correctamente; reducir tiempo de viaje y consumo de energía; mantener la comodidad de los pasajeros; minimizar maniobras bruscas y errores de navegación.
* **Environment:** Calles urbanas, semáforos, vehículos, peatones, ciclistas, motocicletas, señales de tránsito, construcciones, lluvia y otros factores climáticos. Es **parcialmente observable** y **estocástico**.
* **Actuators:** Dirección del volante; acelerador; freno; transmisión; intermitentes; luces; claxon; control de navegación y trayectoria.
* **Sensors:** Cámaras; LiDAR; radar; sensores ultrasónicos; GPS; unidad de medición inercial (IMU); sensores de velocidad y posición de las ruedas; mapas digitales; información de tráfico.

**Justificación:** Es parcialmente observable porque el vehículo no puede conocer perfectamente todos los acontecimientos a su alrededor. También es estocástico por el comportamiento impredecible de otros agentes, como otros conductores, peatones y animales.

---

## 5. Agente de trading algorítmico en bolsa

* **Performance:** Maximizar el rendimiento ajustado al riesgo; minimizar pérdidas y costos de transacción; controlar la exposición financiera; reducir errores operativos; cumplir límites de riesgo y reglas del mercado; mantener una baja latencia en la ejecución de órdenes.
* **Environment:** Mercado bursátil con acciones, compradores, vendedores, otros algoritmos, noticias económicas y cambios en precios. Es **parcialmente observable**, **estocástico** y **secuencial**.
* **Actuators:** Enviar órdenes de compra; enviar órdenes de venta; modificar o cancelar órdenes; establecer límites de precio; ajustar el tamaño de posiciones; cerrar operaciones; redistribuir capital entre activos.
* **Sensors:** Cotizaciones en tiempo real; precios históricos; volumen negociado; libro de órdenes; indicadores técnicos; noticias disponibles mediante APIs; información financiera; estado de la cartera; saldo disponible; confirmaciones de ejecución.

**Justificación:** Es parcialmente observable, ya que el agente no tiene acceso a las intenciones de otros traders ni a información privada corporativa. Además, es estocástico debido a la incertidumbre de los movimientos del mercado. También es secuencial porque las operaciones anteriores afectan el capital y el riesgo disponible para las siguientes.

---

## 6. Sistema de diagnóstico médico asistido por IA

* **Performance:** Maximizar la precisión de las sugerencias diagnósticas; detectar oportunamente señales de riesgo; reducir el tiempo de análisis; presentar información relevante; mantener la seguridad de los datos.
* **Environment:** Hospital, clínica o consultorio, con pacientes, médicos, expedientes clínicos, estudios de laboratorio e imágenes médicas. Es **parcialmente observable** y **estático**.
* **Actuators:** Generar una lista de posibles diagnósticos; señalar regiones sospechosas en una imagen; emitir alertas; priorizar casos; solicitar o recomendar estudios adicionales como apoyo al profesional; presentar estimaciones o probabilidades.
* **Sensors:** Síntomas registrados; antecedentes clínicos; signos vitales; resultados de laboratorio; radiografías; tomografías; resonancias; fotografías clínicas; expedientes electrónicos; resultados de estudios previos.

**Justificación:** Es estático porque durante el proceso en el que el agente analiza la imagen y/o los datos clínicos, estos permanecen sin cambios mientras realiza el cálculo y genera su resultado.

---

## 7. Dron de inspección de infraestructura

* **Performance:** Maximizar la cobertura de inspección; detectar correctamente daños y anomalías; mantener una distancia segura de la infraestructura; completar la misión con el menor consumo de batería; obtener imágenes de suficiente calidad y evitar accidentes.
* **Environment:** Infraestructura industrial o civil, estructuras elevadas, cables, tuberías, viento, lluvia, obstáculos y zonas de difícil acceso. Es **parcialmente observable** y **secuencial**.
* **Actuators:** Motores de las hélices; movimiento hacia adelante, atrás, arriba, abajo y lateral; giro y orientación de la aeronave; control de velocidad; activación de iluminación o dispositivos de inspección; regreso automático al punto de origen.
* **Sensors:** Cámaras RGB; cámaras térmicas; LiDAR; sensores ultrasónicos o de distancia, según el modelo; GPS; IMU; altímetro; sensores de velocidad; sensores de batería; sistemas de detección de obstáculos.

**Justificación:** Es parcialmente observable porque el dron solamente puede analizar las zonas captadas por sus sensores. También es secuencial, ya que elegir una ruta determinada influye en toda la inspección posterior.

---

## 8. Agente jugador de ajedrez

* **Performance:** Maximizar la probabilidad de ganar la partida; evitar movimientos que conduzcan a una derrota; respetar las reglas del ajedrez; utilizar eficientemente el tiempo disponible; minimizar errores estratégicos.
* **Environment:** Tablero de ajedrez, piezas propias y del oponente, reglas oficiales y reloj de partida. Es **observable**, **determinista** y **secuencial**.
* **Actuators:** Seleccionar una pieza; realizar un movimiento legal; capturar una pieza; activar acciones relacionadas con el reloj mediante la interfaz.
* **Sensors:** Posición actual de todas las piezas; movimientos realizados anteriormente; turno actual; reloj de la partida; historial de movimientos; estado de la partida, incluyendo jaque, mate o tablas.

**Justificación:** Es observable porque el agente conoce todas las piezas y posiciones relevantes. También es determinista en cuanto a las reglas y resultados de los movimientos, pero sigue siendo secuencial porque una jugada cambia el estado del juego y afecta todas las decisiones posteriores.
