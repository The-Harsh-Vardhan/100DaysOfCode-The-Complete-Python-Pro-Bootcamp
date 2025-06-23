import turtle as t
import random

my_turtle = t.Turtle()
my_turtle.speed("fastest")
my_turtle.width(10)
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_color = (r, g, b)
    return my_color

def move():
    my_turtle.color(random_color())
    directions = [0 , 90, 180, 270]
    random_direction = random.choice(directions)
    my_turtle.forward(30)
    my_turtle.setheading(random_direction)

for _ in range(200):
    move()