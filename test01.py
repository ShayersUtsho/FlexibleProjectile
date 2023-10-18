class Arc:
    __color = (0, 0, 0)
    __center = {"x":0, "y":0}
    __radius = {"x":0, "y":0}
    __start_angle = 0
    __arc_angle = 0
    __end_angle = 360
    __line_thickness = 1
    __rectStart = (0, 0)
    __rectSize = (0, 0)
    __rectangle = (0, 0, 0, 0)
    __colorList = {
    "red": (255, 0, 0),         "green": (0, 255, 0),   "blue": (0, 0, 255),    "yellow": (255, 255, 0), "orange": (255, 165, 0),   "purple": (128, 0, 128),    "pink": (255, 192, 203),    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),   "lime": (0, 255, 0),    "brown": (139, 69, 19), "gray": (128, 128, 128), "black": (0, 0, 0),        "white": (255, 255, 255),   "silver": (192, 192, 192),  "gold": (255, 215, 0)}
    def __init__(self, color=(0, 0, 0), center=(0,0), centerPos="", radius=(0,0), angles=(-1,0,-1), lineThickness=0):
        pass
    def color(self, c):
        self.__color = self.__colorList.get(c, c)
    def center(self, x, y, pos=""):
        pass
    def radius(self, x, y=0):
        pass
    def angles(self, s, a=0, e=-1):
        pass
    def lineThicknes(self, t):
        pass
    def constructRectangle(self):
        pass
    def drawArc(self, screen):
        pass
    def returnColor(self):
        return self.__color

myArc = Arc()
myArc.color("red")
print(myArc.returnColor())
myArc.color((255, 255, 127))
print(myArc.returnColor())
input()
