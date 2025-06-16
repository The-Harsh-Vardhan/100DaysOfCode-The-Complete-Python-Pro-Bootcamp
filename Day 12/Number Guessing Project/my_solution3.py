import random
import art

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
def choose_difficulty():
    """This function lets the user choose the difficulty of the game"""
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if diff == "easy":
        return EASY_ATTEMPTS
    elif diff == "hard":
        return HARD_ATTEMPTS
    else:
        print("Invalid input. Defaulting to 'easy' mode.")
        return EASY_ATTEMPTS

def check_answer(guess, number):
    """Check guess against the actual number and give feedback"""
    if guess > number:
        print("Too high. Guess again.")
        return False
    elif guess < number:
        print("Too low. Guess again.")
        return False
    else:
        print(f"You got it! The number was {number}.")
        return True

def play_game():
    """This function starts the game"""
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    actual_number = random.randint(1, 100)
    #print(f"Pssst, the correct answer is {actual_number}")
    attempts_left = choose_difficulty()
    guess_correct = False
    while attempts_left > 0 and not guess_correct:
        print(f"\nYou have {attempts_left} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        guess_correct = check_answer(guess, actual_number)
        if not guess_correct:
            attempts_left -= 1
    if not guess_correct:
        print(f"You've run out of guesses. The number was {actual_number}. Better luck next time!")

play_game()