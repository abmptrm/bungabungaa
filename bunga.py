import turtle
import colorsys as color

turtle.bgcolor('black')
turtle.tracer(30)

x = 20

for i in range(100):
    warna = color.hsv_to_rgb(x, 1, 1)
    x +=  0.020
    turtle.color(warna)
    turtle.pensize(3)
    turtle.goto(0,0)
    turtle.circle(i)
    turtle.lt(160)
    turtle.circle(i)
    turtle.lt(160)
  



turtle.done()