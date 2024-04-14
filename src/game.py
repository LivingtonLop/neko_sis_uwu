import pygame
from src.player import Player
class Game:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        self.gravity_y = 0
        # Inicializar cualquier otro estado del juego, cargar recursos, etc.
        # Por ejemplo:
        self.original_sprite_player = pygame.image.load("assets/images/cat_sis_beta.png")
        self.sprite_player = pygame.transform.scale(self.original_sprite_player, (100,100))
        self.player = Player(velocity=5,x=100,y=100,image=self.sprite_player,sound=None)
        # self.enemy = Enemy()

    def update(self):
        #Up gravity on y
        #keyboard
        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_LEFT]:
            self.player.move(-self.player.velocity, 0,window=self.window)
        if keyboard[pygame.K_RIGHT]:
            self.player.move(self.player.velocity, 0,window=self.window)
        # if keyboard[pygame.K_UP]:
        if keyboard[pygame.K_DOWN]:
            self.player.move(0, self.player.velocity,window=self.window)

        if keyboard[pygame.K_SPACE]:
            self.player.jump_bool = True

        self.gravity_y+=1

        if self.player.jump_bool:
            self.gravity_y=-self.player.jump_force
            self.player.jump_bool = False
        
        self.player.move(0, -self.player.jump_force + self.gravity_y,window=self.window)
        

        self.player.draw(self.window)
        # self.enemy.update()
        
    def render(self):
        # Renderizar los elementos del juego en la ventana
        # Por ejemplo:
        self.window.fill((255, 255, 255))  # Llenar la ventana de blanco
        self.window.blit(self.player.image, self.player.rect)
        # self.window.blit(self.enemy.image, self.enemy.rect)
        pygame.display.flip()  # Actualizar la pantalla (podría moverse a main.py dependiendo de la estructura del juego)

    # Agregar más métodos según sea necesario para la lógica del juego

