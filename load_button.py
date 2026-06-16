import pygame
import sys

class LoadButton:
    def __init__(self, screen: pygame.Surface, x, y):
        IMAGE_SIZE = 70
        self.screen = screen
        self.x = x
        self.y = y

        self.load_image = pygame.image.load("load.png")
        self.load_image = pygame.transform.scale(self.load_image, (IMAGE_SIZE, IMAGE_SIZE))
        self.rect = self.load_image.get_rect(center=(self.x + 700, self.y + 245))
        
    def draw(self):
        self.screen.blit(self.load_image, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


def load_button():
    screen = pygame.display.set_mode((1300, 680))
    load_button = LoadButton(screen, 400, 400)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if load_button.is_clicked(event.pos):
                    print("Load button clicked!")

        
        
        load_button.draw()
        
        pygame.display.update()


if __name__ == "__main__":
    load_button()