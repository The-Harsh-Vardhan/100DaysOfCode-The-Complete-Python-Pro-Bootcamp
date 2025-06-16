import art
import random

def deal_card():
    """Picks a Random card from the deck"""
    cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards_deck)
    return card

def calculate_score(cards):
    """Take a list of cards and return their sum"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        #Remove the 11 and add 1
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You Lose!, Opponent has a BlackJack"
    elif user_score == 0:
        return "You Win with a BlackJack"
    elif user_score > 21:
        return "You went over 21, You Lose!!"
    elif computer_score > 21:
        return "Opponent Went Over!! You Win!"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Lose"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    p_score = -1
    c_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        p_score = calculate_score(user_cards)
        c_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, Current score: {p_score}")
        print(f"Computer's first card: {computer_cards[0]}\n")

        if p_score == 0 or c_score == 0 or p_score > 21:
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                user_cards.append(deal_card())
            elif another_card == 'n':
                is_game_over = True

    while c_score != 0 and c_score < 16:
        computer_cards.append(deal_card())
        c_score = calculate_score(computer_cards)

    print(f"Your Final Hand: {user_cards}, Final Score: {p_score}\n")
    print(f"Computer's Final Hand: {computer_cards}, Final Score: {c_score}\n")
    print(compare(p_score, c_score))

while input("Do you want to play a game of BlackJack? 'y' for yes and 'n' for no: ") == 'y':
    print("\n" * 20)
    print(art.logo)
    play_game()