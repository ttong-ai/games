"""Two Bouncing Balls
Here we introduce two bouncing balls
"""

import tkinter as tk
import random
import time

window = tk.Tk()
window.title("Bouncing Ball")
window.geometry("500x500")
width = 500
height = 500
canvas = tk.Canvas(window, width=width, height=height)
canvas.pack()

ball = canvas.create_oval(10, 10, 60, 60, fill="orange")
xspeed = 4
yspeed = 5

ball2 = canvas.create_oval(10, 10, 60, 60, fill="blue")
xspeed2 = -5
yspeed2 = -4

while True:
    canvas.move(ball, xspeed, yspeed)
    pos = canvas.coords(ball)
    if pos[3] >= height or pos[1] <= 0:
        yspeed = -yspeed
    if pos[2] >= width or pos[0] <= 0:
        xspeed = -xspeed

    canvas.move(ball2, xspeed2, yspeed2)
    pos = canvas.coords(ball2)
    if pos[3] >= height or pos[1] <= 0:
        yspeed2 = -yspeed2
    if pos[2] >= width or pos[0] <= 0:
        xspeed2 = -xspeed2
    window.update()
    time.sleep(0.01)

window.mainloop()
