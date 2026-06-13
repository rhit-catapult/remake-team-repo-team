import pygame
import sys
import random
import time
import mouse_position

def main():
    pygame.init()
    pygame.display.set_caption("Music Maker")
    screen = pygame.display.set_mode((800, 500))
    mouse_pos = mouse_position.MousePosition(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pos.is_clicked(event.pos):
                print("Mouse clicked at:", mouse_pos.x, mouse_pos.y)
main()