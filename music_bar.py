import sys
import pygame

from play_button import play_button



class Bar:
    def __init__(self, screen, speed):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.width = 80 # need to change this to the width of a cell
        self.height = 605 # need to change this to the height of player
        # self.color = pygame.Color(0, 0, 0) # opacity?
        # self.color.hsla = (200, 80, 80, 2)
        self.speed = speed # tempo

    def draw(self):
        surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        surface.fill((0, 100, 255, 30))
        self.screen.blit(surface, (self.x, self.y))
        
    def update_position(self, speed):
        self.x += self.speed



def main():
    pygame.init()
    pygame.display.set_caption("cells")
    screen = pygame.display.set_mode((1300, 680))
    bar = Bar(screen, 20)
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(pygame.Color("White"))
        
        bar.draw()

        pygame.display.update()
if __name__ == "__main__":
    main()
