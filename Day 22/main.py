from turtle import  Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import pygame

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

my_turtle = Turtle(shape="square")
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.color("white")
my_turtle.pensize(5)
my_turtle.speed("fastest")
my_turtle.goto(0, 280)
my_turtle.setheading(270)

while my_turtle.ycor() > -270:
    my_turtle.forward(10)
    my_turtle.pendown()
    my_turtle.forward(10)
    my_turtle.penup()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()

screen.onkeypress(key="Up", fun = r_paddle.go_up)
screen.onkeypress(key="Down", fun = r_paddle.go_down)
screen.onkeypress(key="w", fun = l_paddle.go_up)
screen.onkeypress(key="s", fun = l_paddle.go_down)

game_is_on = True

# --- AUDIO SETUP ---
pygame.mixer.init()

# Background music
pygame.mixer.music.load("bgmusic.mp3")
pygame.mixer.music.play(loops=-1)  # Infinite loop

# Sound effects
hit_sound = pygame.mixer.Sound("hit.mp3")
miss_sound = pygame.mixer.Sound("miss.mp3")

while game_is_on:

    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with walls
    if ball.ycor() >= 280 or ball.ycor() < -280:
        ball.bounce_y()
        hit_sound.play()

    #Detect collision with Paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        hit_sound.play()

    #Detect Right Paddle Miss
    if ball.xcor() > 380:
        miss_sound.play()
        ball.reset_position()
        scoreboard.l_point()

    #Detect Left Paddle Miss
    if ball.xcor() < -380:
        miss_sound.play()
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()