import pygame
from src.player import Player
class Game:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        # Inicializar cualquier otro estado del juego, cargar recursos, etc.
        # Por ejemplo:
        self.original_sprite_player = pygame.image.load("assets/images/cat_sis_beta.png")
        self.sprite_player = pygame.transform.scale(self.original_sprite_player, (100,100))
        self.player = Player(velocity=5,x=100,y=100,image=self.sprite_player,sound=None)
        # self.enemy = Enemy()

    def update(self):
        self.player.update(self.window)
        # self.enemy.update()
        
    def render(self):
        
        self.window.fill((255, 255, 255))
        self.window.blit(self.player.image, self.player.rect)
        # self.window.blit(self.enemy.image, self.enemy.rect)
        self.clock.tick(30)
        pygame.display.flip()  # Actualizar la pantalla (podría moverse a main.py dependiendo de la estructura del juego)


