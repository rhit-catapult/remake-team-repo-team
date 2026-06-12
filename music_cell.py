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
        self.height = 80
        self.cells_list = []

    def draw(self):
        while True:

            if self.x + self.length <= self.screen.get_width():
                uno_cell = pygame.draw.rect(self.screen, (100, 100, 100), (self.x, self.y, self.length, self.height))
                self.cells_list.append(uno_cell)
                self.x += self.length + 1

            else:
                self.x = 0
                if self.y + self.height <= self.screen.get_height():
                    uno_cell = pygame.draw.rect(self.screen, (100, 100, 100), (self.x, self.y, self.length, self.height))
                    self.cells_list.append(uno_cell)
                    self.y += self.height + 1
                    # print('working')

                else:
                    print('working')
                    self.y = 0
                    break
            
            
        
        
        

    # def clicked(self, screen):
    #     for event in pygame.event.get():
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             click_position = pygame.mouse.get_pos()

def main():
    pygame.init()
    pygame.display.set_caption("cells")
    screen = pygame.display.set_mode((800, 600))
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

