import pygame
import sys
from math import sin, cos

# Initialize Pygame
pygame.init()

# Set the dimensions of the square
width, height = 200, 200
square_color = (0, 0, 0)  # Black

# Set the initial position of the red dot (in pixel coordinates)
dot_color = (255, 0, 0)  # Red
dot_position = (100, 100)

# Create a display window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Red Pixel Dot on Square")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(square_color)

    # Draw the red dot as a single pixel
    for x in range(width):
        for y in range(height):
            dot_position = (x, y)
            h, k = 100, 100
            r = 90
            a = 90
            if x == h + r * cos(a) and y == k + r * sin(a):
                screen.set_at(dot_position, dot_color)

    # Update the display
    pygame.display.flip()
    
# Quit Pygame
pygame.quit()
sys.exit()
