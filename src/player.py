from src.class_abstrac.entitys import Entitys

class Player (Entitys):
    def __init__(self,velocity: int, x, y, image, sound=None):
        super().__init__(velocity,x, y, image, sound)

    def update(self, surface):
        return super().update(surface)
    
    def draw(self, surface,coord = None):
        return super().draw(surface, coord)
    
    def play_sound(self):
        return super().play_sound()
    
    def set_hitbox(self, x, y, width, height):
        return super().set_hitbox(x, y, width, height)