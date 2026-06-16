import pygame
import sys

class SplashScreen:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("splash_screen.png") # add image path of splash screen here (need to be the same aspect as the screen ratio)
        self.x = 0 # half of screen's x
        self.y = 0 # half of screen's y
        # scale the drawing

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    # click anywhere on the screen to close it?
