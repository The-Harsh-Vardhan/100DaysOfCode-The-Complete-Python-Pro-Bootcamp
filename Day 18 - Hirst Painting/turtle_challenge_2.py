#Draw a dashed line
from turtle import Turtle, Screen
my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

for _ in range(15):
    my_turtle.pendown()
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)

my_screen = Screen()
my_screen.exitonclick()