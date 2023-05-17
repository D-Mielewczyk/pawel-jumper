import os
import pygame

from player import Player
from platform import Platform

pygame.init()

WIDTH, HEIGHT = 600, 1100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Paweł Jumper")

FPS = 60
PLAYER_VEL = 5
GRAVITY = 1


def get_background(color):
    image = pygame.image.load(f"assets/Background/{color}")
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            cords = (i * width, j * height)
            tiles.append(cords)

    return tiles, image


def draw_window(window, background, background_image, player, platforms):
    for tile in background:
        window.blit(background_image, tile)

    player.draw(window)

    for p in platforms:
        p.draw(window)

    pygame.display.update()


def handle_movement(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.go_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.go_right(PLAYER_VEL)


def game_loop(window):
    clock = pygame.time.Clock()

    player = Player(100, 100, 50, 50)
    platforms = [Platform(i, 600) for i in range(0, WIDTH+1, 96)]

    background, background_image = get_background("Blue.png")

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        player.loop()
        handle_movement(player)
        draw_window(window, background, background_image, player, platforms)
    pygame.quit()
    quit()


if __name__ == "__main__":
    game_loop(WIN)
