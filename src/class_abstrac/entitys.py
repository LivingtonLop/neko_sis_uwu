from abc import ABC, abstractmethod

class Entitys(ABC):
    def __init__(self, velocity :int, x, y, image, sound=None):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sound = sound
        self.velocity = velocity
        self.jump_bool = False
        self.jump_force = velocity * 2 #parano hacer tantas variables

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, surface):
        surface.blit(self.image, self.rect)

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

    def jump (self,y):
        
        self.rect.y = max(0,min(y,100))
