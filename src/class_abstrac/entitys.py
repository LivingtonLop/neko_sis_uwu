from abc import ABC, abstractmethod

class Entitys(ABC):
    def __init__(self, x, y, image, sound=None):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sound = sound

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

    