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
        keyboard = pygame.key.get_pressed()
        
        if keyboard[pygame.K_LEFT]:
            self.player.move(-self.player.velocity, 0,window=self.window)
        if keyboard[pygame.K_RIGHT]:
            self.player.move(self.player.velocity, 0,window=self.window)
        if keyboard[pygame.K_DOWN]:
            self.player.move(0, self.player.velocity,window=self.window)
        if keyboard[pygame.K_SPACE] and self.player.on_floor:
            self.player.jump_bool = True
            self.player.on_floor = False

        self.gravity_y+=1

        if self.player.jump_bool:
            self.gravity_y=-self.player.jump_force
            self.player.jump_bool = False
        
        if self.player.rect.y >= self.window.get_height() - self.player.image.get_height():
            self.player.on_floor = True

        self.player.move(0, -self.player.jump_force + self.gravity_y,window=self.window)
        # self.enemy.update()
        
    def render(self):
        
        self.window.fill((255, 255, 255))
        self.window.blit(self.player.image, self.player.rect)
        # self.window.blit(self.enemy.image, self.enemy.rect)
        self.clock.tick(30)
        pygame.display.flip()  # Actualizar la pantalla (podría moverse a main.py dependiendo de la estructura del juego)


