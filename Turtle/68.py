'''
Draw a pattern that will change each time the 
program is run. Use the random function to pick 
the number of lines, the length of each line and 
the angle of each turn. 
'''

import turtle, random

scr = turtle.Screen()

scr.title("Pattern")
scr.bgcolor("black")
turtle.pensize(3)

no_of_lines = random.randint(6, 15)
colors = ['red', 'green', 'blue', 'orange', 'white', 'yellow']

for _ in range(no_of_lines):
    length_of_lines = random.randint(30, 90)
    angle_of_line = random.randint(30, 180)
    
    turtle.color(random.choice(colors))
    turtle.forward(length_of_lines)
    turtle.right(angle_of_line) 

turtle.exitonclick()