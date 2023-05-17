import pygame

from object import Object
from utils import load_sprites


class Player(Object):
    SPRITES = load_sprites("Main characters/Ninja Frog", 32, 32, True)
    DELAY_ANIMATION = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.direction = "right"
        self.animation = 0
        self.fall_count = 0
        self.mask = None

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

    def set_sprite(self):
        sprite = "Idle (32x32)"
        if self.x_vel != 0:
            sprite = "Run (32x32)"

        sprite_name = f"{sprite}_{self.direction}"
        sprites = self.SPRITES[sprite_name]
        index = (self.animation // self.DELAY_ANIMATION) % len(sprites)

        self.sprite = sprites[index]
        self.animation += 1

    def loop(self):
        # self.y_vel += min(1, (self.fall_count / FPS) * GRAVITY)
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        self.fall_count += 1
        self.set_sprite()
        self.update_mask()

    def update_mask(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, window):
        window.blit(self.sprite, (self.rect.x, self.rect.y))
