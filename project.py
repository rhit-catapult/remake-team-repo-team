import pygame
import sys
import my_character
import play_button
import random
import time


def main():
    pygame.init()

    
    pygame.display.set_caption("Music Maker")
    
    screen = pygame.display.set_mode((800, 500))
    # creates a Character from the my_character.py file
    character = my_character.Character(screen, 100, 100)
    button = play_button.Button(screen, 400, 400)

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))

        # draws the character every frame
        character.draw()
        button.draw()

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()