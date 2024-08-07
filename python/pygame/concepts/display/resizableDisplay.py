import pygame
import sys

from constants import DisplayConstant, RenderConstant
from display import Display

"""
Scale and resize display and elements on a VIDEORESIZE

Typically, you do not want this (for performance and visuals).
Instead give the user to select resolutions and used pre-scaled assets.

For example, use 1920*720 image or 160*160 if resolution meets
certain criteria.
"""

class ResizableGame:
    def __init__(self):
        pygame.init()
        self.width, self.height = DisplayConstant.DISPLAY_WIDTH.value, DisplayConstant.DISPLAY_HEIGHT.value
        self.display = Display(self.width, self.height, pygame.RESIZABLE)
        self.load_assets()
        self.clock = pygame.time.Clock()
        self.running = True

    def load_assets(self):
        self.background_image = pygame.image.load(f"assets/background/background_resizable.png")

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(RenderConstant.FPS.value)

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                self.width, self.height = event.size
                self.display.resize(self.width, self.height)

    def update(self):
        pass

    def render(self):
        self.display.fill((0, 0, 0))
        self.display.draw_scaled_asset(self.background_image, self.width, self.height)
        self.display.update()

if __name__ == "__main__":
    ResizableGame().run()
