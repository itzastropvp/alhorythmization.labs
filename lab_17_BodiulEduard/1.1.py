import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
corners = [(-60, 60), (60, 60), (60, -60), (-60, -60)]
colors = ["red", "blue", "black", "green"]
t.penup()
t.goto(corners[0])
t.pendown()
for i in range(4):
    t.pencolor(colors[i])
    t.goto(corners[(i + 1) % 4])
ray_colors = ["red", "blue", "black", "green"]
for i in range(4):
    t.penup()
    t.goto(0, 0)  # центр квадрата
    t.pendown()
    t.pencolor(ray_colors[i])
    t.goto(corners[i])
turtle.done()