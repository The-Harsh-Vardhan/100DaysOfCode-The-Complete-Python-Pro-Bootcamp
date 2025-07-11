print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# IDEAL TRY
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have entered the wrong input! Please Try Again.")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

# MY TRY
# bill = 0
#
# if size == "S":
#     bill += 15
#     if pepperoni == "Y":
#         bill += 2
#     if extra_cheese == "Y":
#         bill += 1
# else:
#     if size == "M":
#         bill += 20
#         if pepperoni == "Y":
#             bill += 3
#         if extra_cheese == "Y":
#             bill += 1
#     else:
#         if size == "L":
#             bill += 25
#             if pepperoni == "Y":
#                 bill += 3
#             if extra_cheese == "Y":
#                 bill += 1
# print(f"Your final bill is: ${bill}.")