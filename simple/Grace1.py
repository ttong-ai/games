import turtle

turtle.setup(500,500,400,0)

grace = turtle.Pen()

grace.color("green", "yellow")
grace.width(3)

for i in range(5):
    grace.forward(100)
    grace.left(-72)
    grace.rt(60)


turtle.exitonclick()