import pygame
import sys
import math

from win32api import GetAsyncKeyState as keypress
arrow = {'left':0x25, 'up':0x26, 'right':0x27, 'down':0x28}

class Arc:
    __color = (0, 0, 0)
    __center = {"x":0, "y":0}
    __radius = {"x":0, "y":0}
    __start_angle = 0
    __arc_angle = 0
    __end_angle = 360
    __line_thickness = 1
    __rectStart = {"x":0, "y":0}
    __rectSize = {"x":0, "y":0}
    __rectangle = (0, 0, 0, 0)
    __colorList = {
    "red": (255, 0, 0),         "green": (0, 255, 0),   "blue": (0, 0, 255),    "yellow": (255, 255, 0), "orange": (255, 165, 0),   "purple": (128, 0, 128),    "pink": (255, 192, 203),    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),   "lime": (0, 255, 0),    "brown": (139, 69, 19), "gray": (128, 128, 128), "black": (0, 0, 0),        "white": (255, 255, 255),   "silver": (192, 192, 192),  "gold": (255, 215, 0)}
    
    def __init__(self, color=(0, 0, 0), center=(0,0), centerPos="", radius=(0,0), angles=(-1,0,-1), lineThickness=0):
        pass
    def color(self, c):
        self.__color = self.__colorList.get(c, c)
        
    def center(self, x, y):
        self.__center["x"] = x
        self.__center["y"] = y
        
    def radius(self, x, y=0):
        self.__radius["x"] = x
        if y:
            self.__radius["y"] = y
        else:
            self.__radius["y"] = x
            
    def angles(self, s, a=0, e=-1):
        self.__start_angle = s
        if a:
            self.__arc_angle = a
            self.__end_angle = s + a
        else:
            self.__end_angle = e
            self.__arc_angle = e - s
            
    def lineThicknes(self, t):
        self.__line_thickness = t
        
    def constructRectangle(self):
        self.__rectStart["x"] = self.__center["x"] - self.__radius["x"]
        self.__rectStart["y"] = self.__center["y"] - self.__radius["y"]
        self.__rectSize["x"] = self.__radius["x"] * 2
        self.__rectSize["y"] = self.__radius["y"] * 2
        
        self.__rectangle = (self.__rectStart["x"], self.__rectStart["y"], self.__rectSize["x"], self.__rectSize["y"])
        
    def drawArc(self, screen):
        pygame.draw.arc(screen, self.__color, self.__rectangle, math.radians(self.__start_angle), math.radians(self.__end_angle), self.__line_thickness)


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
