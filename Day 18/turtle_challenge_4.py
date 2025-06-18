import turtle as t
import random

my_turtle = t.Turtle()
my_turtle.speed("fastest")
my_turtle.width(8)

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def move():
    random_color = random.choice(colors)
    my_turtle.color(random_color)
    directions = [0 , 90, 180, 270]
    random_direction = random.choice(directions)
    my_turtle.forward(10)
    my_turtle.setheading(random_direction)

for _ in range(200):
    move()