import colorgram
import turtle as t
import random

def extract_colors():
    rgb_colors = []
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    print(rgb_colors)

color_list = [ (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86),
               (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
               (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

my_turtle = t.Turtle()
my_turtle.hideturtle()
my_turtle.speed("fastest")
t.colormode(255)

def print_row():
    for _ in range(10):
        random_color = random.choice(color_list)
        my_turtle.color()
        my_turtle.pendown()
        my_turtle.dot(20, random_color)
        my_turtle.penup()
        my_turtle.forward(30)
    my_turtle.left(90)
    my_turtle.forward(30)
    y_position = my_turtle.ycor()
    my_turtle.teleport(0, y_position+1)
    my_turtle.right(90)

for i in range(10):
    print_row()

my_screen = t.Screen()
my_screen.exitonclick()