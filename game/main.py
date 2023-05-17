import os
import pygame

from player import Player
from platform import Platform
from utils import FPS, GRAVITY

pygame.init()

WIDTH, HEIGHT = 600, 1100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Paweł Jumper")

PLAYER_VEL = 5
SCROLL_AREA_HEIGHT = 200



def get_background(color):
    image = pygame.image.load(f"assets/Background/{color}")
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            cords = (i * width, j * height)
            tiles.append(cords)

    return tiles, image


def draw_window(window, background, background_image, offset_y, player, *objects):
    for tile in background:
        window.blit(background_image, tile)

    for obj in objects:
        obj.draw(window, offset_y)

    # Allways draw player last so he is on top
    player.draw(window, offset_y)

    pygame.display.update()

def handle_vert_collision(player, *objects):
    collided = [obj for obj in objects if pygame.sprite.collide_mask(player, obj)]

    for obj in collided:
        if player.y_vel > 0:
            player.rect.bottom = obj.rect.top
            player.landed()

    return collided


def handle_movement(player, *objects):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.go_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.go_right(PLAYER_VEL)

    handle_vert_collision(player, *objects)

def handle_camera(player, offset_y):
    if (player.rect.top + offset_y <= SCROLL_AREA_HEIGHT and player.y_vel < 0):
            offset_y += player.y_vel
    return offset_y


def game_loop(window):
    clock = pygame.time.Clock()

    player = Player(100, 100, 50, 50)
    platforms = [Platform(i, HEIGHT - 75) for i in range(0, WIDTH + 1, 96)] + [Platform(200, 400), Platform(400, 200)]

    background, background_image = get_background("Blue.png")

    offset_y = 0

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player.jumps < 2:
                    player.jump()

        player.loop()
        handle_movement(player, *platforms)
        draw_window(window, background, background_image, offset_y, player, *platforms)

        offset_y = handle_camera(player, offset_y)


    pygame.quit()
    quit()


if __name__ == "__main__":
    game_loop(WIN)
