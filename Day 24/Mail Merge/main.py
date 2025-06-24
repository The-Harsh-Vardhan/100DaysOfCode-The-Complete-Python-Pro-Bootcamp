#TODO: Create a letter using starting_letter.txt

PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    #Now we have all the lines of our letter in my_letter

#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    #Now we have a list of all the names where each name is a list item

#Replace the [name] placeholder with the actual name.
for name in names:
    stripped_name = name.strip()
    new_letter = letter.replace(PLACEHOLDER, stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as output:
        output.write(new_letter)

#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp