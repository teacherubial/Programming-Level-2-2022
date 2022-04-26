# Intro to Pygame

import pygame

pygame.init()

# Constants
BLACK   = (  0,  0,  0)
WHITE   = (255,255,255)
RED     = (255,  0,  0)
GREEN   = (  0,255,  0)
BLUE    = (  0,  0,255)

WINDOW_TITLE = "Pygame Introduction"


def main():
    # Create a Window
    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)

    # Set the title of the window
    pygame.display.set_caption(WINDOW_TITLE)

    done = False

    clock = pygame.time.Clock()

    # ------ MAIN PROGRAM LOOP ------
    while not done:
        # ---- Event Handler
        for event in pygame.event.get():      # list of events
            if event.type == pygame.QUIT:
                # When user clicks the red quit button
                done = True

        # ---- Environment Logic

        # ---- Render the Environment
        # Fill screen with background colour
        screen.fill(WHITE)

        # Draw a rectangle
        # rect -> [x, y, width, height]
        pygame.draw.rect(screen, GREEN, [0,   0, 400, 200])
        pygame.draw.rect(screen, RED,   [30, 30, 400, 200])

        # Draw a line
        pygame.draw.line(screen, BLACK, (0, 0), screen_size)

        # Draw a series of lines
        # range(start, stop, step) ->
        for delta_y in range(30, 231, 10):
            pygame.draw.line(screen, BLUE, (0, 10+delta_y), (100, 100+delta_y))


        # ----     Flip the display
        # Updates the screen with what we've drawn
        pygame.display.flip()

        # ---- Tick the clock
        clock.tick(75)


if __name__ == "__main__":
    main()
