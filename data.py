class Data:
    def __init__(self, number_of_notes, number_of_beats):
        self.number_of_notes = number_of_notes
        self.number_of_beats = number_of_beats
        all_notes = []
        for beat in range(number_of_beats):
            one_beat = []
            for note in range(number_of_notes):
                one_beat.append(False)
            all_notes.append(one_beat)
        self.notes = all_notes

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

if __name__ == "__main__":
    data = Data(8, 16)
    data.click_at(0, 0)
    data.click_at(0, 3)
    data.click_at(4, 0)
    data.click_at(0, 0)
    print(data)
