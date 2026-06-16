import pygame
import sys

class Clear:
    def __init__(self, screen: pygame.Surface):
        IMAGE_SIZE = 70
        self.screen = screen

        self.clear_image = pygame.image.load("clear.png")
        self.clear_image = pygame.transform.scale(self.clear_image, (IMAGE_SIZE, IMAGE_SIZE))
        self.rect = self.clear_image.get_rect(center=(1250, 645))
        
    def draw(self):
        self.screen.blit(self.clear_image, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


def clear_button():
    screen = pygame.display.set_mode((1300, 680))
    clear_button = Clear(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        
        
        clear_button.draw()
        
        pygame.display.update()


if __name__ == "__main__":
    clear_button()