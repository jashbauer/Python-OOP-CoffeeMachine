from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Menu
menu = Menu()
print(menu.get_items())
menu.find_drink("latte")

# Coffee Maker
coffer = CoffeeMaker()
coffer.report()
print(coffer.is_resource_sufficient(menu.find_drink("latte")))
coffer.make_coffee(menu.find_drink("latte"))
coffer.report()

# Money Machine
cashier = MoneyMachine()
cashier.report()
cashier.process_coins()
cashier.make_payment(menu.find_drink("latte").cost)