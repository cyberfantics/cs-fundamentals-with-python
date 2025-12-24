import turtle


scr = turtle.Screen()
scr.title("Star")

scr.bgcolor('black')
turtle.color('green')
turtle.pensize(5)

for i in range (5):
    turtle.forward(150)
    turtle.left(144)

turtle.exitonclick()