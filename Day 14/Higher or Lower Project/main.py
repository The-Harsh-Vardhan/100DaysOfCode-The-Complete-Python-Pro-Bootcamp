import random
import art
import game_data

#Print the logo
print(art.logo)
score = 0
def compare(person_a):
    print(f"Compare A:  {person_a["name"]}, a {person_a["description"]} from {person_a["country"]}")

    #Print the VS Logo
    print(art.vs)

    #Randomly pick another person B from the list data and make sure that it is not the
    # same as person A, then print the details
    person_b = random.choice(game_data.data)
    while person_b == person_a:
        person_b = random.choice(game_data.data)
    print(f"Against B: {person_b["name"]}, a {person_b["description"]} from {person_b["country"]}")
    guess_the_person(person_a, person_b)

def guess_the_person(person_A, person_B):
    #Ask the user to pick either A or B
    guess = input("Who has more followers: Type 'A' or 'B': ").lower()
    if person_A["follower_count"] > person_B["follower_count"]:
        more_followers = "a"
        person = person_A
    else:
        more_followers = "b"
        person = person_B

    global score
    if guess == more_followers:
        print("\n" * 20)
        print(art.logo)
        score += 1
        print(f"You're right! Current score {score}")
        compare(person)
    else:
        #End Screen
        print("\n" * 20)
        print(art.logo)
        print(f"Sorry that's wrong! Your final score is {score}")

#Randomly pick a person A from the list data and Print the data of the first person
Person_a = random.choice(game_data.data)
compare(Person_a)