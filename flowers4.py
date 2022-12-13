from turtle import *
import colorsys as col

speed(0)
bgcolor('black')
pensize(3)
hue = 0.0

for i in range(300):
    color = col.hsv_to_rgb(hue, 1, 1)
    pencolor(color)
    hue += 0.005
    right(i)
    circle(30, i)
    forward(i)
    left(91)

exitonclick()