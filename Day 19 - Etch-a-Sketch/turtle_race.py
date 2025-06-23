from turtle import Turtle, Screen
import random

is_race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make a bet!", prompt="Which turtle is going to win the race? Enter a color: ")
colors = ["red" , "orange" , "yellow" , "green" , "blue" , "purple"]
y_positions = [100, 60, 20, -20, -60, -100]
all_turtles = []

for turtle_index in range(0,6):
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(colors[turtle_index])
    my_turtle.penup()
    my_turtle.goto(x = -230, y = y_positions[turtle_index])
    all_turtles.append(my_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won!! The winner is {winning_color}")
            else:
                print(f"You have lost!! The winner is {winning_color}")
        random_distance = random.randint(0,10) #Since the randint is inclusive so 10 is included
        turtle.forward(random_distance)

my_screen.exitonclick()