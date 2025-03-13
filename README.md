# Juego-de-la-Culebrita-Snake-
El Juego de la Culebrita es una implementación clásica del famoso juego Snake utilizando la biblioteca Pygame en Python. En este juego, el jugador controla una serpiente que crece al comer manzanas. El objetivo es obtener la mayor puntuación posible evitando chocar con las paredes o con el propio cuerpo de la serpiente.

Este proyecto incluye características adicionales como:

Menú Principal : Permite navegar entre opciones como "Jugar", "Niveles", "Opciones" y "Salir".
Niveles : Diferentes velocidades (Fácil, Medio, Difícil) para ajustar la dificultad del juego.
Opciones : Cambiar el color de la serpiente y personalizar la experiencia de juego.
Interfaz Interactiva : Los botones del menú son seleccionables con el mouse.
Gráficos Mejorados : Imágenes personalizadas para la cabeza de la serpiente, la manzana y el fondo del juego.
Características Principales
Menú Principal :
Opciones interactivas para iniciar el juego, seleccionar niveles, cambiar opciones o salir.
Botones resaltados cuando el mouse está sobre ellos.
Niveles :
Fácil: Velocidad baja.
Medio: Velocidad moderada.
Difícil: Velocidad alta.
Opciones :
Cambiar el color del cuerpo de la serpiente (Verde, Azul, Amarillo).
Personalización visual para mejorar la experiencia del jugador.
Juego Principal :
Serpiente controlada con las flechas del teclado.
Comida representada por una imagen de manzana.
Sistema de puntuación que aumenta al comer manzanas.
Pantalla de "Game Over" con opción para reiniciar.
Gráficos y Diseño :
Fondo personalizado para el juego y los menús.
Imagenes para la cabeza de la serpiente y la comida.
Interfaz limpia y atractiva.
Requisitos del Sistema
Para ejecutar este proyecto, necesitas lo siguiente:

Python 3.x instalado en tu sistema.
La biblioteca Pygame instalada. Puedes instalarla usando pip:
pip install pygame
Las imágenes requeridas (manzana.png, fondo.png, cabeza.png) deben estar en la misma carpeta que el archivo del juego o en una subcarpeta llamada assets/.
Estructura del Proyecto
snake_game/
│
├── snake_game.py          # Código principal del juego
├── README.md              # Documentación del proyecto
├── manzana.png            # Imagen de la manzana
├── fondo.png              # Imagen de fondo
└── cabeza.png             # Imagen de la cabeza de la serpiente
Cómo Ejecutar el Juego
Clona o descarga el repositorio en tu computadora.
Asegúrate de tener instalado Python 3.x y Pygame.
Coloca las imágenes (manzana.png, fondo.jpg, cabeza.png) en la misma carpeta que el archivo snake_game.py.
Abre una terminal en la carpeta del proyecto y ejecuta el siguiente comando:
python snake_game.py
¡Disfruta del juego!
Controles del Juego
Movimiento de la Serpiente :
Flecha Arriba: Mover hacia arriba.
Flecha Abajo: Mover hacia abajo.
Flecha Izquierda: Mover hacia la izquierda.
Flecha Derecha: Mover hacia la derecha.
Menú Principal :
Usa el mouse para seleccionar opciones como "Jugar", "Niveles", "Opciones" o "Salir".
Pantalla de Game Over :
Presiona ENTER para reiniciar el juego.
