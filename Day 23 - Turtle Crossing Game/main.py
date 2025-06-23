from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time
import pygame

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="w", fun=player.move)

# --- AUDIO SETUP ---
pygame.mixer.init()

# Background music
pygame.mixer.music.load("turtle-crossing-bgmusic.mp3")
pygame.mixer.music.play(loops=-1)  # Infinite loop

# Sound effects
level_up_sound = pygame.mixer.Sound("level-up.mp3")
game_over_sound = pygame.mixer.Sound("game-over-arcade.mp3")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_new_car()
    car_manager.move_all_cars()

    #Detect win level
    if player.ycor() > 280.0:
        player.restart()
        scoreboard.increase_level()
        car_manager.increase_speed()
        level_up_sound.play()

    #Detect Collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            game_over_sound.play()

screen.exitonclick()