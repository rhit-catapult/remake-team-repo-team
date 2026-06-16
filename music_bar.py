import sys
import pygame
from data import Data
from play_button import play_button



class Bar:
    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.width = 81.25
        self.height = 605 

    def draw(self, what_beat):
        what_beat = what_beat * (1300 // 16)
        surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        surface.fill((0, 100, 255, 30))
        self.screen.blit(surface, (self.x + what_beat, self.y))
        

def main():
    pygame.init()
    pygame.display.set_caption("cells")
    screen = pygame.display.set_mode((1300, 680))
    bar = Bar(screen)
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(pygame.Color("White"))
        
        bar.draw(2)
    
        pygame.display.update()
if __name__ == "__main__":
    main()
