import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.e_type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

    def rectangle(self):
        return pygame.Rect(*self.pos, *self.size)

    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        # no clue
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        # horizontal collison
        self.pos[0] += frame_movement[0]
        entity_rect = self.rectangle()
        for rectangle in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rectangle):
                if frame_movement[0] > 0:
                    self.collisions['right'] = True
                    entity_rect.right = rectangle.left
                if frame_movement[0] < 0:
                    self.collisions['left'] = True
                    entity_rect.left = rectangle.right
                self.pos[0] = entity_rect.x

        # vertical collison
        self.pos[1] += frame_movement[1]
        entity_rect = self.rectangle()
        for rectangle in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rectangle):
                if frame_movement[1] > 0:
                    self.collisions['down'] = True
                    entity_rect.bottom = rectangle.top
                if frame_movement[1] < 0:
                    self.collisions['up'] = True
                    entity_rect.top = rectangle.bottom
                self.pos[1] = entity_rect.y

        self.velocity[1] = min(5, self.velocity[1]+0.1)         # fall gracefull (w/ terminal velocity)

        if self.collisions['up'] or self.collisions['down']:
            self.velocity[1] = 0

    def render(self, surface):
        surface.blit(self.game.assets[self.e_type], self.pos)
