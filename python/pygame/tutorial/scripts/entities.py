import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        self.action = ''
        self.anim_offset = (-3, -3)
        self.flip = False
        self.set_action('idle')

    def rectangle(self):
        return pygame.Rect(*self.pos, *self.size)

    def set_action(self, action):
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + self.action].copy()

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

        if movement[0] > 0:
            self.flip = False
        if movement[0] < 0:
            self.flip = True

        self.velocity[1] = min(5, self.velocity[1]+0.1)         # fall gracefull (w/ terminal velocity)

        if self.collisions['up'] or self.collisions['down']:
            self.velocity[1] = 0

        self.animation.update()

    def render(self, surface, offset):
        surface.blit(pygame.transform.flip(self.animation.img(), self.flip, False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))


class Player(PhysicsEntity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'player', pos, size)
        self.air_time = 0

    def update(self, tilemap, movement=(0, 0)):
        super().update(tilemap, movement=movement)

        self.air_time += 1
        if self.collisions['down']:
            self.air_time = 0

        if self.air_time > 4:
            self.set_action('jump')
        elif movement[0] != 0:
            self.set_action('run')
        else:
            self.set_action('idle')
