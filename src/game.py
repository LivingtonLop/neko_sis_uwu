import pygame
from src.player import Player
from src.enemy import Enemy
class Game:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        # Inicializar cualquier otro estado del juego, cargar recursos, etc.
        # Por ejemplo:
        self.original_sprite_player = pygame.image.load("assets/images/cat_sis_beta.png")
        self.sprite_player = pygame.transform.scale(self.original_sprite_player, (100,100))
        self.player = Player(velocity=5,x=100,y=600,image=self.sprite_player,sound=None,smarth=False) #bug aparece saltando
        # self.enemy = Enemy()
        self.original_sprite_enemy = pygame.image.load("assets/images/bola_de_pelo_beta_32x32.png")
        self.sprite_enemy = pygame.transform.scale(self.original_sprite_enemy, (50,50))
        self.enemy = Enemy(velocity=5,x=100,y=600,image=self.sprite_enemy,sound=None, smarth=(True,5)) #bug aparece saltando


    def update(self):
        self.player.update(self.window)
        self.enemy.update(self.window)
        
    def render(self):
        
        self.window.fill((255, 255, 255))
        self.window.blit(self.player.image, self.player.rect)
        self.window.blit(self.enemy.image, self.enemy.rect)
        self.clock.tick(30)
        pygame.display.flip()  # Actualizar la pantalla (podría moverse a main.py dependiendo de la estructura del juego)


