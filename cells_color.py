import pygame

class Cells:
    def __init__(self, screen, x, y, color=(255, 255, 255)):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
      pygame.draw.rect(self.screen, self.color, (self.x, self.y, 60, 30))
    def update_color(self):
        pos = pygame.mouse.get_pos()
        if pos[1] < self.screen.get_height() / 8 and pos[1] > 0:
            self.color = (250, 0, 0)
        elif pos[1] < self.screen.get_height() * 2 / 8 and pos[1] > self.screen.get_height() / 8:
            self.color = (0, 250, 0)
        elif pos[1] < self.screen.get_height() * 3 / 8 and pos[1] > self.screen.get_height () * 2 / 8:
            self.color = (0, 0, 250)
        elif pos[1] < self.screen.get_height() * 4 / 8 and pos[1] > self.screen.get_height() * 3 / 8:
            self.color = (250, 250, 0)
        elif pos[1] < self.screen.get_height() * 5 / 8 and pos[1] > self.screen.get_height() * 4 / 8:
            self.color = (0, 250, 250)
        elif pos[1] < self.screen.get_height() * 6 / 8 and pos[1] > self.screen.get_height() * 5 / 8:
            self.color = (250, 0, 250)
        elif pos[1] < self.screen.get_height() * 7 / 8 and pos[1] > self.screen.get_height() * 6 / 8:
            self.color = (250, 125, 125)
        elif pos[1] < self.screen.get_height() and pos[1] > self.screen.get_height() * 7 / 8:
            self.color = (125, 125, 255)
        else:
            self.color = (255, 255, 255)