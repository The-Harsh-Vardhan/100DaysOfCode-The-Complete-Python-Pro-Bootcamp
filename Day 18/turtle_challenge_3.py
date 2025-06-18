# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

import turtle as t
import random
my_turtle = t.Turtle()
my_turtle.shape("turtle")

colours = ["CornflowerBlue", "Darkorchid", "IndianRed", "DeepSkyBIue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)

for shape_side in range(3, 11):
    my_turtle.color(random.choice(colours))
    draw_shape(shape_side)