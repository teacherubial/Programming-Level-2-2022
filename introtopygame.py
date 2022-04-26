# Intro to Pygame

import pygame

pygame.init()

# Constants
BLACK   = (  0,  0,  0)
WHITE   = (255,255,255)
RED     = (255,  0,  0)
GREEN   = (  0,255,  0)
BLUE    = (  0,  0,255)


def main():
    # Create a Window
    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)


if __name__ == "__main__":
    main()
