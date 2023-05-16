import pygame

WIDTH, HEIGHT = 600, 1100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Paweł Jumper")

FPS = 60


def draw_window():
    WIN.fill((52, 91, 235))
    pygame.display.update()


def game_loop():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_r:
            #         # klawisz r cos robi
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    game_loop()
