# introtocollision.py

import random
import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Intro to Collision"


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        self.image = pygame.image.load("./assets/mario.png")
        self.image = pygame.transform.scale(self.image, (38, 38))   # scale
        # self.image.set_colorkey((WHITE))      # set transparency

        # Rect
        self.rect = self.image.get_rect()

    def update(self):
        """Follow the mouse"""
        self.rect.center = pygame.mouse.get_pos()


class Treasure(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        self.image = pygame.image.load("./assets/coin.png")

        # Rect
        self.rect = self.image.get_rect()
        self.rect.center = random_coords()      # random location


def random_coords() -> list:
    """Returns a random x, y coord between
    0 to WIDTH and 0 to HEIGHT respectively"""
    return random.randrange(0, WIDTH), random.randrange(0, HEIGHT)


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    pygame.mouse.set_visible(False)     # make cursor invisible

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    num_treasure = 10
    score = 0
    default_font = pygame.font.SysFont("Menlo", 20)

    coin_sound = pygame.mixer.Sound("./assets/coinsound.ogg")

    # Create sprite groups
    all_sprites_group = pygame.sprite.Group()
    treasure_sprites_group = pygame.sprite.Group()

    # Create sprites to fill groups
    # Create treasure sprites
    for i in range(num_treasure):
        treasure = Treasure()

        # Add it to BOTH lists: all_sprites_group and treasure_sprites_group
        all_sprites_group.add(treasure)
        treasure_sprites_group.add(treasure)

    player = Player()
    all_sprites_group.add(player)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprites_group.update()

        # Deal with collision between player and treasure sprites
        #  PLAYER collides with any sprite from TREASURE_SPRITE_GROUP
        collided_treasure = pygame.sprite.spritecollide(
            player,
            treasure_sprites_group,
            dokill=True
        )

        if len(collided_treasure) > 0:
            # coin_sound.play()
            pass

        # Iterate through all collided treasure
        for treasure in collided_treasure:
            print(f"x: {treasure.rect.x}")
            print(f"y: {treasure.rect.y}")

            # Replace the treasure
            treasure = Treasure()
            all_sprites_group.add(treasure)
            treasure_sprites_group.add(treasure)

            # Increase score
            score += 1

        # ----- RENDER
        screen.fill(BLACK)
        all_sprites_group.draw(screen)

        # Render score
        score_surf = default_font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surf, (10, 10))

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()