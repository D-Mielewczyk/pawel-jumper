import pygame
import os

from random import choice

pygame.mixer.init()


class Sound:
    def __init__(self):
        base_path = os.path.join("assets", "Sound")
        self.landing = pygame.mixer.Sound(os.path.join(base_path, "jumpland.wav"))

        os.chdir(os.path.join(base_path, "Jumps"))
        self.jumps = [pygame.mixer.Sound(f) for f in os.listdir() if os.path.isfile(f)]
        os.chdir('../../../')

    def jump(self):
        choice(self.jumps).play(0)

