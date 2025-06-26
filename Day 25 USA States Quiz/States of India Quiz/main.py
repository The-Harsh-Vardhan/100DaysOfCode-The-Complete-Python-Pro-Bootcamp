import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Indian States Quiz")

image = "map_of_india.gif"
turtle.addshape(image)

map_turtle = turtle.Turtle()
map_turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.color("Black")

df = pd.read_csv("india_states.csv")
all_states = df["state"].to_list()

guessed_states = []
missed_states = []

while len(guessed_states) < 30:
    guess_state = screen.textinput(title=f"{len(guessed_states)} / 30 States Correct", prompt="What's another state's name?").title()

    if guess_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
                new_data = pd.DataFrame(missed_states)
                new_data.to_csv("learn.csv")
        break

    if guess_state in all_states and guess_state not in guessed_states:
        guessed_states.append(guess_state)
        my_state = df[df.state == guess_state]
        t.goto(my_state.x.item(), my_state.y.item())
        t.write(f"{guess_state}", align = "center", font=("Courier", 12, "normal"))

screen.mainloop()