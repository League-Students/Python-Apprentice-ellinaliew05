import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.speed(0)
tina.shape('turtle')
def fractal_octagon(size, depth): 
    if depth == 0:
        for i in range(8):
            tina.forward(size)
            tina.left(45)
    else:
        for i in range(8):
            fractal_octagon(size/2, depth-1)
            tina.forward(size)
            tina.left(45)

fractal_octagon(200, 5)


turtle.exitonclick()