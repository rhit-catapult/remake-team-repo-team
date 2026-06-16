import pygame
import sys
import data
import math

class Slider:
    def __init__(self, screen, track_width, min_value, max_value, initial_value=None):
        self.screen = screen
        self.track_color = (150, 150, 150)
        self.fill_color = (50, 50, 50)
        self.text_color = (255, 255, 255)
        self.min_value = min_value
        self.max_value = max_value
        self.track_width = track_width
        self.height = 10
        self.y = screen.get_height() - self.height - 20
        self.value = initial_value if initial_value is not None else min_value
        self.width = self.value_to_width(self.value)
        self.dragging = False
        self.font = pygame.font.SysFont("jokerman", 24)
        self.spacing = 15
        initial_text = self.font.render(f"Tempo: {self.get_bpm()} BPM", True, self.text_color)
        combined_width = self.track_width + self.spacing + initial_text.get_width()
        self.group_x = self.screen.get_width() // 2 - combined_width // 2
        self.text_x = self.group_x + self.track_width + self.spacing
        
    def draw(self):
        # pulse factor oscillates between 0 and 1
        pulse_period = 3.5 * 1000 # milliseconds for a full purple->blue->purple cycle
        t = pygame.time.get_ticks() % pulse_period
        f = (math.sin(2 * math.pi * (t / pulse_period)) + 1) / 2

        # darker purple and blue RGB
        purple = (75, 0, 110)
        blue = (150, 0, 150)
        r = int(purple[0] * (1 - f) + blue[0] * f)
        g = int(purple[1] * (1 - f) + blue[1] * f)
        b = int(purple[2] * (1 - f) + blue[2] * f)
        pulse_color = (r, g, b)

        bpm_text = self.font.render(f"Tempo: {self.get_bpm()} BPM", True, pulse_color)
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

