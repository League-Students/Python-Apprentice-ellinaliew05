import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.speed ()



def fractal_triangle(size, depth):
    fractal_triangle(size/2, depth-1)
    tina.forward(size)
    tina.left(120)

def nudge(color):
    color == 