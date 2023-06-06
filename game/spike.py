import pygame
import os

from object import Object

def get_spike():
    path = os.path.join("assets", "Traps", "Spikes", "Idle.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((7, 7), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 9, 7, 7)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

class Spike(Object):
    def __init__(self, x, y):
        super().__init__(x, y, 14, 14)
        self.sprite.blit(get_spike(), (0, 0))
        self.mask = pygame.mask.from_surface(self.sprite)
