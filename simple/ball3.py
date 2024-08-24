"""Group of Bouncing Balls
Here we introduce a group of many bouncing balls and define a class Ball to introduce
Object Oriented Programming
"""

import tkinter as tk
import random
import time

WIDTH = 800
HEIGHT = 800

window = tk.Tk()
window.title("Pool game")
window.geometry(f"{WIDTH}x{HEIGHT}")
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

colors = [
    "red",
    "green",
    "blue",
    "orange",
    "yellow",
    "cyan",
    "magenta",
    "dodgerblue",
    "turquoise",
    "grey",
    "gold",
    "pink",
]


class Ball:
    def __init__(self, color, size):
        x0 = random.randrange(size, WIDTH - size)
        y0 = random.randrange(size, HEIGHT - size)
        self.shape = canvas.create_oval(x0, y0, x0 + size, y0 + size, fill=color)
        self.xspeed = random.randrange(-10, 10)
        self.yspeed = random.randrange(-10, 10)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[0] <= 0 or pos[2] >= WIDTH:
            self.xspeed = -self.xspeed
        if pos[1] <= 0 or pos[3] >= HEIGHT:
            self.yspeed = -self.yspeed


balls = []
for i in range(100):
    balls.append(Ball(random.choice(colors), random.randrange(0, 10)))

while True:
    for ball in balls:
        ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
