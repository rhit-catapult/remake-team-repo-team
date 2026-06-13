import pygame
import sys
import play_button
import random
import time


def main():
    pygame.init()

    
    pygame.display.set_caption("Music Maker")
    
    screen = pygame.display.set_mode((800, 500))
    button = play_button.Button(screen, 400, 400)

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        

        screen.fill((255, 255, 255))

        
        button.draw()

       
        pygame.display.update()


main()