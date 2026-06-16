import pygame
import sys
import data

class Slider:
    def __init__(self, screen, width, min_value, max_value):
        self.screen = screen
        self.color = (50,50,50)
        self.min_value = min_value
        self.max_value = max_value
        self.inital_value = 60
        self.width = width
        self.height = 10
        self.y = screen.get_height() - self.height - 20
        self.x = screen.get_width() // 2 - self.width // 2
        
    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

