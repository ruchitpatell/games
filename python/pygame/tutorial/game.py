"""
Tutorial: https://www.youtube.com/watch?v=2gABYM5M0ww
"""

import pygame
from sys import exit
from scripts.entities import PhysicsEntity
from scripts.utils import load_image, load_images
from scripts.tilemap import Tilemap


class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption('PyGame Intro')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'player': load_image('entities/player.png'),
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        self.scroll = [0, 0]

        self.tilemap = Tilemap(self, tile_size=16)

    def run(self):
        while True:
            # clear screen (sky color)
            self.display.fill((14, 219, 248))

            # camera positioned such that player is in center and smooth scroll
            self.scroll[0] += (self.player.rectangle().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rectangle().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.tilemap.render(self.display, offset=render_scroll)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)

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
                if event.key == pygame.K_UP:
                    self.player.velocity[1] -= 3

            # releasing a key
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.movement[0] = False
                if event.key == pygame.K_RIGHT:
                    self.movement[1] = False


Game().run()