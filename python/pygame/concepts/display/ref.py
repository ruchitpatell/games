"""
https://www.pygame.org/docs/ref/display.html

* Initialize / pygame.display.init()
    Initializes the pygame display module. 
    The display module cannot do anything until it is initialized.

* Quit / pygame.display.quit()
    This will shut down the entire display module. 
    This means any active displays will be closed

Check Initialized / pygame.display.get_init()
    Returns True if the display module has been initialized

* Set Mode / set_mode(size=(w, h), flags=0, depth=0, display=0, vsync=0) -> Surface
    This function will create a display Surface. 
    The arguments passed in are requests for a display type. 
    The actual created display will be the best possible match supported by the system.

    Depth
    It is usually best to not pass the depth argument. 
    It will default to the best and fastest color depth for the system. 
    If your game requires a specific color format you can control the depth with this argument. 
    Pygame will emulate an unavailable color depth which can be slow.

    Flags
    pygame.FULLSCREEN    create a fullscreen display
    pygame.DOUBLEBUF     only applicable with OPENGL
    pygame.HWSURFACE     (obsolete in pygame 2) hardware accelerated, only in FULLSCREEN
    pygame.OPENGL        create an OpenGL-renderable display
    pygame.RESIZABLE     display window should be sizeable
    pygame.NOFRAME       display window will have no border or controls
    pygame.SCALED        resolution depends on desktop size and scale graphics
    pygame.SHOWN         window is opened in visible mode (default)
    pygame.HIDDEN        window is opened in hidden mode

* Flip / pygame.display.flip()
    Update the full display Surface to the screen

* Update / pygame.display.update(rectangle or rectangle_list)
    Update portions of the screen for software displays.
    If no arguments are passed, updates the entire screen.
    For software displays only.

Get Active / pygame.display.get_active()
    Returns True when the display is active on the screen

Get Driver / pygame.display.get_driver()
    Get the name of the pygame display backend

* Get Info / pygame.display.Info() -> VideoInfo
    Create a video display information object

* Toggle fullscreen / pygame.display.toggle_fullscreen()
    Switch between fullscreen and windowed displays

* Set Icon / pygame.display.set_icon()
    Change the system image for the display window

* Set Title / pygame.display.set_caption()
    Set the current window caption

Get Title / pygame.display.get_caption()
    Get the current window caption

Get Window size / pygame.display.get_window_size()
    Return the size of the window or screen

Get / Set Allow Screensaver
"""