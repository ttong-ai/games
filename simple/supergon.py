from turtle import *


def penfill(c="black", f="white"):
    import turtle as t

    def real_decorator(function):
        def wrapper(*args, **kwargs):
            original_speed = t.speed()
            t.speed(0)
            t.color(c, f)
            t.begin_fill()
            function(*args, **kwargs)
            t.end_fill()
            t.speed(original_speed)

        return wrapper

    return real_decorator


class Eye(Turtle):
    pass


def supergon(n, edge, dir=0):
    seth(dir)
    for i in range(n):
        forward(edge)
        left(360 / n)


screensize(500, 700)
bgcolor("yellow")
width(5)
speed(10)

# Left eye
up()
goto(-200, 50)
down()
penfill("orange", "white")(circle)(120)
up()
goto(-220, 125)
down()
penfill("blue", "black")(circle)(60)

# Right eye
up()
goto(200, 50)
down()
penfill("orange", "white")(circle)(120)
up()
goto(180, 125)
down()
penfill("blue", "black")(circle)(60)

up()
goto(-50, -100)
down()
penfill("blue", "red")(supergon)(n=3, edge=100)

up()
goto(-250, -200)
seth(0)
down()
color("purple", "red")
begin_fill()
forward(500)
right(150)
circle(-500, 60)
end_fill()

up()
goto(-400, 350)
seth(0)
down()
color("black", "black")
begin_fill()
forward(800)
left(150)
circle(800, 60)
end_fill()

up()
goto(-450, -30)
penfill("blue", "orange")(supergon)(n=3, edge=100)
up()
goto(350, -30)
penfill("blue", "orange")(supergon)(n=3, edge=100)


exitonclick()
