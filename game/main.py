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
DELAY_ANIMATION = 5

def rotate(sprite):
    return pygame.transform.flip(sprite, True, False)

def load_sprites(path, width, height, do_rotate=False):
    path = f"assets/{path}"
    images = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(os.path.join(path, image)).convert_alpha()

        frames = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            frames.append(pygame.transform.scale2x(surface))
        
        if do_rotate:
            sprites[image.replace(".png", "") + "_right"] = frames
            sprites[image.replace(".png", "") + "_left"] = [rotate(f) for f in frames]
        else:
            sprites[image.replace(".png", "")] = sprites

    return sprites



class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None


class Player(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.direction = "right"
        self.animation = 0
        self.fall_count = 0
        self.SPRITES = load_sprites("Main characters/Ninja Frog", 32, 32, True)

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
        index = (self.animation // DELAY_ANIMATION) % len(sprites)

        self.sprite = sprites[index]
        self.animation += 1

    def loop(self):
        # self.y_vel += min(1, (self.fall_count / FPS) * GRAVITY)
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        self.fall_count += 1
        self.set_sprite()


    def draw(self, window):
        window.blit(self.sprite, (self.rect.x, self.rect.y))



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

        player.loop()
        handle_movement(player)
        draw_window(window, background, background_image, player)
    pygame.quit()
    quit()


if __name__ == "__main__":
    game_loop(WIN)
