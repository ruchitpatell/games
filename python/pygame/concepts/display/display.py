import pygame
from constants import DisplayConstant

class Display:
    def __init__(self, width, height, flags=0, auto=False):
        assert pygame.display.get_init() == True
        self.width = width
        self.height = height
        self.flags = flags
        
        if auto:
            self.__set_auto_resolution()
        self.__set_display()
        
        self.__set_caption()

    def __set_display(self):
        self.screen = pygame.display.set_mode((self.width, self.height), self.flags)

    def __set_auto_resolution(self):
        info = pygame.display.Info()
        self.width, self.height = info.current_w - DisplayConstant.DISPLAY_AUTO_WIDTH_PAD, info.current_h - DisplayConstant.DISPLAY_AUTO_HEIGHT_PAD

    def __set_caption(self):
        pygame.display.set_caption("PyGame Display")
        icon = pygame.image.load("assets/icon/icon.svg")
        pygame.display.set_icon(icon)

    def fill(self, color):
        self.screen.fill(color)

    def update(self):
        pygame.display.update()

    def toggle_fullscreen(self):
        pygame.display.toggle_fullscreen()

    def resize(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
    
    def draw_scaled_asset(self, asset, width, height):
        asset_width, asset_height = asset.get_size()
        aspect_ratio = asset_width / asset_height

        # compute new dimensions
        if width / height > aspect_ratio:
            new_width = height * aspect_ratio
            new_height = height
        else:
            new_width = width
            new_height = width / aspect_ratio

        # center the image
        x = (width - new_width) // 2
        y = (height - new_height) // 2

        scaled_asset = pygame.transform.scale(asset, (int(new_width), int(new_height)))
        self.screen.blit(scaled_asset, (x, y))
