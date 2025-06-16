import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    print(art.logo)
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    first_number = float(input("Enter the First Number: "))
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation = input("Enter the Operation: ")
        second_number = float(input("Enter the Second Number: "))

        result = operations[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")

        choice = input(f"Type 'y' to continue with {result}, \nType 'n' to start a new calculation: ")

        if choice == 'y':
            first_number = result
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()