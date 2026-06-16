import pygame
import sys
import data

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
        self.x = screen.get_width() // 2 - self.track_width // 2
        self.value = initial_value if initial_value is not None else min_value
        self.width = self.value_to_width(self.value)
        self.dragging = False
        self.font = pygame.font.SysFont("jokerman", 24)
        
    def draw(self):
        pygame.draw.rect(self.screen, self.track_color, (self.x, self.y, self.track_width, self.height))
        pygame.draw.rect(self.screen, self.fill_color, (self.x, self.y, self.width, self.height))
        bpm_text = self.font.render(f"Tempo: {self.get_bpm()} BPM", True, self.text_color)
        text_x = self.x + self.track_width + 15
        text_y = self.y - bpm_text.get_height() // 2 + self.height // 2
        self.screen.blit(bpm_text, (text_x, text_y))

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
            if self.dragging or ((self.x <= mx <= self.x + self.track_width) and (self.y <= my <= self.y + self.height)):
                self.dragging = True
                new_width = mx - self.x
                self.width = max(0, min(new_width, self.track_width))
                self.value = int(self.width_to_value(self.width))
        else:
            self.dragging = False

