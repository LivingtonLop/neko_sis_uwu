import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# Definir los colores
BLANCO = (255, 255, 255)

# Definir las propiedades del personaje
x_personaje = 50
y_personaje = ALTO - 100
ancho_personaje = 50
alto_personaje = 50
velocidad_y = 0
salto = False
fuerza_salto = 10

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                salto = True

    # Aplicar la gravedad
    velocidad_y += 1

    # Aplicar el salto
    if salto:
        velocidad_y = -fuerza_salto
        salto = False

    # Mover el personaje
    y_personaje += velocidad_y

    # Limitar el movimiento del personaje para que no se salga de la pantalla
    y_personaje = max(0, min(y_personaje, ALTO - alto_personaje))

    # Limpiar la pantalla
    pantalla.fill(BLANCO)

    # Dibujar el personaje
    pygame.draw.rect(pantalla, (0, 0, 0), (x_personaje, y_personaje, ancho_personaje, alto_personaje))

    # Actualizar la pantalla
    pygame.display.flip()

    # Esperar un poco para ajustar la velocidad del juego
    pygame.time.Clock().tick(30)

# Salir de Pygame
pygame.quit()
