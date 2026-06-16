import pygame
import sys


class Instrument:
    def __init__(self, screen: pygame.Surface, x, y):
        IMAGE_SIZE = 75
        self.screen = screen
        self.x = x
        self.y = y
       
        self.instrument_violin = pygame.image.load("violin_button.png")
        self.instrument_violin = pygame.transform.scale(self.instrument_violin, (IMAGE_SIZE, IMAGE_SIZE))
        self.instrument_sax = pygame.image.load("sax_button.png")
        self.instrument_sax = pygame.transform.scale(self.instrument_sax, (IMAGE_SIZE, IMAGE_SIZE))
        self.instrument_piano = pygame.image.load("piano_button.png")
        self.instrument_piano = pygame.transform.scale(self.instrument_piano, (IMAGE_SIZE, IMAGE_SIZE))
        self.rect = self.instrument_violin.get_rect(center=(self.x - 265, self.y + 243))
        self.possible_instruments = ["violin", "sax", "piano"]
        self.current_instrument = 0
    
    def get_instrument(self):
        return self.possible_instruments[self.current_instrument]

    def draw(self):
        
        if self.current_instrument == 0:
            self.screen.blit(self.instrument_violin, self.rect)
        if self.current_instrument == 1:
            self.screen.blit(self.instrument_sax, self.rect)
        if self.current_instrument == 2:
            self.screen.blit(self.instrument_piano, self.rect)

    def toggle(self):
        if self.current_instrument == 0:
            self.rect = self.instrument_sax.get_rect(center=(self.x - 265, self.y + 243))
            self.current_instrument = 1

        elif self.current_instrument == 1:
            self.rect = self.instrument_piano.get_rect(center=(self.x - 265, self.y + 243))
            self.current_instrument = 2

        elif self.current_instrument == 2:
            self.rect = self.instrument_violin.get_rect(center=(self.x -265, self.y + 243))
            self.current_instrument = 0
        
        print("self.current_instrument", self.current_instrument)



def instrument():
    screen = pygame.display.set_mode((1300, 680))
    instrument = Instrument(screen, 400, 400)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("somewhere")
                if instrument.rect.collidepoint(event.pos):
                    instrument.toggle()
                    print("clicked button")
        
        instrument.draw()
        
        pygame.display.update()


if __name__ == "__main__":
    instrument()
