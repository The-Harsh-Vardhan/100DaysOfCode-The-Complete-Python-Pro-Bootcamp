print("Hello! Welcome to the tip calculator!")
bill = float(input("What was your bill in Rupees ₹"))
tip = int(input("What percentage should be the tip? 10 12 15 "))
people = int(input("How many people to split the bill? "))
total_amount = bill + (bill*tip)/100
final_share = total_amount / people
print(f"Each person needs to pay : {final_share}")