import turtle

scr = turtle.Screen()

scr.title("Pattern")
scr.bgcolor("black")
turtle.pensize(3)

turtle.color('green')

for _ in range (10):
    for _ in range(8):
        turtle.forward(50)
        turtle.right(45)

    turtle.left(36)

turtle.exitonclick()