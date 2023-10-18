import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the square
width, height = 1024, 1024 
square_color = (0, 0, 0)  # Black

# Set the initial position of the red dot (in pixel coordinates)
dot_color = (0, 0, 0)  # Red
dot_position = (100, 100)

# Create a display window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Red Pixel Dot on Square")

for x in range(width):
    for y in range(height):
        # Generate a random number between 0 and 255
        if (x - 512)**2 + (y - 512)**2 > 512**2:
            screen.set_at((x, y), (64, 128, 255))

# Main game loop
running = True
i = 0
j = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()
    pixel_color = dict()
    for x in range(width):
        for y in range(height):
            pixel_color[(x, y)] = screen.get_at((x, y))
    
    i += 1
    i = 0
    j *= 2
    
    for x in range(0, width, j):
        for y in range(0, height, j):
            rSum = 0
            for xi in range(j):
                for yi in range(j):
                    rSum += pixel_color[(x+xi, y+yi)][0]
            r = rSum//(j*j)
            
            gSum = 0
            for xi in range(j):
                for yi in range(j):
                    gSum += pixel_color[(x+xi, y+yi)][1]
            g = gSum//(j*j)
            
            bSum = 0
            for xi in range(j):
                for yi in range(j):
                    bSum += pixel_color[(x+xi, y+yi)][2]
            b = bSum//(j*j)
            
            for xi in range(j):
                for yi in range(j):
                    pixel_color[(x+xi, y+yi)] = (r, g, b)
    for x in range(width):
        for y in range(height):
            screen.set_at((x, y), (pixel_color[(x, y)][0], pixel_color[(x, y)][1], pixel_color[(x, y)][2]))


# Quit Pygame
pygame.quit()
sys.exit()
