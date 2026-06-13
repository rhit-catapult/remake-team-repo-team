import sys
import random
import time
import pygame


class Cell:
    def __init__(self, screen: pygame.Surface, x, y, color):
        self.screen = screen
        self.x = 0
        self.y = 0
        # self.width = 81
        # self.height = 85
        self.color = color
        self.cells_list = []
        

    # def draw(self):
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

        self.width, spacing_horizontal = divmod(self.screen.get_width(), 16)
        
        # if spacing_horizontal == 0:
        self.width = 80
        spacing_horizontal = 20

            
        # self.x = spacing_horizontal / (blocks_horizontal + 1)

        self.height, spacing_vertical = divmod(self.screen.get_height() - 180, 8)
        self.height = 60
        spacing_vertical = 20
        # if spacing_vertical == 0:
        #     spacing_vertical = self.height
        #     blocks_vertical -= 1
        # self.y = spacing_vertical / (blocks_vertical + 1)
        # print(self.width, " x ", self.height)
        self.x = 0
        self.y = 0

       
        for k in range(8):
            for k in range(16):
                uno_cell = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
                self.cells_list.append(uno_cell)
                self.x += self.width + (spacing_horizontal / 15)
            self.x = 0
            self.y += self.height + (spacing_vertical / 7)
        
        self.y += 2
        for k in range(16):
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, 100))
            self.x += self.width + (spacing_horizontal / 15)

    
        pygame.draw.rect(self.screen, pygame.Color("Gray"), (0, 610, self.screen.get_width(), 70))

def main():
    pygame.init()
    pygame.display.set_caption("cells")
    screen = pygame.display.set_mode((1300, 680))
    cell_grid = Cell(screen, 100, 100, pygame.Color("White"))
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(pygame.Color("Black"))
        cell_grid.draw()
    

        pygame.display.update()

main()

