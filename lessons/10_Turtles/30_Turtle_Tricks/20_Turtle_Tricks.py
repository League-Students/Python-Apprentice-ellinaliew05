"""
# 20_Turtle_Tricks.py

In this assignment, you will use Tina the Turtle to draw a pentagon. 

- Each side of the pentagon should be a different color. 
- Use the turtle commands: tina.forward(), tina.left(), and tina.pencolor() to accomplish this.

Refer to the previous program, Meet_Tina.py, for examples of how to use turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600, 600, 0, 0)            # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
tina.speed(2)

tina.penup()
tina.goto(100,100)
tina.pendown()
tina.forward(100)

tina.pencolor('lightskyblue')
tina.left(70)
tina.forward(100)

tina.pencolor('deepskyblue')
tina.left(70)
tina.forward(100)

tina.pencolor('royalblue')
tina.left(75)
tina.forward(100)

tina.pencolor('darkblue')
tina.left(70)
tina.forward(110)
turtle.exitonclick()                    # Close the window when we click on it