import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("USA States Quiz")

image = "blank_states_img.gif"
turtle.addshape(image)

map_turtle = turtle.Turtle()
map_turtle.shape(image)

df = pd.read_csv("50_states.csv")
states_dict = df.to_dict()
print(states_dict)

my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.color("Black")

guesses = 0

while guesses < 50:
    guess_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    if states_dict["state"]  == guess_state:
        guesses += 1
        screen.title(f"USA States Quiz   {guesses} / 50")
        x_cor = x_cor_list[i]
        y_cor = y_cor_list[i]
        my_turtle.goto(x_cor, y_cor)
        my_turtle.write(f"{guess_state}", align="center", font=("Courier", 12, "normal"))

screen.mainloop()