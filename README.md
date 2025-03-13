**Juego de la Culebrita (Snake)**

El Juego de la Culebrita es una implementación clásica del famoso juego Snake utilizando la biblioteca Pygame en Python. En este juego, el jugador controla una serpiente que crece al comer manzanas. El objetivo es obtener la mayor puntuación posible evitando chocar con las paredes o con el propio cuerpo de la serpiente.

📌 Características del Proyecto

Menú Principal: Permite navegar entre opciones como Jugar, Niveles, Opciones y Salir.

Niveles: Diferentes velocidades (Fácil, Medio, Difícil) para ajustar la dificultad del juego.

Opciones: Personalización del color de la serpiente.

Interfaz Interactiva: Los botones del menú se pueden seleccionar con el mouse.

Gráficos Mejorados: Imágenes personalizadas para la cabeza de la serpiente, la manzana y el fondo del juego.

🎮 Características Principales

Menú Principal

Opciones interactivas para:

Iniciar el juego.

- Seleccionar niveles.
- Cambiar opciones.
- Salir del juego.

Botones resaltados al pasar el mouse.

Niveles

- Fácil: Velocidad baja.
- Medio: Velocidad moderada.
- Difícil: Velocidad alta.

Opciones

Personalización del color de la serpiente:

- Verde.
- Azul.
- Amarillo.

Juego Principal

- Control de la serpiente con las flechas del teclado.
- Comida representada por una imagen de manzana.
- Sistema de puntuación que aumenta al comer manzanas.
- Pantalla de Game Over con opción para reiniciar el juego.

Gráficos y Diseño

- Fondo personalizado para el juego y los menús.
- Imágenes para la cabeza de la serpiente y la comida.
- Interfaz limpia y atractiva.

🧰 Requisitos del Sistema

Para ejecutar este proyecto, necesitas lo siguiente:

- Python 3.x instalado en tu sistema.
- La biblioteca Pygame instalada. Puedes instalarla con el siguiente comando:

`pip install pygame`

- Asegúrate de tener las imágenes requeridas (manzana.png, fondo.png, cabeza.png) en la misma carpeta que el archivo del juego o en una subcarpeta llamada assets/.

📂 Estructura del Proyecto
```
snake_game/
│
├── snake_game.py          # Código principal del juego
├── README.md              # Documentación del proyecto
├── manzana.png            # Imagen de la manzana
├── fondo.png              # Imagen de fondo
└── cabeza.png             # Imagen de la cabeza de la serpiente
```

▶️ Cómo Ejecutar el Juego

1. Clona o descarga el repositorio en tu computadora
2. Asegúrate de tener Python 3.x y Pygame instalados.
3. Coloca las imágenes (manzana.png, fondo.png, cabeza.png) en la misma carpeta que snake_game.py.
4. Abre una terminal en la carpeta del proyecto y ejecuta el siguiente comando:
   
`python snake_game.py`

¡Disfruta del juego!

🎮 Controles del Juego

Movimiento de la Serpiente

- Flecha Arriba: Mover hacia arriba.
- Flecha Abajo: Mover hacia abajo.
- Flecha Izquierda: Mover hacia la izquierda.
- Flecha Derecha: Mover hacia la derecha.

Menú Principal

Usa el mouse para seleccionar las opciones: Jugar, Niveles, Opciones o Salir.

Pantalla de Game Over

- Presiona ENTER para reiniciar el juego.

📃 Licencia

- Este proyecto se distribuye bajo la licencia MIT. ¡Siéntete libre de usar, modificar y compartir este código! 🚀
