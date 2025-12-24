import turtle

scr = turtle.Screen()
scr.bgcolor('black')
scr.title("Circle")
turtle.color('green')
turtle.pensize(5)

radius = 75
circumference = 2 * 3.14 * radius

for i in range(360):
    turtle.forward(circumference / 360)
    turtle.left(1)

turtle.exitonclick()
