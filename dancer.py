import pygame
import sys

class Dancer:
    IMAGE_SETS = { # dancer sprites go in theese sets set 1 is to the left and set 2 is on the right
        "set1": [
            "green_dancer_one.png",
            "green_dancer_two.png",
            "green_dancer_three.png",
        ],
        "set2": [
            "play.png",
            "play.png",
            "pause.png",
        ],
    }

    def __init__(
        self,
        screen: pygame.Surface,
        x,
        y,
        size=(70, 70),
        image_set: str = "set1",
        image_paths: list[str] | None = None,
    ):
        self.screen = screen
        self.size = size
        # Hard-coded dancer location. This is intentionally fixed so the dancer
        # does not depend on slider internals or position data.
        self.x = x
        self.y = y

        if image_paths is not None:
            self.image_paths = image_paths
        else:
            self.image_paths = self.IMAGE_SETS.get(image_set, self.IMAGE_SETS["set1"])

        self.images = [
            pygame.transform.scale(pygame.image.load(path), self.size)
            for path in self.image_paths
        ]

        self.current_index = 0
        self.last_update = pygame.time.get_ticks()
        self.bpm = 120
        self.frame_delay = self.bpm_to_delay(self.bpm)
        self.playing = False

    def bpm_to_delay(self, bpm: float) -> float:
        """Convert BPM to a frame delay in milliseconds."""
        # Use a shorter delay at higher BPM so the dancer animation speeds up.
        # This formula gives roughly two dancer frames per beat.
        delay = 55000 / bpm / 2
        return max(30, delay)

    def update(self, playing: bool, bpm: float | None = None):
        """Update dancer animation state based on whether music is playing."""
        if bpm is not None:
            self.bpm = bpm
            self.frame_delay = self.bpm_to_delay(self.bpm)

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

    def set_image_set(self, image_set: str):
        self.image_paths = self.IMAGE_SETS.get(image_set, self.IMAGE_SETS["set1"])
        self.images = [
            pygame.transform.scale(pygame.image.load(path), self.size)
            for path in self.image_paths
        ]
        self.current_index = 0

    def draw(self):
        self.screen.blit(self.images[self.current_index], (self.x, self.y))


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Dancer Test")
    dancer = Dancer(screen, 0, 0, image_set="set1")
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
                elif event.key == pygame.K_1:
                    dancer.set_image_set("set1")
                elif event.key == pygame.K_2:
                    dancer.set_image_set("set2")

        dancer.update(playing)
        screen.fill((30, 30, 30))
        dancer.draw()

        info_text = pygame.font.SysFont(None, 20).render(
            "SPACE to toggle, 1/2 to switch dancer sets", True, (255, 255, 255)
        )
        screen.blit(info_text, (10, 10))

        pygame.display.update()
        clock.tick(30)
