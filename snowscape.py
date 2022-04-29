# snowscape.py

import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Snowscape"


class Snow(pygame.sprite.Sprite):
    def __init__(self, width: int):
        """
        :param width: width of snow in px
        """
        super().__init__()

        self.image = pygame.Surface([width, width])
        # fill that image with an actual shape
        pygame.draw.circle(
            self.image,
            WHITE,
            (width // 2, width // 2),  # draw in the middle
            width // 2
        )

        self.rect = self.image.get_rect()


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # Create a new snow object
    snow = Snow(10)
    # TODO: Test
    snow.rect.center = (WIDTH // 2, HEIGHT // 2)

    # Create a snow sprites group
    snow_sprites = pygame.sprite.Group()

    # Add the snow object to the snow sprites group
    snow_sprites.add(snow)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC

        # ----- RENDER
        screen.fill(BLACK)

        # Draw all the sprite groups
        snow_sprites.draw(screen)

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()