import argparse
import pygame
import sys

from constants import ArgumentDict, ColorConstant, DisplayConstant, FUNC, ARGS, FunctionArgumentDict, RenderConstant, ShapeParamConstant

class Game:
    def __init__(self, shapes=None):
        pygame.init()
        self.screen = pygame.display.set_mode((DisplayConstant.DISPLAY_WIDTH.value, DisplayConstant.DISPLAY_HEIGHT.value))
        pygame.display.set_caption("Pygame Draw")
        self.clock = pygame.time.Clock()
        self.running = True
        self.shapes = shapes
        self.screen.fill(ColorConstant.BLACK.value)
        self.demo_shapes()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.clock.tick(RenderConstant.FPS.value)

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def __demo(self, shape):
        try:
            FunctionArgumentDict[shape][FUNC](self.screen, FunctionArgumentDict[shape][ARGS][:ShapeParamConstant.MAX_OBJECTS.value])
        except Exception as e:
            print('Exception: ', e)
            self.running = False

    def demo_shapes(self):
        if not self.shapes:
            return
        for shape in self.shapes:
            self.__demo(shape)

def handle_args():
    parser = argparse.ArgumentParser(description="Draw shapes.")

    for key, value in ArgumentDict.items():
        parser.add_argument(*value, action='append_const', const=key, dest='shapes', help=f'Draw {key}')

    args = parser.parse_args()
    return list(set(args.shapes)) if args.shapes else None       # .shapes has to match dest='shapes'


def main():
    shapes = handle_args()
    Game(shapes).run()

if __name__ == '__main__':
    main()
