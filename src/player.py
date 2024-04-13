from src.class_abstrac.entitys import Entitys

class Player (Entitys):
    def __init__(self, x, y, image, sound=None):
        super().__init__(x, y, image, sound)

    def update(self):
        return super().update()
    
    def draw(self, surface):
        return super().draw(surface)
    
    def play_sound(self):
        return super().play_sound()
    
    def set_hitbox(self, x, y, width, height):
        return super().set_hitbox(x, y, width, height)