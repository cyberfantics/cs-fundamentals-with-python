import turtle


scr = turtle.Screen()
scr.title("Triangle")

scr.bgcolor('black')
turtle.color('green')
turtle.pensize(5)

for i in range (3):
    turtle.forward(150)
    turtle.left(120)

turtle.exitonclick()

# Here is the easy way to understand it
# turtle.forward(150)
# turtle.left(120)
# turtle.forward(150)
# turtle.left(120)
# turtle.forward(150)
