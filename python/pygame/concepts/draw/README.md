Most of the functions take a width argument to represent the size of stroke (thickness) around the edge of the shape.

If a width of 0 is passed the shape will be filled (solid).

All the drawing functions respect the clip area for the surface and will be constrained to that area. 

The functions return a rectangle representing the bounding area of changed pixels. This bounding rectangle is the 'minimum' bounding box that encloses the affected area.

All the drawing functions accept a color argument that can be one of the following formats: a pygame.Color, an (RGB) triplet (tuple/list), an (RGBA) quadruplet (tuple/list), and an integer value that has been mapped to the surface's pixel format (see pygame.Surface.map_rgb()convert a color into a mapped color value and pygame.Surface.unmap_rgb()convert a mapped integer color value into a Color)