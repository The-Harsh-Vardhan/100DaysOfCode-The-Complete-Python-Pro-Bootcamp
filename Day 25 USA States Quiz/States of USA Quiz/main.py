import turtle
import pandas as pd
import pygame

screen = turtle.Screen()
screen.title("USA States Quiz")

image = "blank_states_img.gif"
turtle.addshape(image)

map_turtle = turtle.Turtle()
map_turtle.shape(image)

df = pd.read_csv("50_states.csv")
states = df["state"]
states_list = states.to_list()
x_cor = df["x"]
x_cor_list = x_cor.to_list()
y_cor = df["y"]
y_cor_list = y_cor.to_list()

my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.color("Black")

# --- AUDIO SETUP ---
pygame.mixer.init()

# Background music
pygame.mixer.music.load("game-music.mp3")
pygame.mixer.music.play(loops=-1)  # Infinite loop

# Sound effects
level_up_sound = pygame.mixer.Sound("level-up.mp3")

guesses = 0
guessed_states = []
missed_states = []

while len(guessed_states) < 50:
    guess_state = screen.textinput(title=f"{len(guessed_states)} / 50 States Correct", prompt="What's another state's name?").title()
    if guess_state == "Exit":
        # list comprehension approach
        # missed_states = [state for state in states if state not in guessed_states]
        for state in states:
            if state not in guessed_states:
                missed_states.append(state)
        # Save the missing states to a csv file (learn.csv)
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv("learn.csv")
        screen.bye()
        break



    if guess_state not in guessed_states:
        for i in range(0, len(states_list)):
            if states[i] == guess_state:
                guessed_states.append(guess_state)
                level_up_sound.play()
                screen.title(f"USA States Quiz   {guesses} / 50")
                x_cor = x_cor_list[i]
                y_cor = y_cor_list[i]
                my_turtle.goto(x_cor, y_cor)
                my_turtle.write(f"{guess_state}", align="center", font=("Courier", 12, "normal"))

screen.mainloop()