import turtle


turtle.setup(800, 800, 400, 0)

nathan = turtle.Pen()

nathan.color("blue")
nathan.width(100)
nathan.speed(10)
for i in range(50):
     nathan.square(i * 5)
     nathan.left(50)

turtle.exitonclick()

turtle.done()