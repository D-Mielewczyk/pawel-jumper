import pygame
import os

from random import randint

from utils import load_sprites, WIDTH, HEIGHT
from object import Object


def get_random_platform_type(diff_level):
    roll = randint(min(diff_level, 50), 100)
    if diff_level == 0 or roll < 60:
        return "basic"
    elif roll < 90:
        return "tramp"
    else:
        return "diss"


def load_platform(self, width, height):
    if self.type == "basic":
        path = os.path.join("assets", "Terrain", "Terrain (16x16).png")
        rect = pygame.Rect(272, 16, width, height)
    elif self.type == "tramp":
        path = "assets\Traps\Trampoline\Idle.png"
        path = os.path.join("assets", "Traps", "Trampoline", "Idle.png")
        rect = pygame.Rect(2, 17, width, height)
    elif self.type == "diss":
        path = os.path.join("assets", "Terrain", "Terrain (16x16).png")
        rect = pygame.Rect(272, 0, width, height)
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


class Platform(Object):
    next_platform_height = HEIGHT - randint(90, 500)
    width = 96
    TRAMP_SPRITE = load_sprites(os.path.join("Traps", "Trampoline"), 28, 28)
    DELAY_ANIMATION = 3
    heights = {
        "basic": 10,
        "tramp": 24,
        "diss": 10,
    }
    widths = {
        "basic": 96,
        "tramp": 96,
        "diss": 96,
    }

    def __init__(self, x, y, diff_level, type="basic", width=96, height=10):
        super().__init__(x, y, width, height)

        self.type = type
        width = Platform.widths[type]
        height = Platform.heights[type]
        self.animation = 0

        scaled_width = width
        if self.type == "basic":
            scaled_width = max(96 - diff_level, 48)

        original_image = load_platform(self, width, height)
        scaled_image = pygame.transform.scale(
            original_image, (scaled_width * 2, height * 2)
        )
        self.sprite.blit(scaled_image, (0, 0))
        self.mask = pygame.mask.from_surface(self.sprite)

    @staticmethod
    def gen_platforms(min_height, max_height, platforms, diff_level):
        while Platform.next_platform_height >= max_height:
            platforms.append(
                Platform(
                    randint(0, WIDTH - 96),
                    Platform.next_platform_height,
                    diff_level,
                    get_random_platform_type(diff_level),
                )
            )
            Platform.next_platform_height -= randint(min(0 + diff_level * 7, 500), 625)

        for index, platform in enumerate(platforms):
            if platform.rect.top > min_height:
                platforms.pop(index)

    def reset_platform_height():
        Platform.next_platform_height = HEIGHT - randint(90, 700)

    def disappear(platforms, index):
        platforms.pop(index)
