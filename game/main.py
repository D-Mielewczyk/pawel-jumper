import os
import pygame

pygame.init()
os.chdir('..')

WIDTH, HEIGHT = 600, 1100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Paweł Jumper")

FPS = 60


def get_background(color):
    image = pygame.image.load(f"assets/Background/{color}")
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            cords = (i * width, j * height)
            tiles.append(cords)

    return tiles, image


def draw_window(window, background, background_image):
    for tile in background:
        window.blit(background_image, tile)

    pygame.display.update()


def game_loop(window):
    clock = pygame.time.Clock()

    background, background_image = get_background("Blue.png")

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_r:
            #         # klawisz r cos robi
        draw_window(window, background, background_image)
    pygame.quit()
    quit()


if __name__ == "__main__":
    game_loop(WIN)
