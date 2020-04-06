import turtle


turtle.setup(800, 800, 400, 0)

nathan = turtle.Pen()

nathan.color("blue")
nathan.width(2)
nathan.speed(0)
for i in range(50):
     nathan.circle(i * 5)
     nathan.left(10)

turtle.exitonclick()
