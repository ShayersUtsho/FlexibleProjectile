import pygame
import sys
import math

from win32api import GetAsyncKeyState as keypress
arrow = {'left':0x25, 'up':0x26, 'right':0x27, 'down':0x28}

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
arc_length = 90
end_angle = start_angle + arc_length  # Ending angle in degrees
line_thickness = 1

# Main game loop
running = True
keypresscount = {'right' : 0, 'left' : 0}
while running:
    if keypress(arrow['right']) and keypresscount['right'] < 1:
        keypresscount['right'] += 100
        start_angle -= 1
        end_angle = start_angle + arc_length
    else:
        keypresscount['right'] -= 1
        
    if keypress(arrow['left']) and keypresscount['left'] < 1:
        keypresscount['left'] += 100
        start_angle +0= 1
        end_angle = start_angle + arc_length
    else:
        keypresscount['left'] -= 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # dimensions of rectangular box containing arc
    rectangleStartingX = center[0] - radius
    rectangleStartingY = center[1] - radius
    rectangleWidth = radius * 2
    rectangleHeight = radius * 2
    rectangle = (rectangleStartingX, rectangleStartingY, rectangleWidth, rectangleHeight)
    
    # Draw the circular arc
    pygame.draw.arc(screen, red, rectangle, math.radians(start_angle), math.radians(end_angle), line_thickness)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
