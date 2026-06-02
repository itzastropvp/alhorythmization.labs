import turtle
screen = turtle.Screen()
screen.bgcolor("lightyellow")
t = turtle.Turtle()
t.speed(0)
cell_size = 40
for row in range(4):
    for col in range(4):
        x = col * cell_size - 80
        y = 80 - row * cell_size
        t.penup()
        t.goto(x, y)
        t.pendown()
        if (row + col) % 2 == 0:
            t.fillcolor("white")
        else:
            t.fillcolor("gray")
        t.begin_fill()
        for _ in range(4):
            t.forward(cell_size)
            t.right(90)
        t.end_fill()
t.hideturtle()
turtle.done()