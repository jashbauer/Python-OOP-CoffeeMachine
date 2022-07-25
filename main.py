from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# ASSIGNING CLASSES
# Menu
menu = Menu()
# Coffee Maker
coffer = CoffeeMaker()
# Money Machine
cashier = MoneyMachine()


def coffee_machine():
    choice = input(f"What would you like, ({menu.get_items()})? ")

    if choice == "report":
        coffer.report()
        cashier.report()
    elif choice == "off":
        print("Shutting Down...")
        return
    else:
        drink = menu.find_drink(choice)
        if drink != None:
            if coffer.is_resource_sufficient(drink):
                if cashier.make_payment(drink.cost):
                    coffer.make_coffee(drink)

    coffee_machine()


coffee_machine()
