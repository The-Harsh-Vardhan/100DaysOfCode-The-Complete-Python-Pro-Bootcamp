from traceback import print_tb

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("nato_phonetic_alphabet.csv")

#Using Dictionary Comprehension
alpha_dict = {row.letter : row.code for (index,row) in df.iterrows() }

# Using loops
# alpha_dict = {}
# for (index, row) in df.iterrows():
#     alpha_dict[row.letter] = row.code

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_is_on = True
while input_is_on:
    user_input = input("Enter a word: ").upper()
    output = [ alpha_dict[letter] for letter in user_input ]
    print(output)




