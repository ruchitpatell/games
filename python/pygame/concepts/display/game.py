import pygame
import random
import sys

from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT, FPS
from display import Display

class Game:
    def __init__(self):
        pygame.init()
        self.display = Display(DISPLAY_WIDTH, DISPLAY_HEIGHT, pygame.RESIZABLE, auto=True)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                self.display.resize(event.w, event.h)

    def update(self):
        pass

    def render(self):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.display.fill((0, 0, 0))
        pygame.draw.rect(self.display.screen, random_color, (50, 50, 100, 100))
        self.display.update()

def main():
    Game().run()

if __name__ == '__main__':
    main()
