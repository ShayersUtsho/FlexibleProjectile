import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the square
width, height = 200, 200
square_color = (0, 0, 0)  # Black

# Set the initial position of the red dot (in pixel coordinates)
dot_color = (0, 0, 0)  # Red
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
    screen.set_at(dot_position, dot_color)

    # Update the display
    pygame.display.flip()
    pixel_color = screen.get_at((100, 100))

    print(f"Color at (100, 100): {pixel_color}")
# Quit Pygame
pygame.quit()
sys.exit()
