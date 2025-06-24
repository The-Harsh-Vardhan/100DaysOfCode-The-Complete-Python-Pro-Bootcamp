import time
import pygame
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.title("Improved Snake Game")
my_screen.setup(width=600, height=600)
my_screen.tracer(0)

my_snake = Snake()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(my_snake.up, "w")
my_screen.onkey(my_snake.down, "s")
my_screen.onkey(my_snake.left, "a")
my_screen.onkey(my_snake.right, "d")

# --- AUDIO SETUP ---
pygame.mixer.init()

# Background music
pygame.mixer.music.load("snake_game_bgmusic.mp3")
pygame.mixer.music.play(loops=-1)  # Infinite loop

# Sound effects
level_up_sound = pygame.mixer.Sound("level-up.mp3")
game_over_sound = pygame.mixer.Sound("game-over-arcade.mp3")

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
        level_up_sound.play()

    #Detect Collision with Wall
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        scoreboard.reset()
        my_snake.reset()
        food.refresh()
        game_over_sound.play()

    #Detect Collision with Tail
    for segment in my_snake.all_segments[2:]:
        if my_snake.head.distance(segment) < 10:
            scoreboard.reset()
            food.refresh()
            my_snake.reset()
            game_over_sound.play()

my_screen.exitonclick()