from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.speed("fast")

def move_forward():
    my_turtle.forward(10)

def move_backward():
    my_turtle.backward(10)

def turn_right():
    my_turtle.right(10)

def turn_left():
    my_turtle.left(10)

def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

my_screen = Screen()
my_screen.listen()
my_screen.onkeypress(key="w", fun=move_forward)
my_screen.onkeypress(key="s", fun=move_backward)
my_screen.onkeypress(key="d", fun=turn_right)
my_screen.onkeypress(key="a", fun=turn_left)
my_screen.onkeypress(key="c", fun=clear)

my_screen.exitonclick()