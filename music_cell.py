import sys
import time
import pygame
from data import Data


class Cell:
    def __init__(self, screen: pygame.Surface, data):
        self.screen = screen
        self.data = data
          
    def draw(self):
        color = [pygame.Color("Maroon"), pygame.Color("Orange"), pygame.Color("Yellow"), pygame.Color(" Dark Green"), pygame.Color("Teal"), pygame.Color("Blue"), pygame.Color("Purple")]
        next_color = 0
        self.x = 0
        self.y = 1
        self.width = 80
        spacing_horizontal = 20
        self.height = 60
        spacing_vertical = 20

        notes = self.data.get_all_notes()
       
        for note_index in range(8):
            for beat_index in range(16):
                if notes[beat_index][note_index] == False:
                    pygame.draw.rect(self.screen, pygame.Color("White"), (self.x, self.y, self.width, self.height))
                elif notes[beat_index][note_index] == True:
                    pygame.draw.rect(self.screen, color[0 + next_color], (self.x, self.y, self.width, self.height))
                self.x += self.width + (spacing_horizontal / 15)
            self.x = 0
            self.y += self.height + (spacing_vertical / 7)
            if next_color == 6:
                next_color = 0
            else:
                next_color += 1
            
        
        self.y = 505
        #color = pygame.Color("Blue")
        
        for k in range(16):
            pygame.draw.rect(self.screen, pygame.Color("White"), (self.x, self.y, self.width, 100))
            # if not clicked
            pygame.draw.circle(self.screen, pygame.Color("Gray"), (40 + self.x, 535), 8)
            #else:
                #pygame.draw.circle(self.screen, color, (40 + self.x, 535), 8)
            #if not clicked:
            pygame.draw.polygon(self.screen, pygame.Color("Gray"), [(40 + self.x, 568), (32 + self.x, 583), (48 + self.x, 583)], 0)
            #else:
                #pygame.draw.polygon(self.screen, color, [(40 + self.x, 568), (32 + self.x, 583), (48 + self.x, 583)], 0)
            
            self.x += self.width + (spacing_horizontal / 15)
    
        pygame.draw.rect(self.screen, pygame.Color("Gray"), (0, 610, self.screen.get_width(), 70))
        

def main():
    pygame.init()
    pygame.display.set_caption("cells")
    screen = pygame.display.set_mode((1300, 680))
    my_data = Data(8, 16)
    cell_grid = Cell(screen, my_data)
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(pygame.Color("Black"))
        cell_grid.draw()
        

        pygame.display.update()
if __name__ == "__main__":
    main()
