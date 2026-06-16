import pygame
import sys

class Dancer:
    def __init__(self, screen: pygame.Surface, x: int = 0, y: int = 0, size=(60, 60)):
        self.screen = screen
        self.size = size
        # Hard-coded dancer location. This is intentionally fixed so the dancer
        # does not depend on slider internals or position data.
        self.x = 260
        self.y = 615

        # Placeholder image file names. Put your dancer PNGs in the same
        # folder as this script or update the paths below.
        image_paths = [
            "play.png",
            "pause.png",
            "sax_button.png",
        ]

        self.images = [
            pygame.transform.scale(pygame.image.load(path), self.size)
            for path in image_paths
        ]

        self.current_index = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_delay = 200  # milliseconds between dancer frames
        self.playing = False

    def update(self, playing: bool):
        """Update dancer animation state based on whether music is playing."""
        if playing:
            now = pygame.time.get_ticks()
            if now - self.last_update >= self.frame_delay:
                self.last_update = now
                self.current_index = (self.current_index + 1) % len(self.images)
                self.playing = True
        else:
            self.current_index = 0
            self.playing = False
            self.last_update = pygame.time.get_ticks()

    def draw(self):
        self.screen.blit(self.images[self.current_index], (self.x, self.y))


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Dancer Test")
    dancer = Dancer(screen, 140, 90)
    clock = pygame.time.Clock()
    playing = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing

        dancer.update(playing)
        screen.fill((30, 30, 30))
        dancer.draw()

        pygame.display.update()
        clock.tick(30)

    if __name__ == "__main__":
        pygame.init()
        screen = pygame.display.set_mode((800, 500))
