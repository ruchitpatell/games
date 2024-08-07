import pygame
import sys

from constants import ResolutionConstant, ResolutionLookup
from display import Display

class MultiResolutionGame:
    def __init__(self):
        pygame.init()
        self.current_resolution = ResolutionLookup[ResolutionConstant.MEDIUM]
        self.set_resolution(self.current_resolution)
        self.clock = pygame.time.Clock()
        self.running = True

    def set_resolution(self, resolution):
        self.width, self.height = resolution
        self.display = Display(self.width, self.height)
        self.load_assets()
        self.setup_physics()

    def load_assets(self):
        self.background_image = pygame.image.load(f"assets/background/background_{self.width}x{self.height}.png")

    def setup_physics(self):
        self.gravity = 9.8 * (self.height / 600)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                self.set_resolution(event.size)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.change_resolution(ResolutionConstant.SMALL)
                elif event.key == pygame.K_2:
                    self.change_resolution(ResolutionConstant.MEDIUM)
                elif event.key == pygame.K_3:
                    self.change_resolution(ResolutionConstant.LARGE)

    def change_resolution(self, resolution_key):
        if resolution_key in ResolutionLookup:
            self.set_resolution(ResolutionLookup[resolution_key])

    def update(self):
        pass

    def render(self):
        self.display.screen.blit(self.background_image, (0, 0))
        self.display.update()

if __name__ == "__main__":
    MultiResolutionGame().run()
