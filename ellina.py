import turtle

tina = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
tina.speed(0)
tina.shape('turtle')
def fractal_triacontagon(size, depth): 
    if depth == 0:
        for i in range(30):
            tina.forward(size)
            tina.left(90)
    else:
        for i in range(4):
            fractal_square(size/2, depth-1)
            tina.forward(size)
            tina.left(90)

fractal_square(200, 4)


turtle.exitonclick()