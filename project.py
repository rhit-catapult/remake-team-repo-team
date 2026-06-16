import pygame
import sys
import mouse_position
import play_button
import random
import time
import data
import music_cell
import image_play_button
import music_player
import instrument_button


def main():
    pygame.init()

    
    pygame.display.set_caption("Music Maker")
    
    screen = pygame.display.set_mode((1300, 680))
    # button = play_button.Button(screen, 400, 400)
    mouse_pos = mouse_position.MousePosition(screen)
    my_data = data.Data(8, 16)
    cell_grid = music_cell.Cell(screen, my_data)
    play_button = image_play_button.Button(screen, 400, 400)
    instrument = instrument_button.Instrument(screen, 400, 400)

   
    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.rect.collidepoint(event.pos):
                    play_button.toggle()
                    if play_button.pressed:
                        my_data.play()
                    else:
                        my_data.stop()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("somewhere")
                if instrument.rect.collidepoint(event.pos):
                    instrument.toggle()
                    my_data.music_player.set_instrument(instrument.get_instrument())

            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_p]:
                    my_data.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos.is_clicked(event.pos):
                    beat_index, note_index = mouse_pos.find_grid_position()
                    my_data.click_at(beat_index, note_index)

        
        my_data.update()
        screen.fill((0, 0, 0))
        cell_grid.draw()
        
        play_button.draw()
        instrument.draw()
        my_data.set_bpm(240)

       
        pygame.display.update()


main()