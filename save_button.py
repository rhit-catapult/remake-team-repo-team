import pygame
import sys

class SaveButton:
    def __init__(self, screen: pygame.Surface):
        IMAGE_SIZE = 70
        self.screen = screen

        self.save_image = pygame.image.load("save.png")
        self.save_image = pygame.transform.scale(self.save_image, (IMAGE_SIZE, IMAGE_SIZE))
        self.rect = self.save_image.get_rect(center=(1175, 645))
        
    def draw(self):
        self.screen.blit(self.save_image, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


def save_button():
    screen = pygame.display.set_mode((1300, 680))
    save_button = SaveButton(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        
        
        save_button.draw()
        
        pygame.display.update()


if __name__ == "__main__":
    save_button()