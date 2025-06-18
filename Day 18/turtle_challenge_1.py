# Draw a Square
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.color("red")
my_turtle.shape("turtle")

for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

screen = Screen()
screen.exitonclick()