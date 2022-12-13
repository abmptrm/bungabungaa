import turtle
import colorsys as color

turtle.bgcolor('#f1f1f1')
turtle.pencolor('#54b4ae')
turtle.speed(0)
turtle.tracer(100)
turtle.pensize(1)
# turtle.goto(0,0)

color = ('#003049', '#d62828', '#f77f00', '#fcbf49', '#eae2b7')

for i in range(4):
    for j in range(400):
        turtle.color(color[j%4])
        turtle.circle(190 - j/2, 90)
        turtle.left(90)
        turtle.circle(190 - j/2, 90)
        turtle.color(color[j%4])
    turtle.left(35)
    
turtle.exitonclick()

