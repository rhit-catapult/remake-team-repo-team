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
import tempo_slider
import image_clear_button
from dancer import Dancer
import splash_screen
import load_save_dialog
import load_button
import save_button 
from music_bar import Bar
import volume


def main():
    pygame.init()

    
    pygame.display.set_caption("Music Maker")
    
    screen = pygame.display.set_mode((1300, 680))
    # button = play_button.Button(screen, 400, 400)
    mouse_pos = mouse_position.MousePosition(screen)
    my_data = data.Data(8, 16)
    cell_grid = music_cell.Cell(screen, my_data)
    drums_cells = music_cell.Cell(screen, my_data)
    play_button = image_play_button.Button(screen)
    instrument = instrument_button.Instrument(screen)
    tempo_bar = tempo_slider.Slider(screen, 400, 100, 240, initial_value = 220)
    volume_slider = volume.VolumeSlider(screen, 300, 0, 100, initial_value = 50)
    dancer1 = Dancer(screen, 262, 610, image_set = "set1")
    dancer2 = Dancer(screen, 970, 610, image_set = "set2")
    clear_button = image_clear_button.Clear(screen)
    load = load_button.LoadButton(screen)
    save = save_button.SaveButton(screen)
    splash = splash_screen.SplashScreen(screen)
    is_showing_splashhscreen = True
    beat_bar = Bar(screen)
    need_beat_bar = False

    dialog = load_save_dialog.LoadSaveDialog(screen)
    is_showing_dialog = False
   
    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if is_showing_splashhscreen and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                is_showing_splashhscreen = False
                continue  # skip the rest of the loop to avoid processing other events while the splash screen is showing

            if event.type == pygame.MOUSEBUTTONDOWN:
                if load.rect.collidepoint(event.pos):
                    dialog.open_load()
                    is_showing_dialog = True
                if save.rect.collidepoint(event.pos):
                    dialog.open_save()
                    is_showing_dialog = True

            result = dialog.process_event(event)
            if result and result[0] == 'picked':
                print('Chosen file:', result[1])
                is_showing_dialog = False
                my_data.load_from_file(result[1])
                tempo_bar.value = my_data.get_bpm()
                instrument.set_instrument(my_data.music_player.current_instrument)

            if result and result[0] == 'saved':
                print('Save filename:', result[1])
                is_showing_dialog = False
                my_data.save_to_file(result[1], instrument.get_instrument())
            if result and result[0] == 'closed':
                is_showing_dialog = False

            if is_showing_dialog:
                continue  # skip the rest of the loop to avoid processing other events while the dialog is open

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    dialog.open_load()
                    is_showing_dialog = True
                elif event.key == pygame.K_s:
                    dialog.open_save()
                    is_showing_dialog = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.rect.collidepoint(event.pos):
                    play_button.toggle()
                    if play_button.pressed:
                        my_data.play()
                        need_beat_bar = True
                    else:
                        my_data.stop()
                        need_beat_bar = False



            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if instrument.rect.collidepoint(event.pos):
                    instrument.toggle()
                    my_data.music_player.set_instrument(instrument.get_instrument())

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if clear_button.is_clicked(event.pos):
                    my_data.clear_screen()
                    need_beat_bar = False
                    play_button.reset()


            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_p]:
                    my_data.play()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos.is_clicked(event.pos):
                    the_y, beat_index, note_index = mouse_pos.find_grid_position()
                    if 505 <= the_y <= 605:
                        my_data.click_drum_at(beat_index, note_index)
                    else:
                        my_data.click_at(beat_index, note_index)

        if is_showing_splashhscreen:
            splash.draw()
            pygame.display.update()
            continue  # skip the rest of the loop to avoid updating other elements while the splash screen is showing
        

        tempo_bar.update()
        volume_slider.update()
        dancer1.update(play_button.pressed, tempo_bar.get_bpm())
        dancer2.update(play_button.pressed, tempo_bar.get_bpm())

        my_data.set_bpm(tempo_bar.get_bpm())
        my_data.update()
        my_data.music_player.set_volume(volume_slider.get_volume() / 100.0)
        
        screen.fill((0, 0, 0))
        cell_grid.draw()
        drums_cells.draw_drums()   
        
        play_button.draw()
        instrument.draw()
        clear_button.draw()
        tempo_bar.draw()
        dancer1.draw()
        dancer2.draw()
        if need_beat_bar == True:
            beat_bar.draw(my_data.get_display_beat())
        
        load.draw()
        save.draw()
        volume_slider.draw()

        dialog.draw()       
        pygame.display.update()


main()