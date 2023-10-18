import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 400, 400

# Create a display window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing an Arc")

# Colors
black = (0, 0, 0)
red = (255, 0, 0)

# Define the parameters for the arc
rect = (0, 0, 200, 200)  # (x, y, width, height)
start_angle = 45  # Starting angle in degrees
end_angle = 90  # Ending angle in degrees

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Draw the red arc
    pygame.draw.arc(screen, red, rect, start_angle, end_angle, 1)  # 5 is the width of the arc line

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
