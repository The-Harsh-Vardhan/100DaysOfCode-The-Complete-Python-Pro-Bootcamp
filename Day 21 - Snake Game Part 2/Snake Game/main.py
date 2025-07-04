import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=600, height=600)
my_screen.tracer(0)

my_snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    #Detect Collision with Food
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        scoreboard.increase_score()

    #Detect Collision with Wall
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect Collision with Tail
    for segment in my_snake.all_segments[2:]:
        if my_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

my_screen.exitonclick()