# File created by Isaac Leon 
WIDTH = 800
HEIGHT = 600
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
MOB_ACC = 2
MOB_FRICTION = -0.3
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False
# Starting platforms
# I amde a plat form and hcnaged their colors
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, RED, "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (200,200,200), "bouncey"),
                 (125, HEIGHT - 350, 100, 5, (200,200,200), "disappearing "),
# The platform on the right states that there is an opneining on the left side of the game 
# Disappearing = when I touvh it, it will magicaly disapear from existence. 
                 (350, 200, 100, 20, (200,200,200), "normal"), (100, HEIGHT - 100, WIDTH, 10, BLACK, "normal"), (500, HEIGHT - 500, WIDTH, 10, BLACK, "bouncey")]

platform_width = 200
platform_height = 50
platform_x = 0
platform_y = 400
platform_speed = 5
platform_rect = (platform_x, platform_y, platform_width, platform_height)
#PLATFORM_RECT_LIST = [platform_x, 0, platform_y, 400, platform_width, 200, platform_height, 50, BLACK, platform_speed, 5]




'''
A function that is associated with an object and called using dot notation.

#Method

The parent class from which behavior and properties are inherited.

#Superclass or Base-class

Provides a means of bundling data and functionality together. 

#Object

Creates a new type of object, allowing new instances of that type to be made.

#Class

Constructor method called when an object is created from a class, 
and it allows the class to initialize the attributes of the class.

#The __init__ method 


Parameter that is typically a reference to the current instance of the class 
and is used to access variables that belong to the class.

#'Self'


Class/Object property associated with parameter of class.

#Attribute

To create a new object from an existing Class.

#You need to instantiate the class using the class constructor.

'''