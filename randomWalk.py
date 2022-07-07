#CSCI 127
#Maya Carla Loletha Anderson

import turtle
import random

maya = turtle.Turtle()

for i in range(100):
    maya.forward(10)
    a = random.randrange(0, 360, 90)
    maya.right(a)
