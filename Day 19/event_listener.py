from turtle import Turtle, Screen

my_turtle = Turtle()

def move_forward():
    my_turtle.forward(10)

my_screen = Screen()
my_screen.listen()
my_screen.onkeypress(key = "space", fun=move_forward)
my_screen.exitonclick()