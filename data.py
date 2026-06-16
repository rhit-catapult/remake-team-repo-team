import music_player
import time
import pygame
import sys
import json

class Data:
    def __init__(self, number_of_notes, number_of_beats):
        self.number_of_notes = number_of_notes
        self.number_of_beats = number_of_beats
        self.current_beat = 0
        self.music_player = music_player.MusicPlayer()
        all_notes = []
        all_drums = []
        self.beat_duration = 0.5  # Duration of each beat in seconds
    
        for beat in range(number_of_beats):
            one_beat = []
            for note in range(number_of_notes):
                one_beat.append(False)
            all_notes.append(one_beat)
        self.notes = all_notes

        for beat in range(number_of_beats):
            one_beat = []
            for note in range(2):
                one_beat.append(False)
            all_drums.append(one_beat)
        self.drums = all_drums
        self.is_playing = False

    def __repr__(self):
        representation = f"Data(number_of_notes={self.number_of_notes}, number_of_beats={self.number_of_beats})"
        for k in range(len(self.notes)):
            beat = self.notes[k]
            drums = self.drums[k]
            representation += "\n" + str(beat) + "  " + str(drums)
        return representation
    
    def click_at(self, beat_index, note_index):
        if 0 <= beat_index < self.number_of_beats and 0 <= note_index < self.number_of_notes:
            self.notes[beat_index][note_index] = not self.notes[beat_index][note_index]

    def click_drum_at(self, beat_index, note_index):
        if 0 <= beat_index < self.number_of_beats and 0 <= note_index < 2:
            self.drums[beat_index][note_index] = not self.drums[beat_index][note_index]

    def get_note(self, beat_index, note_index):
        if 0 <= beat_index < self.number_of_beats and 0 <= note_index < self.number_of_notes:
            return self.notes[beat_index][note_index]
        else:
            raise IndexError("Beat or note index out of bounds")
    
    def get_all_notes(self):
        return self.notes
    
    def get_all_drums(self):
        return self.drums

    def play(self):
        self.is_playing = True
        self.next_beat_time = time.time()
        self.current_beat = 0

    def update(self):
        if not self.is_playing:
            return

        current_time = time.time()
        if current_time >= self.next_beat_time:
            possible_notes = []
            for k in range(8):
                if self.notes[self.current_beat][k]:
                    possible_notes.append(k)

            possible_drums = []
            for k in range(2):
                if self.drums[self.current_beat][k]:
                    possible_drums.append(k)

            print(f"Playing beat {self.current_beat}: {self.notes[self.current_beat]}")
            
            self.music_player.play_sound(possible_notes, possible_drums)
            self.current_beat = (self.current_beat + 1) % self.number_of_beats
            self.next_beat_time = current_time + self.beat_duration  # Adjust the beat duration as needed

    def get_current_beat(self):
        # print(self.current_beat)
        return self.current_beat
    
    def stop(self):
        self.is_playing = False

    def set_bpm(self, bpm):
        self.beat_duration = 60 / bpm  # Convert BPM to seconds per beat

    def get_bpm(self):
        return 60 / self.beat_duration  # Convert seconds per beat back to BPM
    
    def clear_screen(self):
        for beat in range(self.number_of_beats):
            for note in range(self.number_of_notes):
                self.notes[beat][note] = False

        for beat in range(self.number_of_beats):
            for drum in range(2):
                self.drums[beat][drum] = False
        
        self.stop()
    
    def load_from_file(self, file_path):
 
        with open(file_path, 'r') as f:
            data = json.load(f)
            self.notes = data['notes']
            self.drums = data['drums']
            self.set_bpm(data['tempo'])
            self.music_player.set_instrument(data['instrument'])

    def save_to_file(self, file_path, instrument):
        data = {
            'notes': self.notes,
            'drums': self.drums,
            'tempo': self.get_bpm(),
            'instrument': instrument
        }
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    data = Data(8, 16)
    data.music_player.set_instrument("piano")
    # slide = data.tempo_slider()
    data.set_bpm(320)
    # data.click_at(0, 0)
    # data.click_at(1, 3)        
    # data.click_at(2, 5)
    # data.click_at(3, 3)
    # data.click_at(4, 0)
    # data.click_at(5, 2)
    # data.click_at(6, 0)
    # data.click_at(0, 0)
    

    # data.click_drum_at(0, 0)
    # data.click_drum_at(1, 1)
    # data.click_drum_at(15, 1)
    # print(data.get_all_drums())
    data.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        data.update()
        data.get_current_beat()

