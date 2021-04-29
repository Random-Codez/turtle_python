import turtle

my_screen = turtle.Screen()
my_screen.bgcolor('black')
my_pen = turtle.Turtle()

def circle(radius):
    my_pen.speed(20)
    my_pen.pencolor('white')
    for i in range(0, 360, 1):
        my_pen.circle(radius=radius)
        my_pen.right(1)

def sea_shell():
    my_pen.speed(20)
    my_pen.pencolor('white')
    for i in range(0, 360, 1):
        my_pen.circle(i)
        my_pen.right(1)


def colour_spiral(radius):
    my_pen.speed(20)
    for i in range(0, 9, 1):
        for color in ('red', 'green', 'blue', 'white'):
            my_pen.circle(radius=radius)
            my_pen.pencolor(color)
            my_pen.right(10)

def tree_pattern():
    turtle.tracer(0)
    my_pen.speed(20)
    my_pen.pencolor('white')
    my_pen.left(90)
    for i in range(0, 4, 1):
        my_pen.forward(10)
        for l in range(0, 2, 1):
            my_pen.left(40)
            my_pen.forward(10)
            for m in range(0, 2, 1):
                my_pen.left(40)
                my_pen.forward(10)
                tree()
                my_pen.backward(10)
                my_pen.right(80)
                my_pen.forward(10)
                tree()
                my_pen.backward(10)
                my_pen.left(40)
            tree()
            my_pen.backward(10)
            my_pen.right(80)
            my_pen.forward(10)
            for n in range(0, 2, 1):
                my_pen.left(40)
                my_pen.forward(10)
                tree()
                my_pen.backward(10)
                my_pen.right(80)
                my_pen.forward(10)
                tree()
                my_pen.backward(10)
                my_pen.left(40)
            tree()
            my_pen.backward(10)
            my_pen.left(40)
        my_pen.backward(10)
        my_pen.right(90)

def tree():
    for m in range(0, 2, 1):
        my_pen.left(40)
        my_pen.forward(10)
        my_pen.backward(10)
        my_pen.right(80)
        my_pen.forward(10)
        my_pen.backward(10)
        my_pen.left(40)

colour_spiral(100)

turtle.done()