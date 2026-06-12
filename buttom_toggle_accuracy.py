import pygame
import sys
import random
import time


class Button:
    def __init__(self, screen, x, y, width, height, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.original_color = color
        self.pressed_color = (255, 0, 0)
        self.is_pressed = False

    def draw(self):
        # Draw the button rectangle
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def is_clicked(self, mouse_pos):
        return (self.x <= mouse_pos[0] <= self.x + self.width and
                self.y <= mouse_pos[1] <= self.y + self.height)
    
def main():
    pygame.init()
    pygame.display.set_caption("Button Example")
    screen = pygame.display.set_mode((640, 480))

    button = Button(screen, 0, 0, 50, 50, (0, 0, 255))
    button.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.is_clicked(event.pos):
                    button.is_pressed = not button.is_pressed
                    button.color = button.pressed_color if button.is_pressed else button.original_color


        screen.fill((255, 255, 255))  # Fill background with white
        button.draw()
        pygame.display.update()


main()
