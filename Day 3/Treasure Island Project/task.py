print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You are at an intersection!")
direction = input("Go Left or Right ").lower()

if direction == "left":
    print("You arrives at a Castle!")
    castle = input("Go Inside or Wait Outside").lower()
    if castle == "inside":
        print("You entered the Castle of Death!")
        print("Game Over")
    else:
        print("You were eaten by a Bear!")
        print("Game Over")
else:
    print("You arrives at a River!")
    print("You see an eccentric man wearing a robe!")
    man = input("Ask for 'help' to cross the river or 'cross' the River yourself").lower()
    if man == "help":
        print("Hello Gentleman! Can you please help me Cross the River?")
        print("Yeah! Sure, Let's go")
        print("You have crossed the River!")
        print("You arrived at a Mansion")
        mansion = input("Go 'inside' or wait 'outside' ").lower()
        if mansion == 'inside':
            print("You see three doors!")
            door = input("Choose one! 'red' or 'green' or 'blue' ").lower()
            if door == "red":
                print("You win!")
                print("You Found the Treasure")
            elif door == 'green':
                print("You enter a room full of beasts!")
                print("GAME OVER!!")
            elif door == 'blue':
                print("You enter a room full of fire!")
                print("GAME OVER!!")
        else:
            print("You died because of Night Demons!")
            print("GAME OVER!!")
    elif man == "cross":
        print("You died because of Crocodiles in the River!")
        print("Game Over!")