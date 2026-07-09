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
            tina.left()
    else:
        for i in range(30):
            fractal_triacontagon(size/2, depth-1)
            tina.forward(size)
            tina.left(90)

fractal_triacontagon(200, 4)


turtle.exitonclick()