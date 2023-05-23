import os
import pygame

pygame.init()


os.chdir("..")

WIDTH, HEIGHT = 600, 1000
FPS = 60
GRAVITY = 1

FONT_NAME = "assets/04B_30__.TTF"
GAME_FONT_BIG = pygame.font.Font(FONT_NAME, 40)
GAME_FONT_SMALL = pygame.font.Font(FONT_NAME, 24)

# We need to mock window here so .convert_alpha() works
pygame.display.set_mode((1000, 1000))


def rotate(sprite):
    return pygame.transform.flip(sprite, True, False)


def load_sprites(path, width, height, do_rotate=False):
    path = f"assets/{path}"
    images = [
        f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))
    ]

    sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(
            os.path.join(path, image)
        ).convert_alpha()

        frames = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            frames.append(pygame.transform.scale2x(surface))

        if do_rotate:
            sprites[image.replace(".png", "") + "_right"] = frames
            sprites[image.replace(".png", "") + "_left"] = [
                rotate(f) for f in frames
            ]
        else:
            sprites[image.replace(".png", "")] = sprites

    return sprites
