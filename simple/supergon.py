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


def supergon(n, edge, dir=0):
    seth(dir)
    for i in range(n):
        forward(edge)
        left(360 / n)


screensize(500, 500)
bgcolor("yellow")
width(5)
speed(10)

up()
goto(-200, 100)
down()
penfill("orange", "white")(circle)(120)
up()
goto(-220, 125)
down()
penfill("black", "black")(circle)(60)


up()
goto(200, 100)
down()
penfill("orange", "white")(circle)(120)
up()
goto(180, 125)
down()
penfill("black", "black")(circle)(60)

up()
goto(-50, -100)
down()
penfill("blue", "black")(supergon)(n=3, edge=100)

up()
goto(-200, -200)
seth(0)
down()
forward(400)

up()
goto(-450, -30)
penfill("blue", "orange")(supergon)(n=3, edge=100)
up()
goto(350, -30)
penfill("blue", "orange")(supergon)(n=3, edge=100)


exitonclick()
