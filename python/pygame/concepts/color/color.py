import pygame

if __name__ == '__main__':
    pygame.init()

    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame Color Class Examples")

    color_rgba = pygame.Color(255, 0, 0, 128)  # Semi-transparent red
    color_hex = pygame.Color("#00FF00")  # Green
    color_name = pygame.Color("blue") 

    # color_hsva = pygame.Color(255, 0, 0)  # Red
    # color_hsva.hsva = (240, 100, 100, 255)  # Adjust hue to create a blue color

    # color_hsla = pygame.Color(255, 0, 0)  # Red
    # color_hsla.hsla = (120, 100, 50, 255)  # Adjust hue to create a green color

    # Interpolation between colors
    color1 = pygame.Color(255, 0, 0)  # Red
    color2 = pygame.Color(0, 0, 255)  # Blue
    mid_color = color1.lerp(color2, 0.5)  # Midway between red and blue

    screen.fill((255, 255, 255))

    font = pygame.font.Font(None, 36)

    pygame.draw.rect(screen, color_rgba, pygame.Rect(50, 50, 150, 150))
    screen.blit(font.render("RGBA: Red (50% opacity)", True, (0, 0, 0)), (210, 100))

    pygame.draw.rect(screen, color_hex, pygame.Rect(50, 220, 150, 150))
    screen.blit(font.render("Hex: Green", True, (0, 0, 0)), (210, 270))

    pygame.draw.rect(screen, color_name, pygame.Rect(50, 390, 150, 150))
    screen.blit(font.render("Name: Blue", True, (0, 0, 0)), (210, 440))

    pygame.draw.rect(screen, mid_color, pygame.Rect(600, 275, 150, 150))
    screen.blit(font.render("Lerp: Mid Red-Blue", True, (0, 0, 0)), (385, 325))

    pygame.display.flip()

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(1)

    pygame.quit()
