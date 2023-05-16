import os
import pygame

pygame.init()
os.chdir('..')

WIDTH, HEIGHT = 600, 1100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Paweł Jumper")

FPS = 60
PLAYER_VEL = 5
GRAVITY = 1


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None


class Player(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.direction = None
        self.animation = 0
        self.fall_count = 0

    def go_left(self, velocity):
        self.x_vel = -velocity
        if self.direction != "left":
            self.direction == "left"
            self.animation = 0

    def go_right(self, velocity):
        self.x_vel = velocity
        if self.direction != "right":
            self.direction == "right"
            self.animation = 0

    def loop(self):
        self.y_vel += min(1, (self.fall_count / FPS) * GRAVITY)
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        self.fall_count += 1


    def draw(self, window):
        pygame.draw.rect(window, (10, 100, 200), self.rect)



def get_background(color):
    image = pygame.image.load(f"assets/Background/{color}")
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            cords = (i * width, j * height)
            tiles.append(cords)

    return tiles, image


def draw_window(window, background, background_image, player):
    for tile in background:
        window.blit(background_image, tile)

    player.draw(window)

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
        player.loop()
        handle_movement(player)
        draw_window(window, background, background_image, player)
    pygame.quit()
    quit()


if __name__ == "__main__":
    game_loop(WIN)
