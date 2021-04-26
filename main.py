import turtle

my_screen = turtle.Screen()
my_pen = turtle.Turtle()

#  Draws square with given radius


def square(side):
    for i in range(1, 5, 1):
        my_pen.forward(side)
        my_pen.right(90)


#  Draws circle with given radius

def circle(radius):
    my_pen.circle(radius=radius)

# Draws equilateral triangle with given side


def triangle(side):
    for i in range(1, 4, 1):
        my_pen.forward(side)
        my_pen.left(120)

# Draws regular hexagon given side


def hexagon(side):
    for i in range(1, 7, 1):
        my_pen.forward(side)
        my_pen.left(60)

# Draws regular shapes


def regular(sides, length):
    interior = ((sides - 2)*180)/sides
    for i in range(0, sides, 1):
        my_pen.forward(length)
        my_pen.left(180 - interior)


# Fibonacci Spiral

# 0 1 1 2 3 5 8
def fibonacci():
    a = 0
    b = 1
    for i in range(0, 20, 1):
        c = a + b
        a = b
        b = c
        my_pen.circle(radius=c, extent=90)


fibonacci()


turtle.done()


