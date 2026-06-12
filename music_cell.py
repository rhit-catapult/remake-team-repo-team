import sys
import random
import time
import pygame


class Cell:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.length = 50
        self.height = 50
        self.cells_list = []

    def draw(self):
        for k in range(50):
            for k in range(50):
                uno_cell = pygame.draw.rect(self.screen, (100, 100, 100), (self.x, self.y, self.length, self.height))
                self.cells_list.append(uno_cell)
                self.x += self.length + 1
            self.x = 0
            self.y += self.length + 1
        
        self.y = 0
            
        
        

    # def clicked(self, screen):
    #     for event in pygame.event.get():
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             click_position = pygame.mouse.get_pos()

def main():
    pygame.init()
    pygame.display.set_caption("cells")
    screen = pygame.display.set_mode((640, 480))
    test_cell = Cell(screen, 100, 100, )
    clock = pygame.time.Clock()



    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        test_cell.draw()
    


        pygame.display.update()

main()

