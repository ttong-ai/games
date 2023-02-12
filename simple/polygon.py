import turtle
from turtle import *

fred = turtle.Pen()

fred.color("green")
fred.color("green", "red")
fred.speed(0)
for i in range(50):
    fred.circle(i * 3)
    fred.left(11120)
done()
