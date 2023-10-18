import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 400, 400

# Create a display window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing a Circular Arc")

# Colors
black = (0, 0, 0)
red = (255, 0, 0)

# Define the parameters for the circular arc
center = (200, 200)  # Center coordinates of the circle
radius = 100
start_angle = 45  # Starting angle in degrees
end_angle = start_angle + 90  # Ending angle in degrees
line_thickness = 1

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Draw the circular arc
    # dimensions of rectangular box
    rectangleStartingX = center[0] - radius
    rectangleStartingY = center[1] - radius
    rectangleWidth = radius * 2
    rectangleHeight = radius * 2
    pygame.draw.arc(screen, red, (rectangleStartingX, rectangleStartingY, rectangleWidth, rectangleHeight), 
                    math.radians(start_angle), math.radians(end_angle), line_thickness)

    # Draw lines to connect the ends of the arc to the center, creating a circular arc
    start_x = center[0] - radius * math.cos(math.radians(start_angle))
    start_y = center[1] - radius * math.sin(math.radians(start_angle))
    end_x = center[0] - radius * math.cos(math.radians(end_angle))
    end_y = center[1] - radius * math.sin(math.radians(end_angle))
    pygame.draw.line(screen, red, center, (start_x, start_y), line_thickness)
    pygame.draw.line(screen, red, center, (end_x, end_y), line_thickness)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
