# Graficación utilizando Pygame

Este proyecto consiste en la creación de un entorno tipo laberinto utilizando la librería `pygame`. El objetivo es familiarizarse con la creación de entornos para la simulación de agentes inteligentes.

## Capturas de Pantalla

<img src="/graficacion-laberinto/images/img1.png" alt="Captura de Pantalla 1" width="400"/>
Laberinto sin jugador. El punto verde es el punto inicial. El punto rojo es la meta

<img src="/graficacion-laberinto/images/img2.png" alt="Captura de Pantalla 2" width="400"/>
Laberinto con jugador. El punto morado es el jugador

<img src="/graficacion-laberinto/images/img3.png" alt="Captura de Pantalla 3" width="400"/>
Pantalla de victoria. Se consigue cuando el jugador llega a la meta.

## Características del Laberinto

- **Diseño de Laberinto:** El código define un laberinto en forma de matriz utilizando caracteres. Cada celda del laberinto puede ser una pared (`X`), una celda de inicio (`S`), una celda de meta (`E`), o pasillos (`0`) por los que el jugador puede moverse.

- **Interacción del Jugador:** El jugador puede moverse por el laberinto utilizando las teclas de dirección (arriba, abajo, izquierda, derecha). Se implementa una lógica que impide que el jugador se mueva a través de las paredes.

- **Detección de Condición de Victoria:** El juego detecta cuando el jugador alcanza la celda de meta (`E`) y muestra un mensaje de victoria en pantalla. Después de mostrar el mensaje, el programa espera durante 2 segundos antes de finalizar.

- **Representación Visual:** Utilizando colores y formas geométricas, el código visualiza el laberinto, la posición del jugador, la celda de inicio y la celda de meta en una ventana gráfica.

- **Control de Velocidad:** El código controla la velocidad de actualización de la pantalla para proporcionar una experiencia de juego suave y fluida.

- **Flexibilidad del Laberinto:** El laberinto se define como una matriz de caracteres, lo que permite a los usuarios modificar y personalizar la estructura del laberinto según sus preferencias.

- Por último, el laberinto se puede ejecutar con el siguiente comando:

   ```bash
   python graficacion-laberinto.py
