import random
import art

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def choose_difficulty():
    """This function let the user choose the difficulty of the Game"""
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if diff == "easy":
        return EASY_ATTEMPTS
    elif diff == "hard":
        return HARD_ATTEMPTS
    return None

def check_answer(guess, number, attempts):
    """Check answer against guess and return Number of Attempts Remaining"""
    if guess == number:
        print(f"You won! The number was {number}")
        return
    elif guess > number:
        print("Too High\nGuess Again!")
        return attempts- 1
    elif guess < number:
        print("Too Low\nGuess Again!")
        return attempts - 1
    return None

def play_game():
    """This function is used to Start the Game"""
    print(art.logo)
    print("Welcome to My Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    actual_number = random.randint(1, 100)
    print(f"Pssst, the correct answer is {actual_number}")

    attempts_left = choose_difficulty()

    guess = int(input("Make a Guess: "))
    while guess != actual_number:
        print(f"You have {attempts_left} remaining to guess the game")
        if attempts_left == 0:
            return None
        attempts_left = check_answer(guess, actual_number, attempts_left)
    return None

play_game()