from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()


continue_operating = True
while continue_operating:
    order = input(f"What would you like? {my_menu.get_items()}: ")
    if order == "off":
        continue_operating = False
        break
    elif order == "report":
        my_coffee_maker.report()
        my_money_machine.report()
        continue
    else:
        my_drink = my_menu.find_drink(order) #Object of the Type Menu Item
        if my_coffee_maker.is_resource_sufficient(my_drink):
            if my_money_machine.make_payment(my_drink.cost):
                my_coffee_maker.make_coffee(my_drink)