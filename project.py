import pygame
import sys
import mouse_position
import play_button
import random
import time
import data
import music_cell


def main():
    pygame.init()

    
    pygame.display.set_caption("Music Maker")
    
    screen = pygame.display.set_mode((1300, 680))
    # button = play_button.Button(screen, 400, 400)
    mouse_pos = mouse_position.MousePosition(screen)
    my_data = data.Data(8, 16)
    cell_grid = music_cell.Cell(screen, my_data)
   
    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_p]:
                    my_data.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos.is_clicked(event.pos):
                    beat_index, note_index = mouse_pos.find_grid_position()
                    my_data.click_at(beat_index, note_index)

        

        screen.fill((0, 0, 0))
        cell_grid.draw()
        
        # button.draw()

       
        pygame.display.update()


main()