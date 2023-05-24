import pygame
import os

from object import Object
from utils import load_sprites, FPS, GRAVITY, HEIGHT


class Player(Object):
    SPRITES = load_sprites(os.path.join('Main characters', 'Ninja Frog'), 32, 32, True)
    DELAY_ANIMATION = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.direction = "right"
        self.animation = 0
        self.fall_count = 0
        self.mask = None
        self.jumps = 0
        self.dead_height = HEIGHT

    def go_left(self, velocity):
        self.x_vel = -velocity
        if self.direction != "left":
            self.direction = "left"
            self.animation = 0

    def go_right(self, velocity):
        self.x_vel = velocity
        if self.direction != "right":
            self.direction = "right"
            self.animation = 0

    def jump(self):
        self.y_vel = -GRAVITY * 12
        self.animation_count = 0
        self.jumps += 1
        if self.jumps == 1:
            self.fall_count = 0
        elif self.jumps == 2:
            self.y_vel = -GRAVITY * 20

    def set_sprite(self):
        sprite = "Idle (32x32)"
        if self.y_vel < 0:
            if self.jumps == 1:
                sprite = "Jump (32x32)"
            elif self.jumps == 2:
                sprite = "Double Jump (32x32)"
        elif self.y_vel > 0:
            sprite = "Fall (32x32)"
        elif self.x_vel != 0:
            sprite = "Run (32x32)"

        sprite_name = f"{sprite}_{self.direction}"
        sprites = self.SPRITES[sprite_name]
        index = (self.animation // self.DELAY_ANIMATION) % len(sprites)

        self.sprite = sprites[index]
        self.animation += 1

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jumps = 0
        self.jump()

    def loop(self):
        self.y_vel += min(1, (self.fall_count / FPS) * GRAVITY)
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        self.fall_count += 1
        self.set_sprite()
        self.update_mask()

    def update_mask(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)
