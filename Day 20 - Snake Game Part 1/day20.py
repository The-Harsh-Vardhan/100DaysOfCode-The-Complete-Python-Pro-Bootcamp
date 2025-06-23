import time
from turtle import Turtle, Screen
from snake import Snake

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=600, height=600)
my_screen.tracer(0)

my_snake = Snake()

my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()

my_screen.exitonclick()