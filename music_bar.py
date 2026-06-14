
import pygame

from play_button import play_button



class bar:
    def __init__(self, screen, speed):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.width = 80 # need to change this to the width of a cell
        self.height = 400 # need to change this to the height of player
        self.color = (0,0,0) # opacity?
        self.speed = speed # tempo

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    def update_position(self, speed=None):
        self.x += self.speed