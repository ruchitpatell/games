from pygame import Rect
from enum import Enum
from rect import draw_rects, RectangleConstant

class DisplayConstant(Enum):
    DISPLAY_HEIGHT = 480
    DISPLAY_WIDTH = 600

class RenderConstant(Enum):
    FPS = 1

class ColorConstant(Enum):
    RED = "red"
    BLACK = "black"
    WHITE = "white"
    GREEN = "green"
    BLUE = "blue"
    CYAN = "cyan"
    MAGENTA = "magenta"

class ArgumentConstant(Enum):
    RECTANGLE = "RECTANGLE"
    POLYGON   = "POLYGON"
    CIRCLE    = "CIRCLE"
    ELLIPSE   = "ELLIPSE"
    ARC       = "ARC"
    LINE      = "LINE"
    LINES     = "LINES"
    AALINE    = "AALINE"
    AALINES   = "AALINES"

ArgumentDict = {
    ArgumentConstant.RECTANGLE.value : ["-r",    "-R",     "--rect",      "--RECT",     "--rectangle"   , "--RECTANGLE"],
    ArgumentConstant.POLYGON.value   : ["-p",    "-P",     "--poly",      "--POLY",     "--polygon"     , "--POLYGON"],
    ArgumentConstant.CIRCLE.value    : ["-c",    "-C",     "--cir" ,      "--CIR" ,     "--circle"      , "--CIRCLE"],
    ArgumentConstant.ELLIPSE.value   : ["-e",    "-E",     "--elp",       "--ELP",      "--ellipse"     , "--ELLIPSE"],
    ArgumentConstant.ARC.value       : ["-a",    "-A",     "--arc",       "--ARC"],
    ArgumentConstant.LINE.value      : ["-l",    "-L",     "--line",      "--LINE"],
    ArgumentConstant.LINES.value     : ["-ls",   "--LS",   "--lines",     "--LINES"],
    ArgumentConstant.AALINE.value    : ["-aal",  "--AAL",  "--aaline",    "--AALINE"],
    ArgumentConstant.AALINES.value   : ["-aals", "--AALS", "--aalines",   "--AALINES"],
}

# sequence of display
ObjectOrderDict = {
    ArgumentConstant.RECTANGLE.value : 0,
    ArgumentConstant.POLYGON.value   : 1,
    ArgumentConstant.CIRCLE.value    : 2,
    ArgumentConstant.ELLIPSE.value   : 3,
    ArgumentConstant.ARC.value       : 4,
    ArgumentConstant.LINE.value      : 5,
    ArgumentConstant.LINES.value     : 6,
    ArgumentConstant.AALINE.value    : 7,
    ArgumentConstant.AALINES.value   : 8,
}

class ShapeParamConstant(Enum):
    MAX_OBJECTS = 5
    NUM_SHAPES = len(ArgumentDict)
    SHAPE_HEIGHT = DisplayConstant.DISPLAY_HEIGHT.value // MAX_OBJECTS
    SHAPE_WIDTH = DisplayConstant.DISPLAY_WIDTH.value // NUM_SHAPES

FUNC = "FUNCTION"
ARGS = "ARGUMENTS"
FunctionArgumentDict = {
    ArgumentConstant.RECTANGLE.value: {FUNC: draw_rects, ARGS: [
        {
            # Width + Radius
            RectangleConstant.COLOR.value: ColorConstant.RED.value,
            RectangleConstant.RECT.value: Rect(
                ObjectOrderDict[ArgumentConstant.RECTANGLE.value] * ShapeParamConstant.SHAPE_WIDTH.value,
                0 * ShapeParamConstant.SHAPE_HEIGHT.value,
                ShapeParamConstant.SHAPE_WIDTH.value,
                ShapeParamConstant.SHAPE_HEIGHT.value,
            ),
            RectangleConstant.WIDTH.value: 10,
            RectangleConstant.BORDER.value: {
                RectangleConstant.BORDER_RADIUS.value: 10,
                RectangleConstant.BORDER_TL_RADIUS.value: 5,
            },
        },
        {
            # Width = 0
            RectangleConstant.COLOR.value: ColorConstant.WHITE.value,
            RectangleConstant.RECT.value: Rect(
                ObjectOrderDict[ArgumentConstant.RECTANGLE.value] * ShapeParamConstant.SHAPE_WIDTH.value,
                1 * ShapeParamConstant.SHAPE_HEIGHT.value,
                ShapeParamConstant.SHAPE_WIDTH.value,
                ShapeParamConstant.SHAPE_HEIGHT.value,
            ),
            RectangleConstant.WIDTH.value: 0,
        },
        {   
            # Border precedence over width
            RectangleConstant.COLOR.value: ColorConstant.BLUE.value,
            RectangleConstant.RECT.value: Rect(
                ObjectOrderDict[ArgumentConstant.RECTANGLE.value] * ShapeParamConstant.SHAPE_WIDTH.value,
                2 * ShapeParamConstant.SHAPE_HEIGHT.value,
                ShapeParamConstant.SHAPE_WIDTH.value,
                ShapeParamConstant.SHAPE_HEIGHT.value,
            ),
            RectangleConstant.WIDTH.value: 10,
            RectangleConstant.BORDER.value: {
                RectangleConstant.BORDER_RADIUS.value: 40,
                RectangleConstant.BORDER_TL_RADIUS.value: 5,
            },
        },
        {
            # No width, no radius
            RectangleConstant.COLOR.value: ColorConstant.MAGENTA.value,
            RectangleConstant.RECT.value: Rect(
                ObjectOrderDict[ArgumentConstant.RECTANGLE.value] * ShapeParamConstant.SHAPE_WIDTH.value,
                3 * ShapeParamConstant.SHAPE_HEIGHT.value,
                ShapeParamConstant.SHAPE_WIDTH.value,
                ShapeParamConstant.SHAPE_HEIGHT.value,
            ),
        },
        {
            # example
            RectangleConstant.COLOR.value: ColorConstant.GREEN.value,
            RectangleConstant.RECT.value: Rect(
                ObjectOrderDict[ArgumentConstant.RECTANGLE.value] * ShapeParamConstant.SHAPE_WIDTH.value,
                4 * ShapeParamConstant.SHAPE_HEIGHT.value,
                ShapeParamConstant.SHAPE_WIDTH.value,
                ShapeParamConstant.SHAPE_HEIGHT.value,
            ),
            RectangleConstant.WIDTH.value: 10,
            RectangleConstant.BORDER.value: {
                RectangleConstant.BORDER_RADIUS.value: 10,
            },
        },
    ]},
    ArgumentConstant.POLYGON.value   : {FUNC: lambda *_: None, ARGS: [

    ]},
    ArgumentConstant.CIRCLE.value    : {FUNC: lambda *_: None, ARGS: [

    ]},
    ArgumentConstant.ELLIPSE.value   : {FUNC: lambda *_: None, ARGS: [

    ]},
    ArgumentConstant.ARC.value       : {FUNC: lambda *_: None, ARGS: [

    ]},
    ArgumentConstant.LINE.value      : {FUNC: lambda *_: None, ARGS: [

    ]},
    ArgumentConstant.LINES.value     : {FUNC: lambda *_: None, ARGS: [

    ]},
    ArgumentConstant.AALINE.value    : {FUNC: lambda *_: None, ARGS: [

    ]},
    ArgumentConstant.AALINES.value   : {FUNC: lambda *_: None, ARGS: [

    ]},

}
    
