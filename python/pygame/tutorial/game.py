"""
Tutorial: https://www.youtube.com/watch?v=2gABYM5M0ww
"""

import pygame
from sys import exit


class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption('PyGame Intro')
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img_pos = [160, 260]
        self.movement = [False, False]

        self.collision_area = pygame.Rect(50, 50, 300, 50)  # x, y, width, height

    def run(self):
        while True:
            # clear screen (sky color)
            self.screen.fill((14, 219, 248))

            # A rectangle following our image, detect collision
            img_r = pygame.Rect(*self.img_pos, *self.img.get_size())
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)

            self.img_pos[1] += (self.movement[1] - self.movement[0])*5  # boolean math 4 up or down
            self.img.set_colorkey((0, 0, 0))                            # set black as transparent
            self.screen.blit(self.img, self.img_pos)                    # top-left (0, 0)
                
            # self.screen.blit(img_r, img_r.get)

            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # pressing a key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True

                # releasing a key
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
            
            # update 60 frames per second
            pygame.display.update()
            self.clock.tick(60)

Game().run()