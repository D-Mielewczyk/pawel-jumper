import pygame
import os

from player import Player
from platform_cls import Platform
from utils import FPS, WIDTH, HEIGHT, GAME_FONT_BIG, GAME_FONT_SMALL
from score import Score
from spike import Spike

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Paweł Jumper")

PLAYER_VEL = 9
SCROLL_AREA_HEIGHT = 300


def get_background(color):
    image = pygame.image.load(os.path.join("assets", "Background", color))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            cords = (i * width, j * height)
            tiles.append(cords)

    return tiles, image


def draw_window(
    window, background, background_image, offset_y, player, score, *objects
):
    for tile in background:
        window.blit(background_image, tile)

    for obj in objects:
        obj.draw(window, offset_y)

    score.draw(window)
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


def handle_camera(player, offset_y, platforms, diff_level, platform_type):
    if player.rect.top <= SCROLL_AREA_HEIGHT + offset_y and player.y_vel < 0:
        offset_y += player.y_vel
        player.dead_height += player.y_vel
    Platform.gen_platforms(
        player.dead_height, offset_y, platforms, diff_level, platform_type
    )
    return offset_y


def game_over(window, score):
    score.load_best_score()

    # Draw texts
    if score.new_best_score_flag == True:
        text = GAME_FONT_BIG.render(
            "New best score: " + str(int(score.best_score)), True, (200, 0, 0)
        )
    else:
        text = GAME_FONT_SMALL.render(
            "Best score: " + str(int(score.best_score)), True, (0, 0, 0)
        )
    text_rect = text.get_rect(center=(WIDTH / 2, 110))
    window.blit(text, text_rect)

    text = GAME_FONT_BIG.render("GAME OVER", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 3))
    window.blit(text, text_rect)
    text = GAME_FONT_SMALL.render("Press 'space' to play again", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 3 + 50))
    window.blit(text, text_rect)
    text = GAME_FONT_SMALL.render("'x' to exit", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 3 + 80))
    window.blit(text, text_rect)
    pygame.display.update()
    # Draw texts

    exit_game = False
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    exit_game = True
                    break
                if event.key == pygame.K_SPACE:
                    game_loop(window)


def check_loose(player):
    return player.rect.top >= player.dead_height


def game_loop(window):
    clock = pygame.time.Clock()

    score = Score()

    offset_y = 0
    Platform.reset_platform_height()
    player = Player(100, 900, 50, 50)

    pygame.display.set_icon(player.SPRITES["Idle (32x32)_right"][0])

    platforms = [
        Platform(i, HEIGHT - 75, score.current_score, "basic")
        for i in range(0, WIDTH, 96)
    ]  # generate floor
    Platform.gen_platforms(
        player.dead_height, offset_y, platforms, score.current_score, "basic"
    )

    background, background_image = get_background("Blue.png")

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
        draw_window(
            window,
            background,
            background_image,
            offset_y,
            player,
            score,
            *platforms,
            *spikes
        )

        offset_y = handle_camera(
            player, offset_y, platforms, score.current_score, "basic"
        )

        score.update_current_score(-offset_y)

        if check_loose(player):
            run = False
            break

    game_over(window, score)

    pygame.quit()
    quit()


if __name__ == "__main__":
    game_loop(WIN)
