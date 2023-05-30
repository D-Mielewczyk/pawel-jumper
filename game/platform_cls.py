import pygame

from random import randint

from utils import WIDTH, HEIGHT
from object import Object


def width_disc(type):
    switcher = {
        "basic" : int(96),
        "tramp" : int(96),
        "diss"  : int(96),
    }
    return switcher.get(type)

def height_disc(type):
    switcher = {
        "basic" : int(10),
        "tramp" : int(24),
        "diss"  : int(24),
    }
    return switcher.get(type)


def load_platform(self, width, height):
    if self.type == "basic":
        path = "assets\Terrain\Terrain (16x16).png"
        rect = pygame.Rect(272, 16, width, height)
    elif self.type == "tramp":
        path = "assets\Traps\Trampoline\Idle.png"
        rect = pygame.Rect(2, 17, width, height)
    elif self.type == "diss":
        path = "assets\Traps\Platforms\Grey Off.png"
        rect = pygame.Rect(0, 1, width, height)
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
<<<<<<< Updated upstream
    rect = pygame.Rect(272, 0, width, height)
=======
    
>>>>>>> Stashed changes
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


class Platform(Object):
    next_platform_height = HEIGHT - randint(90, 700)

<<<<<<< Updated upstream
    def __init__(self, x, y, width=96, height=10):
        super().__init__(x, y, width, height)
        self.sprite.blit(load_platform(width, height), (0, 0))
=======
    def __init__(self, x, y, diff_level, type, width = 96, height = 10):
        self.type = type
        width = width_disc(type)
        height = height_disc(type)

        super().__init__(x, y, width, height)


        if self.type == "basic":
            scaled_width = max(96 - 8*(diff_level//15), 48)
        else:
            scaled_width = 96
        original_image = load_platform(self, width, height)
        scaled_image = pygame.transform.scale(original_image, (scaled_width*2, height*2))
        self.sprite.blit(scaled_image, (0, 0))
>>>>>>> Stashed changes
        self.mask = pygame.mask.from_surface(self.sprite)

    @staticmethod
    def gen_platforms(min_height, max_height, platforms):
        while Platform.next_platform_height >= max_height:
            platforms.append(
                Platform(
                    randint(0, WIDTH - 96),
                    Platform.next_platform_height,
                )
            )
            Platform.next_platform_height -= randint(0, 625)

        for index, platform in enumerate(platforms):
            if platform.rect.top > min_height:
                platforms.pop(index)
    
    def disappear(platforms, index):
        platforms.pop(index)

    def reset_platform_height():
        Platform.next_platform_height = HEIGHT - randint(90, 700)


# 46 4
