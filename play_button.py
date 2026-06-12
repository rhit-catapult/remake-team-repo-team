import pygame
import sys


class Button:
    def __init__(self, screen: pygame.Surface, x, y, color, active_colour):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.base_color = color
        self.active_colour = active_colour
        self.pressed = False
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x - 350, self.y + 50), 20)

    def toggle(self):
        self.pressed = not self.pressed
        # self.color = self.active_colour if self.pressed else self.base_color
        if self.pressed:
            self.color = self.active_colour
        else:
            self.color = self.base_color
        



def play_button():
    screen = pygame.display.set_mode((800, 500))
    play_button = Button(screen, 400, 400, "gray", "red")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                distance = ((mouse_pos[0] - (play_button.x - 350)) ** 2 + (mouse_pos[1] - (play_button.y + 50)) ** 2) ** 0.5
                if distance <= 20:
                    play_button.toggle()
        play_button.draw()
        
        pygame.display.update()


if __name__ == "__main__":
    play_button()
