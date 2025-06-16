MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

COST_OF_ESPRESSO = MENU["espresso"]["cost"]
COST_OF_LATTE = MENU["latte"]["cost"]
COST_OF_CAPPUCCINO = MENU["cappuccino"]["cost"]

def get_coins():
    """Return the total amount from the coins inserted by the user"""
    print("Please insert coins: ")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    total_money_inserted = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total_money_inserted

def print_report(resources_list, money_left):
    """Prints the quantity of ingredients left and the profit earned!"""
    print(f"Water: {resources_list['water']}ml")
    print(f"Coffee: {resources_list["coffee"]}ml")
    print(f"Milk: {resources_list["milk"]}g")
    print(f"Money: {money_left}")

def check_resources(ingredients_needed):
    """""This returns the ingredient if it is insufficient"""
    for key in ingredients_needed:
        if ingredients_needed[key] >= resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True

def is_money_enough(inserted_money, money_needed):
    if inserted_money >= money_needed:
        change = round(inserted_money - money_needed, 2)
        print(f"Here is ${change} in change.")
        global money
        money += money_needed
        return True
    else:
        print("Not enough money! Money Refunded!")
        return False

def make_coffee(order_placed):
    for key in order_placed:
        resources[key] -= order_placed[key]
    print(f"Here is your {order} ☕️.Enjoy! ")

money = 0
continue_operating = True
while continue_operating:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        continue_operating = False
        break
    elif order == "report":
        print_report(resources, money)
        continue
    drink = MENU[order]
    if check_resources(drink["ingredients"]):
        money_inserted = get_coins()
        if is_money_enough(money_inserted, MENU[order]["cost"]):
            make_coffee(MENU[order]["ingredients"])