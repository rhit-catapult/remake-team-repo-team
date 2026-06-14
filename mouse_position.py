import pygame
import sys
import random
import time


class MousePosition:
    def __init__(self, screen):
        self.screen = screen
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]

    def is_clicked(self, mouse_pos):
        if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
            self.x, self.y = mouse_pos
            return True
        return False