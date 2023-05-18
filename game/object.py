import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.sprite = pygame.Surface((width, height), pygame.SRCALPHA)

    def draw(self, window, offset_y):
        window.blit(self.sprite, (self.rect.x, self.rect.y - offset_y))
