import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

continue_playing = True
while continue_playing:
    game = input("Do you want to play a game of BlackJack? 'y' for yes and 'n' for no: ")
    if game == 'no':
        continue_playing = False
    else:
        print("\n" * 20)
        print(art.logo)
        your_cards = []
        dealer_cards = []
        p_score = 0
        c_score = 0
        for i in range(0, 2):
            p_card = random.choice(cards)
            your_cards.append(p_card)
            p_score += p_card

            c_card = random.choice(cards)
            dealer_cards.append(c_card)
            c_score += c_card
        if c_score == 21:
            print("You Win")
        if p_score == 21 and c_score != 21:
            print("You Win!")

        print(f"Your cards: {your_cards}")
        print(f"current score: {p_score}")
        print(f"Computer's first card: {dealer_cards[0]}\n")

        draw_card = True
        while draw_card:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                p_card = random.choice(cards)
                your_cards.append(p_card)
                p_score += p_card
                if p_score > 21:
                    for item in your_cards:
                        if item == 11:
                            your_cards[item] = 1
                            p_score -= 10
                if p_score > 21:
                    draw_card == False
                    break
                print(f"Your cards: {your_cards}")
                print(f"current score: {p_score}\n")
                print(f"Computer's first card: {dealer_cards[0]}\n")

            elif another_card == 'n':
                draw_card = False
                while c_score < 16:
                    c_card = random.choice(cards)
                    dealer_cards.append(c_card)
                    c_score += c_card
                print(f"Your Final Hand: {your_cards}, ")
                print(f"Final Score: {p_score}\n")
                print(f"Computer's Final Hand: {dealer_cards} ")
                print(f"Final Score: {c_score}\n")
                if p_score >= 21:
                    print("You Lose!!")
                elif 21 - p_score < 21 - c_score:
                    print("You Lose!!")
                else:
                    print("You Win!!")