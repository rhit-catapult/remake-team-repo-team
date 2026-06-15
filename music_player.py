import pygame
import sys
import time
import random
import math

class MusicPlayer:
    def __init__(self):
        self.violin_sounds = []
        self.sax_sounds = []
        self.piano_sounds = []
        self.current_sounds = self.violin_sounds
        self.violin_sounds.append(pygame.mixer.Sound("violin/violin_c4.wav"))
        self.violin_sounds.append(pygame.mixer.Sound("violin/violin_d4.wav"))
        self.violin_sounds.append(pygame.mixer.Sound("violin/violin_e4.wav"))
        self.violin_sounds.append(pygame.mixer.Sound("violin/violin_f4.wav"))
        self.violin_sounds.append(pygame.mixer.Sound("violin/violin_g4.wav"))
        self.violin_sounds.append(pygame.mixer.Sound("violin/violin_a4.wav"))
        self.violin_sounds.append(pygame.mixer.Sound("violin/violin_b4.wav"))
        self.violin_sounds.append(pygame.mixer.Sound("violin/violin_c5.wav"))
        self.sax_sounds.append(pygame.mixer.Sound("sax/sax_c3.wav"))
        self.sax_sounds.append(pygame.mixer.Sound("sax/sax_d3.wav"))
        self.sax_sounds.append(pygame.mixer.Sound("sax/sax_e3.wav"))
        self.sax_sounds.append(pygame.mixer.Sound("sax/sax_f3.wav"))
        self.sax_sounds.append(pygame.mixer.Sound("sax/sax_g3.wav"))
        self.sax_sounds.append(pygame.mixer.Sound("sax/sax_a3.wav"))
        self.sax_sounds.append(pygame.mixer.Sound("sax/sax_b3.wav"))
        self.sax_sounds.append(pygame.mixer.Sound("sax/sax_c4.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("piano/piano_c3.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("piano/piano_d3.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("piano/piano_e3.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("piano/piano_f3.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("piano/piano_g3.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("piano/piano_a3.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("piano/piano_b3.wav"))
        self.piano_sounds.append(pygame.mixer.Sound("piano/piano_c4.wav"))
    
    def play_sound(self, possible_notes):
        for k in range(len(possible_notes)):
            if possible_notes[k]:
                self.current_sounds[k].play()
                print("note")

    def set_instrument(self, instrument):
        if instrument == "violin":
            self.current_sounds = self.violin_sounds
        elif instrument == "sax":
            self.current_sounds = self.sax_sounds
        elif instrument == "piano":
            self.current_sounds = self.piano_sounds
        else:
            raise ValueError("Invalid instrument selected")

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    player = MusicPlayer()
    player.set_instrument("piano")
    player.play_sound([0, 2, 4])
    time.sleep(2)
    player.play_sound([0])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()



    