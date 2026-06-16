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
        if 505 <= self.y <= 605:
            drum_cell_width = self.screen.get_width() // 16
            drum_x = self.x // drum_cell_width
            if 525 < self.y < 545:
                drum_y = 0
            elif 563 < self.y < 588:
                drum_y = 1
            else:
                drum_y = -1
            
            return self.y, drum_x, drum_y
        else:
            cell_width = self.screen.get_width() // 16  # Assuming 16 columns
            cell_height = 505 // 8   # Assuming 8 rows
            grid_x = self.x // cell_width
            grid_y = self.y // cell_height
            return self.y, grid_x, grid_y
