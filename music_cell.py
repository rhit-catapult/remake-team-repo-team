import sys
import time
import pygame


class Cell:
    def __init__(self, screen: pygame.Surface, color):
        self.screen = screen
        self.color = color
          
    def draw(self):
        self.x = 0
        self.y = 0
        self.width = 80
        spacing_horizontal = 20
        self.height = 60
        spacing_vertical = 20
       
        for k in range(8):
            for k in range(16):
                # if clicked then:
                pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
                # if not clicked then:
                #pygame.draw.rect(self.screen, pygame.Color("White"), (self.x, self.y, self.width, self.height))
                self.x += self.width + (spacing_horizontal / 15)
            self.x = 0
            self.y += self.height + (spacing_vertical / 7)
            #move one data row down
            #change self.color as rows increase
        
        self.y = 505
        #self.color = pygame.Color("Blue")
        
        for k in range(16):
            pygame.draw.rect(self.screen, pygame.Color("White"), (self.x, self.y, self.width, 100))
            # if not clicked
            pygame.draw.circle(self.screen, pygame.Color("Gray"), (40 + self.x, 535), 8)
            #else:
                #pygame.draw.circle(self.screen, self.color, (40 + self.x, 535), 8)
            #if not clicked:
            pygame.draw.polygon(self.screen, pygame.Color("Gray"), [(40 + self.x, 568), (32 + self.x, 583), (48 + self.x, 583)], 0)
            #else:
                #pygame.draw.polygon(self.screen, self.color, [(40 + self.x, 568), (32 + self.x, 583), (48 + self.x, 583)], 0)
            
            self.x += self.width + (spacing_horizontal / 15)
    
        pygame.draw.rect(self.screen, pygame.Color("Gray"), (0, 610, self.screen.get_width(), 70))
        

def main():
    pygame.init()
    pygame.display.set_caption("cells")
    screen = pygame.display.set_mode((1300, 680))
    cell_grid = Cell(screen, pygame.Color("White"))
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
