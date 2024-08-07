PyGame module to control the display window and screen.

The origin of the display, where x = 0 and y = 0, is the top left of the screen. Both axes increase positively towards the bottom right of the screen.

The pygame display can actually be initialized in one of several modes. By default, the display is a basic software driven framebuffer. You can request special modules like automatic scaling or OpenGL support. These are controlled by flags passed to pygame.display.set_mode().

Pygame can only have a single display active at any time. Creating a new one with pygame.display.set_mode() will close the previous display.
