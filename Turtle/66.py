import turtle, random

scr = turtle.Screen()

scr.title("Octogon")
scr.bgcolor("black")
turtle.pensize(5)

turtle.penup()
turtle.goto(0, -20)
turtle.pendown()

colors = ['red', 'green', 'blue', 'purple', 'white', 'orange']

for _ in range(8):
    turtle.color(random.choice(colors))
    turtle.forward(100)
    turtle.left(45)

turtle.exitonclick()
