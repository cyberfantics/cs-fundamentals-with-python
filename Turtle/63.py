'''  
Draw three squares in a row with a gap between each. 
Fill each square with a different colour.
'''

import turtle
scr = turtle.Screen()
scr.title("Three Filled Squares")
scr.bgcolor('black')
turtle.pensize(5)

colors = ['red', 'green', 'blue']
scolor = ['white', 'yellow', 'cyan']
square_size = 50
gap = 20

for idx, color in enumerate(colors):
    turtle.color(scolor[idx], color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(square_size)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.backward(square_size + gap)
    turtle.pendown()

turtle.exitonclick()
