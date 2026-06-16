import sys
import pygame
from data import Data
from play_button import play_button



class Bar:
    def __init__(self, screen):
        self.screen = screen
        self.width = 81.25
        self.height = 605 

    def draw(self, current_beat):
        if current_beat == 0:
            current_beat = 0
        else:
            current_beat = (self.width * current_beat) - self.width
        surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        surface.fill((0, 100, 255, 30))
        self.screen.blit(surface, (current_beat, 0))
        

def main():
    pygame.init()
    pygame.display.set_caption("cells")
    screen = pygame.display.set_mode((1300, 680))
    bar = Bar(screen)
    clock = pygame.time.Clock()
    my_data = Data(8, 16)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(pygame.Color("White"))
        
        bar.draw(my_data.get_current_beat())
    
        pygame.display.update()
if __name__ == "__main__":
    main()
