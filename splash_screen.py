import pygame
import sys

class SplashScreen:
    def __init__(self, screen: pygame.Surface):
        

        self.screen = screen
        self.splash_image = pygame.image.load("splash_screen.png") # add image path of splash screen here (need to be the same aspect as the screen ratio)
        self.x = 0
        self.y = 0
        self.splash_image = pygame.transform.scale(self.splash_image, (1300, 680))
        self.pressed = False
        

    def draw(self):
        self.screen.blit(self.splash_image, (self.x, self.y))

    def toggle(self):
        self.pressed = not self.pressed
            
        



def splash():
    screen = pygame.display.set_mode((1300, 680))
    splash = SplashScreen(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                splash.toggle()

        if splash.pressed:
            return


        splash.draw()
        
        pygame.display.update()


if __name__ == "__main__":
    splash()