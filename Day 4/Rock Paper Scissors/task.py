rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome! Let's Play Rock, Paper and Scissors!")
p_choice = int(input("Type '0' for Rock, '1' for Paper and '2' for Scissors\n"))
print("Player Choose!")
if p_choice == 0:
    print(rock)
elif p_choice == 1:
    print(paper)
elif p_choice == 2:
    print(scissors)
else:
    print("You have choosen a wrong input!")

options = [rock,paper,scissors]

import random
c_choice = random.randint(0,2)

print("Computer Choose!")
print(options[c_choice])

if p_choice == c_choice:
    print("DRAW!!")
elif p_choice == 0:
    if c_choice == 1:
        print("PLAYER LOSES!")
    elif c_choice == 2:
        print("PLAYER WINS")
elif p_choice == 1:
    if c_choice == 2:
        print("PLAYER LOSES!")
    elif c_choice == 0:
        print("PLAYER WINS")
elif p_choice == 2:
    if c_choice == 0:
        print("PLAYER LOSES!")
    elif c_choice == 1:
        print("PLAYER WINS")