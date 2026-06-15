import music_player
import time
import pygame
import sys

class Data:
    def __init__(self, number_of_notes, number_of_beats):
        self.number_of_notes = number_of_notes
        self.number_of_beats = number_of_beats
        self.music_player = music_player.MusicPlayer()
        all_notes = []
        for beat in range(number_of_beats):
            one_beat = []
            for note in range(number_of_notes):
                one_beat.append(False)
            all_notes.append(one_beat)
        self.notes = all_notes
        self.is_playing = False


    def __repr__(self):
        representation = f"Data(number_of_notes={self.number_of_notes}, number_of_beats={self.number_of_beats})"
        for beat in self.notes:
            representation += "\n" + str(beat)
        return representation
    
    def click_at(self, beat_index, note_index):
        if 0 <= beat_index < self.number_of_beats and 0 <= note_index < self.number_of_notes:
            self.notes[beat_index][note_index] = not self.notes[beat_index][note_index]

    def get_note(self, beat_index, note_index):
        if 0 <= beat_index < self.number_of_beats and 0 <= note_index < self.number_of_notes:
            return self.notes[beat_index][note_index]
        else:
            raise IndexError("Beat or note index out of bounds")
    
    def get_all_notes(self):
        return self.notes
    
    def play(self):
        self.is_playing = True
        self.next_beat_time = time.time()
        self.current_beat = 0

    def update(self):
        if not self.is_playing:
            return

        current_time = time.time()
        if current_time >= self.next_beat_time:
            print(f"Playing beat {self.current_beat}: {self.notes[self.current_beat]}")
            
            self.music_player.play_sound(self.notes[self.current_beat])
            self.current_beat = (self.current_beat + 1) % self.number_of_beats
            self.next_beat_time = current_time + 1.5  # Adjust the beat duration as needed

    def stop(self):
        self.is_playing = False

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    data = Data(8, 16)
    data.click_at(0, 0)
    data.click_at(0, 3)        
    data.click_at(4, 0)
    # data.click_at(0, 0)
    data.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        data.update()

