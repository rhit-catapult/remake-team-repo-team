import pygame
import sys
import time
import random
import math

class MusicBox:
    def __init__(self, number_of_notes, number_of_beats):
        self.number_of_notes = number_of_notes
        self.number_of_beats = number_of_beats
        self.notes = [[0 for _ in range(number_of_beats)] for _ in range(number_of_notes)]
    