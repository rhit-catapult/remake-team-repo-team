import pygame
import sys


class Button:
    def __init__(self, screen: pygame.Surface, x, y):
        IMAGE_SIZE = 90
        self.screen = screen
        self.x = x
        self.y = y
        self.color = pygame.image.load("play.png")
        self.color = pygame.transform.scale(self.color, (IMAGE_SIZE, IMAGE_SIZE))
        self.base_color = pygame.image.load("play.png")
        self.base_color = pygame.transform.scale(self.base_color, (IMAGE_SIZE, IMAGE_SIZE))
        self.active_color = pygame.image.load("pause.png")
        self.active_color = pygame.transform.scale(self.active_color, (IMAGE_SIZE, IMAGE_SIZE))
        self.pressed = False
        self.rect = self.color.get_rect(center=(self.x - 340, self.y + 220))

    def draw(self):
        self.screen.blit(self.color, self.rect)
        

    def toggle(self):
        self.pressed = not self.pressed
        # self.color = self.active_colour if self.pressed else self.base_color
        if self.pressed:
            self.color = self.active_color
        else:
            self.color = self.base_color
        self.rect = self.color.get_rect(center=(self.x - 340, self.y + 220))
        



def play_button():
    screen = pygame.display.set_mode((1300, 680))
    play_button = Button(screen, 400, 400)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.rect.collidepoint(event.pos):
                    play_button.toggle()
        
        play_button.draw()
        
        pygame.display.update()


if __name__ == "__main__":
    play_button()
