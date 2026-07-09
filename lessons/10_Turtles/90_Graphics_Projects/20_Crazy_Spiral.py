"""
# 20_Crazy_Spiral.py

Make your own crazy spiral with a pattern like
in 10_Flaming_Ninja_Star.py, but use what you've learned about loops

uid: zfzMbyH7
name: Crazy Spiral
"""

import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]


def get_next_color(i):
    return colors[i % len(colors)]

turtle.setup(600, 600, 0, 0)            # Set the size of the window
window = turtle.Screen()

base_size = 200  # the size of the black part of the star
flame_size = 130  # the length of the flaming arms

t = turtle.Turtle()
t.shape("turtle")
t.width(2)
t.speed(0)

for i in range(20):
    t.pencolor('limegreen')
    t.fillcolor('greenyellow')
    t.begin_fill()
    t.forward(30)
    t.left(90)
    t.forward(flame_size)
    t.right(170)
    t.forward(flame_size)
    t.right(67)
    t.forward(base_size)
    t.end_fill()

for i in range(20):
    t.pencolor('darkgreen')
    t.fillcolor('forestgreen')
    t.begin_fill()
    t.forward(30)
    t.left(110)
    t.forward(flame_size)
    t.right(170)
    t.forward(flame_size)
    t.right(67)
    t.forward(base_size)
    t.end_fill()

for i in range(20):
    t.pencolor('midnightblue')
    t.fillcolor('deepskyblue')
    t.begin_fill()
    t.forward(30)
    t.left(130)
    t.forward(flame_size)
    t.right(170)
    t.forward(flame_size)
    t.right(67)
    t.forward(base_size)
    t.end_fill()

for i in range(20):
    t.pencolor('indigo')
    t.fillcolor('mediumorchid')
    t.begin_fill()
    t.forward(30)
    t.left(150)
    t.forward(flame_size)
    t.right(170)
    t.forward(flame_size)
    t.right(67)
    t.forward(base_size)
    t.end_fill()


t.hideturtle()

turtle.done()