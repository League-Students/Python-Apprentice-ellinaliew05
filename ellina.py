import turtle

tina = turtle.Turtle()
screen = turtle.Screen()



def fractal_triangle(size, depth):
    fractal_triangle(size/2, depth-1)
    tina.forward(size)
    tina.left(120)

def nudge(color):
    color == 