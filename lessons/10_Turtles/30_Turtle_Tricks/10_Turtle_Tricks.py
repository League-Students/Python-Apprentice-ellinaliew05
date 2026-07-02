"""
# 10_Turtle_Tricks.py

In this exercise, you will use Tina the Turtle to draw an equilateral triangle.

- Use the commands: tina.forward() and tina.left() to draw the three sides of the triangle.
- Change the pen color before drawing each side using tina.pencolor(), so each side is a different color.

Refer to previous turtle programs for examples of how to use these commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600, 600, 0, 0)            # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
tina.speed(1)

tina.penup()
tina.goto(100,100)
tina.pendown()
tina.forward(100)

tina.left(120)
tina.forward(100)

tina.left(120)
tina.forward(100)
turtle.exitonclick()                    # Close the window when we click on it