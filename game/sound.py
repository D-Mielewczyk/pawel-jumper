import pygame
import os

from random import choice


class Sound:
    def __init__(self):
        base_path = os.path.join("assets", "Sound")
        self.landing = pygame.mixer.Sound(os.path.join(base_path, "jumpland.wav"))

        os.chdir(os.path.join(base_path, "Jumps"))
        self.jumps = [pygame.mixer.Sound(f) for f in os.listdir() if os.path.isfile(f)]
        os.chdir("../../../")
        self.tramp_jump = pygame.mixer.Sound(
            os.path.join(base_path, "SFX_Jump_tramp.wav")
        )

    def jump(self):
        choice(self.jumps).play(0)

    def tramp(self):
        self.tramp_jump.play(0)
