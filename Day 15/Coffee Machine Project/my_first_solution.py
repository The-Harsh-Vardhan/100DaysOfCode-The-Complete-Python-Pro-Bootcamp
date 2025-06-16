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

#TODO : Get User Input
def get_order():
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        print("Coffee Machine is Shutting Down!")
        return "off"
    if user_input == "report":
        return "report"
    if user_input == "espresso":
        return "espresso"
    elif user_input == "latte":
        return "latte"
    elif user_input == "cappuccino":
        return "cappuccino"
    return None

def get_coins():
    print("Please insert coins: ")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    total_money_inserted = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total_money_inserted

def print_report(resources_list, money_left):
    print(f"Water: {resources_list['water']}ml")
    print(f"Coffee: {resources_list["coffee"]}ml")
    print(f"Milk: {resources_list["milk"]}g")
    print(f"Money: {money_left}")

def check_resources(ingredients_available, ingredients_needed, order_placed):
    if ingredients_needed["coffee"] <= ingredients_available["coffee"]:
        if ingredients_needed["water"] <= ingredients_available["water"]:
            if order_placed != "espresso":
                if ingredients_needed["milk"] <= ingredients_available["milk"]:
                    return True
                else:
                    return "milk"
            else:
                return True
        else:
            return "water"
    else:
        return "coffee"

def is_money_enough(inserted_money, money_needed):
    if inserted_money >= money_needed:
        return inserted_money - money_needed
    else:
        return -1

def transaction_possible(value_of_coins_inserted, resources_available, order_details):
    change_left = is_money_enough(value_of_coins_inserted, COST_OF_ESPRESSO)
    are_resources_enough = check_resources(resources_available, MENU[order_details]["ingredients"], order_details)

    if change_left >=0 and are_resources_enough == True:
        return True
    else:
        if change_left < 0:
            print("Not enough money! Money Refunded!")
        else:
            print(f"Sorry there is not enough {are_resources_enough}! Money Refunded")
        return False

def make_coffee(ingredients_available, order_placed):
    milk_left = ingredients_available["milk"]
    if order_placed != "espresso":
        milk_left = int(ingredients_available["milk"] - MENU[order_placed]["ingredients"]["milk"])
    water_left = int(ingredients_available["water"] - MENU[order_placed]["ingredients"]["water"])
    coffee_left = int(ingredients_available["coffee"] - MENU[order_placed]["ingredients"]["coffee"])
    ingredients_available["milk"] = milk_left
    ingredients_available["water"] = water_left
    ingredients_available["coffee"] = coffee_left
    return ingredients_available

def deduct_money(money_available, inserted_money, order_placed):
    cost_of_coffee = MENU[order_placed]["cost"]
    change_left = round(inserted_money - cost_of_coffee, 2)
    if change_left > 0:
        print(f"Here is your change: ${change_left}")
    return money_available + cost_of_coffee

money = 0
continue_operating = True
while continue_operating:
    order = get_order()
    if order == "off":
        continue_operating = False
        break
    elif order == "report":
        print_report(resources, money)
        continue
    money_inserted = get_coins()
    transaction = transaction_possible( money_inserted, resources, order)
    if transaction:
        profit = deduct_money(money, money_inserted, order)
        resources_left = make_coffee(resources, order)
        resources = resources_left
        money += profit
        print(f"Here is your {order} ☕️.Enjoy! ")
