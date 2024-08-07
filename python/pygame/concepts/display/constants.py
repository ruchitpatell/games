from enum import Enum

class DisplayConstant(Enum):
    DISPLAY_HEIGHT = 480
    DISPLAY_WIDTH = 600
    DISPLAY_AUTO_HEIGHT_PAD = 50
    DISPLAY_AUTO_WIDTH_PAD = 50

class RenderConstant(Enum):
    FPS = 1

class ResolutionConstant(Enum):
    SMALL = 'SMALL'
    MEDIUM = 'MEDIUM'
    LARGE = 'LARGE'

ResolutionLookup = {
    ResolutionConstant.SMALL: (640, 480),
    ResolutionConstant.MEDIUM: (800, 600),
    ResolutionConstant.LARGE: (1024, 768),
}
