"""
Tutorial: https://www.youtube.com/watch?v=2gABYM5M0ww
"""

import pygame
from sys import exit
from scripts.entities import PhysicsEntity
from scripts.utils import load_image


class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption('PyGame Intro')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

    def run(self):
        while True:
            # clear screen (sky color)
            self.display.fill((14, 219, 248))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            self.handle_event()
            
            # create pixel effect, slow
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

            # update 60 frames per second
            pygame.display.update()
            self.clock.tick(60)

    def handle_event(self):
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # pressing a key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.movement[0] = True
                if event.key == pygame.K_RIGHT:
                    self.movement[1] = True

            # releasing a key
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.movement[0] = False
                if event.key == pygame.K_RIGHT:
                    self.movement[1] = False


Game().run()