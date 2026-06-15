import pygame
import sys

class Slider:
    def __init__(self, x, y, width, min_value, max_value, initial_value):
        self.rect = pygame.Rect(x, y, width, 10)
        self.min_value = min_value
        self.max_value = max_value
        