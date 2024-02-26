# Benedetto Aiello
# Cs 175 L
import turtle
dan = turtle.Turtle()
dan.shape('turtle')

distance = 50
sides = 8
# The angle we turn is related to the number of sides by this formula
angle = 360 / sides
my_color = "red"

dan.penup()
dan.goto(-50, 100)
dan.pendown()
dan.color(my_color)
dan.begin_fill()
# repeat the forward/right functions for each side
for i in range(sides):
   dan.forward(distance)
   dan.right(angle)

dan.end_fill()

dan.penup()
dan.goto(-57, 120)
distance += 20
dan.pensize(10)
dan.pendown()
dan.color(my_color)
# repeat the forward/right functions for each side
for i in range(sides):
   dan.forward(distance)
   dan.right(angle)

dan.hideturtle()

dan.penup()
dan.right(100)
dan.goto(-60,25)
dan.color('white')
dan.write('STOP', font=("Arial", 30, "normal"))
