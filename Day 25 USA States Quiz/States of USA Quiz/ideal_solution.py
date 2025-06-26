import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("USA States Quiz")

image = "blank_states_img.gif"
turtle.addshape(image)

map_turtle = turtle.Turtle()
map_turtle.shape(image)

my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.color("Black")

df = pd.read_csv("50_states.csv")
all_states = df["state"].to_list()

guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        for state in all_states:
            missed_states = []
            if state not in guessed_states:
                missed_states.append(state)
        # Save the missing states to a csv file (learn.csv)
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv("learn.csv")
        break

    if answer_state in all_states:  #Membership Function
        guessed_states.append(answer_state)
        state_data = df[df.state == answer_state]
        my_turtle.goto(state_data.x.item(), state_data.y.item())
        my_turtle.write(f"{answer_state}", align="center", font=("Courier", 12, "normal"))


screen.mainloop()