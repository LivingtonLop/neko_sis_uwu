import pygame
import sys
from src.game import Game

def main():
    # Inicializar Pygame
    pygame.init()

    # Definir dimensiones de la ventana
    WIDTH, HEIGHT = 800, 600
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mi Juego Pygame")

    # Crear instancia del juego
    game = Game(WINDOW)

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar y renderizar el juego
        game.update()
        game.render()

        # Actualizar la pantalla
        pygame.display.flip()

    # Salir de Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
