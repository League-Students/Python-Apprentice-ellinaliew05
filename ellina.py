import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.speed (0)
tina.shape('turtle')


def fractal_triangle(size, depth):
    fractal_triangle(size/2, depth-1)
    tina.forward(size)
    tina.left(120)

def nudge(color):
    color += 1 + random.random() * 0.1 - 0.05
    return color % 1

def fractal cool