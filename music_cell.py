import sys
import random
import time
import pygame


class Cell:
    def __init__(self, screen: pygame.Surface, x, y, color):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.width = 80
        self.height = 80
        self.color = color
        self.cells_list = []
        

    # def draw(self):
        # pass
        # while True:

        #     if self.y + self.height <= self.screen.get_height():
        #         if self.x + self.width <= self.screen.get_width():
        #             uno_cell = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        #             self.cells_list.append(uno_cell)
        #             self.x += self.width + 1

        #         else:
        #             self.x = 0
        #             uno_cell = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        #             self.cells_list.append(uno_cell)
        #             self.y += self.height + 1

        #     else:
        #         self.y = 0
        #         break
            

    def draw(self):

        blocks_horizontal, spacing_horizontal = divmod(self.screen.get_width(), self.width)
        self.x = spacing_horizontal / (blocks_horizontal + 1)

        blocks_vertical, spacing_vertical = divmod(self.screen.get_height(), self.height)
        self.y = spacing_vertical / (blocks_vertical + 1)

        
        for k in range(blocks_vertical):
            for k in range(blocks_horizontal):
                uno_cell = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
                self.cells_list.append(uno_cell)
                self.x += self.width + (spacing_horizontal / (blocks_horizontal + 1))
            self.x = spacing_horizontal / (blocks_horizontal + 1)
            self.y += self.height + (spacing_vertical / (blocks_vertical + 1))
        self.y = spacing_vertical / (blocks_vertical + 1)
        

def main():
    pygame.init()
    pygame.display.set_caption("cells")
    screen = pygame.display.set_mode((780, 780))
    cell_grid = Cell(screen, 100, 100, (30, 50, 100))
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        cell_grid.draw()
    

        pygame.display.update()

main()

