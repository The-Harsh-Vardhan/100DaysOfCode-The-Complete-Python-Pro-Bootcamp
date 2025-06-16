import random
import art

print(art.logo)
print("Welcome to My Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(0,100)

print(f"Pssst, the correct answer is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts_left = 0
if difficulty == "easy":
    attempts_left = 10
elif difficulty == "hard":
    attempts_left = 5

game_over = False
while not game_over:
    print(f"You have {attempts_left} remaining to guess the game")
    guess = int(input("Make a Guess: "))
    attempts_left -= 1
    if guess == number:
        print(f"You won! The number was {number}")
        game_over = True
    elif guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")