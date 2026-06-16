import pygame
import sys
import data
import math
import colorsys

class Slider:
    def __init__(self, screen, track_width, min_value, max_value, initial_value=None, pulse_period = 4000.0):
        self.screen = screen
        # dark purple styling for the tempo bar
        self.track_color = (43, 23, 83)
        self.fill_color = (100, 42, 150)
        self.text_color = (255, 255, 255)
        self.min_value = min_value
        self.max_value = max_value
        self.track_width = track_width
        self.height = 10
        self.y = screen.get_height() - self.height - 26
        self.value = initial_value if initial_value is not None else min_value
        self.width = self.value_to_width(self.value)
        self.dragging = False
        self.font = pygame.font.SysFont("jokerman", 24)
        self.spacing = 15
        # milliseconds for a full hue cycle; adjustable
        self.pulse_period = pulse_period
        initial_text = self.font.render(f"Tempo: {self.get_bpm()} BPM", True, self.text_color)
        combined_width = self.track_width + self.spacing + initial_text.get_width()
        self.group_x = self.screen.get_width() // 2 - combined_width // 2
        self.text_x = self.group_x + self.track_width + self.spacing
        
    def draw(self):

        # hue cycles 0..1 over self.pulse_period milliseconds
        t = pygame.time.get_ticks() % self.pulse_period
        h = (t / self.pulse_period) % 1.0
        r_f, g_f, b_f = colorsys.hsv_to_rgb(h, 0.9, 0.55)
        pulse_color = (int(r_f * 255), int(g_f * 255), int(b_f * 255))

        bpm_text = self.font.render(f"Tempo: {self.get_bpm()} BPM", True, pulse_color)
        # draw outer border first so the slider looks clearer
        pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            (self.group_x - 3, self.y - 3, self.track_width + 5, self.height + 5),
            3,
        )
        pygame.draw.rect(self.screen, self.track_color, (self.group_x, self.y, self.track_width, self.height))
        pygame.draw.rect(self.screen, self.fill_color, (self.group_x, self.y, self.width, self.height))
        text_y = self.y + (self.height - bpm_text.get_height()) // 2
        self.screen.blit(bpm_text, (self.text_x, text_y))

    def value_to_width(self, value):
        percent = (value - self.min_value) / (self.max_value - self.min_value)
        percent = max(0.0, min(percent, 1.0))
        return int(percent * self.track_width)

    def width_to_value(self, width):
        percent = width / self.track_width if self.track_width else 0
        percent = max(0.0, min(percent, 1.0))
        return self.min_value + percent * (self.max_value - self.min_value)

    def get_bpm(self):
        return int(self.value)

    def update(self):
        """Update slider width when the left mouse button is held or dragged over the track."""
        mx, my = pygame.mouse.get_pos()
        mouse_down = pygame.mouse.get_pressed()[0]
        if mouse_down:
            if self.dragging or ((self.group_x <= mx <= self.group_x + self.track_width) and (self.y <= my <= self.y + self.height)):
                self.dragging = True
                new_width = mx - self.group_x
                self.width = max(0, min(new_width, self.track_width))
                self.value = int(self.width_to_value(self.width))
        else:
            self.dragging = False

