import turtle
import colorsys as color

turtle.bgcolor('black')
turtle.tracer(3)

x = 20
for i in range(300):
    warna = color.hsv_to_rgb(x, 1, 1)
    x +=  0.020
    turtle.color(warna)
    turtle.pensize(3)
    turtle.goto(0,0)
    turtle.circle(i, extent=100)
    turtle.lt(80)
    turtle.circle(i, extent=100)   

turtle.exitonclick()

