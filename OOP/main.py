from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


def coffee_machine():
    off = False
    while not off:
        choice = input(f'Would you like a ({menu.get_items()}) : ')
        if choice == 'off':
            off = True
        elif choice == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

coffee_machine()