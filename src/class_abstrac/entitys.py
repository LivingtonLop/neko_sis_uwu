import pygame
from abc import ABC, abstractmethod

class Entitys(ABC):
    def __init__(self, velocity :int, smarth: dict|bool , x, y, image, sound=None):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sound = sound
        self.velocity = velocity
        self.on_floor = True
        self.jump_bool = False
        self.jump_force = velocity * 2 #parano hacer tantas variables
        self.gravity_y = 0
        self.smarth = smarth

    @abstractmethod
    def update(self, surface):
        if not self.smarth:
            keyboard = pygame.key.get_pressed()
            
            if keyboard[pygame.K_LEFT]:
                self.move(-self.velocity, 0,window=surface)
            if keyboard[pygame.K_RIGHT]:
                self.move(self.velocity, 0,window=surface)
            if keyboard[pygame.K_DOWN]:
                self.move(0, self.velocity,window=surface)
            if keyboard[pygame.K_SPACE] and self.on_floor:
                self.jump_bool = True
                self.on_floor = False

            self.gravity_y+=1

            if self.jump_bool:
                self.gravity_y=-self.jump_force
                self.jump_bool = False
            
            if self.rect.y >= surface.get_height() - self.image.get_height():
                self.on_floor = True

            self.move(0, -self.jump_force + self.gravity_y,window=surface)

    @abstractmethod
    def draw(self, surface, coord = None):
        if coord != None: surface.blit(self.image, coord)
        else: surface.blit(self.image, self.rect)

    @abstractmethod
    def play_sound(self):
        if self.sound:
            self.sound.play()
    
    @abstractmethod
    def set_hitbox(self, x, y, width, height):
        # Modificar las dimensiones y la posición de la hitbox
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height

    def move (self, x :int, y :int, window): #limited ()
        self.rect.x += x
        self.rect.y += y
        self.rect.x = max(0, min(self.rect.x, window.get_width() - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, window.get_height() - self.rect.height))
