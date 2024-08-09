import pygame
from enum import Enum

class RectangleConstant(Enum):
    DEFAULT_WIDTH = 0
    DEFAULT_BORDER = dict()
    DEFAULT_BORDER_RADIUS = -1
    BORDER_RADIUS = "border_radius"
    BORDER_TL_RADIUS = "border_top_left_radius"
    BORDER_TR_RADIUS = "border_top_right_radius"
    BORDER_BL_RADIUS = "border_bottom_left_radius"
    BORDER_BR_RADIUS = "border_bottom_right_radius"

    COLOR = "COLOR"
    RECT = "RECT"
    WIDTH = "WIDTH"
    BORDER = "BORDER"

def draw_rect(surface, color, rect, width=RectangleConstant.DEFAULT_WIDTH.value, **border):
    return pygame.draw.rect(
        surface=surface,
        color=color,
        rect=rect,
        width=width,
        border_radius=border.get(RectangleConstant.BORDER_RADIUS.value, RectangleConstant.DEFAULT_BORDER_RADIUS.value),
        border_top_left_radius=border.get(RectangleConstant.BORDER_TL_RADIUS.value, RectangleConstant.DEFAULT_BORDER_RADIUS.value),
        border_top_right_radius=border.get(RectangleConstant.BORDER_TR_RADIUS.value, RectangleConstant.DEFAULT_BORDER_RADIUS.value),
        border_bottom_left_radius=border.get(RectangleConstant.BORDER_BL_RADIUS.value, RectangleConstant.DEFAULT_BORDER_RADIUS.value),
        border_bottom_right_radius=border.get(RectangleConstant.BORDER_BR_RADIUS.value, RectangleConstant.DEFAULT_BORDER_RADIUS.value),
    )

def draw_rects(surface, rects):
    for rect in rects:
        draw_rect(
            surface,
            rect[RectangleConstant.COLOR.value],
            rect[RectangleConstant.RECT.value],
            width=rect.get(RectangleConstant.WIDTH.value, RectangleConstant.DEFAULT_WIDTH.value),
            border=rect.get(RectangleConstant.BORDER.value, RectangleConstant.DEFAULT_BORDER.value),
        )
