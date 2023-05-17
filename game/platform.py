import pygame
import os

from object import Object

def load_platform(width, height):
    path = "assets\Terrain\Terrain (16x16).png"
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 0, width, height)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)

class Platform(Object):
    def __init__(self, x, y, width=96, height=10):
        super().__init__(x, y, width, height)
        self.sprite.blit(load_platform(width, height), (0, 0))
        self.mask = pygame.mask.from_surface(self.sprite)

# 46 4