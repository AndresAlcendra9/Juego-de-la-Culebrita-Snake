import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Culebrita")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)

# Cargar imágenes
background_image = pygame.image.load("fondo.png")  # Fondo
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Ajustar tamaño
apple_image = pygame.image.load("manzana.png")  # Manzana
apple_image = pygame.transform.scale(apple_image, (BLOCK_SIZE, BLOCK_SIZE))  # Ajustar tamaño
snake_head_image = pygame.image.load("cabeza.png")  # Cabeza de la serpiente
snake_head_image = pygame.transform.scale(snake_head_image, (BLOCK_SIZE, BLOCK_SIZE))  # Ajustar tamaño

# Variables Globales
current_level = "Fácil"  # Nivel predeterminado
snake_color = GREEN      # Color predeterminado del cuerpo de la serpiente

# Fuentes
font = pygame.font.SysFont("Arial", 24)
title_font = pygame.font.SysFont("Arial", 48)

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Clase Snake
class Snake:
    def __init__(self):
        self.body = [[WIDTH // 2, HEIGHT // 2]]
        self.direction = "RIGHT"
        self.grow = False

    def move(self):
        head = self.body[0].copy()
        if self.direction == "UP":
            head[1] -= BLOCK_SIZE
        elif self.direction == "DOWN":
            head[1] += BLOCK_SIZE
        elif self.direction == "LEFT":
            head[0] -= BLOCK_SIZE
        elif self.direction == "RIGHT":
            head[0] += BLOCK_SIZE

        # Agregar nueva cabeza
        self.body.insert(0, head)

        # Si no crece, eliminar la cola
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self):
        # Dibujar la cabeza de la serpiente
        screen.blit(snake_head_image, self.body[0])
        # Dibujar el resto del cuerpo
        for segment in self.body[1:]:
            pygame.draw.rect(screen, snake_color, (*segment, BLOCK_SIZE, BLOCK_SIZE))

    def check_collision(self):
        head = self.body[0]
        # Colisión con bordes
        if (
            head[0] < 0
            or head[0] >= WIDTH
            or head[1] < 0
            or head[1] >= HEIGHT
        ):
            return True
        # Colisión con su propio cuerpo
        if head in self.body[1:]:
            return True
        return False

    def eat_food(self, food_position):
        if self.body[0] == food_position:
            self.grow = True
            return True
        return False

# Clase Food
class Food:
    def __init__(self):
        self.position = [random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                         random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE]

    def draw(self):
        # Dibujar la imagen de la manzana
        screen.blit(apple_image, self.position)

# Función para mostrar texto en pantalla
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Menú Principal
def main_menu():
    while True:
        screen.blit(background_image, (0, 0))  # Dibujar fondo
        draw_text("Culebrita", title_font, WHITE, WIDTH // 2, HEIGHT // 4)

        # Definir hitboxes para los botones
        button_width, button_height = 200, 50
        play_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - 30, button_width, button_height)
        levels_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 20, button_width, button_height)
        options_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 70, button_width, button_height)
        quit_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 120, button_width, button_height)

        # Obtener posición del mouse
        mouse_pos = pygame.mouse.get_pos()

        # Resaltar botones si el mouse está sobre ellos
        for button, text in [(play_button, "Jugar"), (levels_button, "Niveles"),
                             (options_button, "Opciones"), (quit_button, "Salir")]:
            if button.collidepoint(mouse_pos):
                pygame.draw.rect(screen, GRAY, button)  # Resaltar el botón
            else:
                pygame.draw.rect(screen, WHITE, button)  # Dibujar el botón normal
            draw_text(text, font, BLACK, button.centerx, button.centery)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    game_loop()
                elif levels_button.collidepoint(event.pos):
                    level_menu()
                elif options_button.collidepoint(event.pos):
                    options_menu()
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

# Menú de Niveles
def level_menu():
    global current_level
    levels = {
        "Fácil": 5,
        "Medio": 10,
        "Difícil": 15
    }

    while True:
        screen.blit(background_image, (0, 0))  # Dibujar fondo
        draw_text("Selecciona un nivel", font, WHITE, WIDTH // 2, HEIGHT // 4)
        draw_text(f"Nivel seleccionado: {current_level}", font, YELLOW, WIDTH // 2, HEIGHT // 2 - 60)

        # Definir hitboxes para los botones
        button_width, button_height = 200, 50
        easy_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - 30, button_width, button_height)
        medium_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 20, button_width, button_height)
        hard_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 70, button_width, button_height)
        back_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 120, button_width, button_height)

        # Obtener posición del mouse
        mouse_pos = pygame.mouse.get_pos()

        # Resaltar botones si el mouse está sobre ellos
        for button, text in [(easy_button, "Fácil"), (medium_button, "Medio"),
                             (hard_button, "Difícil"), (back_button, "Volver")]:
            if button.collidepoint(mouse_pos):
                pygame.draw.rect(screen, GRAY, button)  # Resaltar el botón
            else:
                pygame.draw.rect(screen, WHITE, button)  # Dibujar el botón normal
            draw_text(text, font, BLACK, button.centerx, button.centery)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    current_level = "Fácil"
                elif medium_button.collidepoint(event.pos):
                    current_level = "Medio"
                elif hard_button.collidepoint(event.pos):
                    current_level = "Difícil"
                elif back_button.collidepoint(event.pos):
                    return

# Menú de Opciones
def options_menu():
    global snake_color
    colors = {
        "Verde": GREEN,
        "Azul": BLUE,
        "Amarillo": YELLOW
    }
    selected_color_name = "Verde"

    while True:
        screen.blit(background_image, (0, 0))  # Dibujar fondo
        draw_text("Opciones", font, WHITE, WIDTH // 2, HEIGHT // 4)
        draw_text(f"Color seleccionado: {selected_color_name}", font, YELLOW, WIDTH // 2, HEIGHT // 2 - 60)

        # Definir hitboxes para los botones
        button_width, button_height = 200, 50
        green_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - 30, button_width, button_height)
        blue_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 20, button_width, button_height)
        yellow_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 70, button_width, button_height)
        back_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 120, button_width, button_height)

        # Obtener posición del mouse
        mouse_pos = pygame.mouse.get_pos()

        # Resaltar botones si el mouse está sobre ellos
        for button, text in [(green_button, "Verde"), (blue_button, "Azul"),
                             (yellow_button, "Amarillo"), (back_button, "Volver")]:
            if button.collidepoint(mouse_pos):
                pygame.draw.rect(screen, GRAY, button)  # Resaltar el botón
            else:
                pygame.draw.rect(screen, WHITE, button)  # Dibujar el botón normal
            draw_text(text, font, BLACK, button.centerx, button.centery)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if green_button.collidepoint(event.pos):
                    snake_color = GREEN
                    selected_color_name = "Verde"
                elif blue_button.collidepoint(event.pos):
                    snake_color = BLUE
                    selected_color_name = "Azul"
                elif yellow_button.collidepoint(event.pos):
                    snake_color = YELLOW
                    selected_color_name = "Amarillo"
                elif back_button.collidepoint(event.pos):
                    return

# Bucle Principal del Juego
def game_loop():
    global current_level
    levels = {
        "Fácil": 5,
        "Medio": 10,
        "Difícil": 15
    }
    speed = levels[current_level]

    while True:
        snake = Snake()
        food = Food()
        score = 0

        while True:
            screen.blit(background_image, (0, 0))  # Dibujar fondo

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and snake.direction != "DOWN":
                        snake.direction = "UP"
                    elif event.key == pygame.K_DOWN and snake.direction != "UP":
                        snake.direction = "DOWN"
                    elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                        snake.direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                        snake.direction = "RIGHT"

            snake.move()

            if snake.eat_food(food.position):
                food = Food()
                score += 10

            if snake.check_collision():
                if game_over(score):  # Si el jugador decide reiniciar
                    break  # Salir del bucle interno para reiniciar el juego

            snake.draw()
            food.draw()

            draw_text(f"Puntuación: {score}", font, WHITE, WIDTH // 2, 20)

            pygame.display.flip()
            clock.tick(speed)

# Pantalla de Game Over
def game_over(score):
    while True:
        screen.fill(BLACK)
        draw_text("Has Perdido", title_font, RED, WIDTH // 2, HEIGHT // 3)
        draw_text(f"Puntuación Final: {score}", font, WHITE, WIDTH // 2, HEIGHT // 2)
        draw_text("Presiona ENTER para reiniciar", font, WHITE, WIDTH // 2, HEIGHT // 2 + 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True  # Indica que se debe reiniciar el juego

# Iniciar el juego
if __name__ == "__main__":
    main_menu()