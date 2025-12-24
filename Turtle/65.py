import turtle
scr = turtle.Screen()
scr.title("Numbers in Vertical Sequence")
scr.bgcolor('black')
turtle.pensize(5)

turtle.color('white')
turtle.penup()
turtle.goto(0, 50)

# Drawing number 1
turtle.pendown()
turtle.left(90)
turtle.forward(150)

# Drawing number 2
turtle.penup()
turtle.goto(30, 200)
turtle.pendown()

turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(100)


turtle.penup()
turtle.goto(150, 200)
turtle.pendown()

# Drawing number 3
turtle.forward(100) 
turtle.right(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(80)
turtle.backward(80)
turtle.left(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(100)

turtle.exitonclick()
