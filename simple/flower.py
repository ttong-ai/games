import turtle

turtle.setup(1000, 1000, 400, 0)

nathan = turtle.Pen()

nathan.color("red", "yellow")
nathan.width(2)
nathan.speed(0)


r = 0
step_r = 2.5
m, n = 1.9, 8

for i in range(150):
    nathan.down()
    nathan.begin_fill()
    nathan.circle(radius=5)
    nathan.end_fill()
    nathan.up()
    r = r + step_r
    nathan.forward(step_r)
    nathan.left(90)
    nathan.circle(r, extent=360 / n * m)
    nathan.right(90)

turtle.exitonclick()
