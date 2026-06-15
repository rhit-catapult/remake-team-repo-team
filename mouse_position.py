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
    
    def find_grid_position(self):
        cell_width = self.screen.get_width() // 16  # Assuming 16 columns
        cell_height = self.screen.get_height() // 8   # Assuming 8 rows
        grid_x = self.x // cell_width
        grid_y = self.y // cell_height
        return grid_x, grid_y