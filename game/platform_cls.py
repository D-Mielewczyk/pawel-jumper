import pygame
import os

from random import randint

from utils import WIDTH, HEIGHT
from object import Object


def load_platform(width, height):
    path = os.path.join("assets", "Terrain", "Terrain (16x16).png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    rect = pygame.Rect(272, 16, width, height)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


class Platform(Object):
    next_platform_height = HEIGHT - randint(90, 700)
    width = 96

    def __init__(self, x, y, diff_level, type, width=96, height=10):
        super().__init__(x, y, width, height)
        self.type = type

        if self.type == "basic":
            scaled_width = max(96 - 8 * (diff_level // 15), 48)
        else:
            scaled_width = 96
        original_image = load_platform(width, height)
        scaled_image = pygame.transform.scale(original_image, (scaled_width * 2, height * 2))
        self.sprite.blit(scaled_image, (0, 0))
        self.mask = pygame.mask.from_surface(self.sprite)

    @staticmethod
    def gen_platforms(min_height, max_height, platforms, diff_level, type):
        while Platform.next_platform_height >= max_height:
            platforms.append(
                Platform(randint(0, WIDTH - 96), Platform.next_platform_height, diff_level, type)
            )
            Platform.next_platform_height -= randint(min(0 + diff_level * 7, 500), 625)

        for index, platform in enumerate(platforms):
            if platform.rect.top > min_height:
                platforms.pop(index)

    def reset_platform_height():
        Platform.next_platform_height = HEIGHT - randint(90, 700)


# 46 4
