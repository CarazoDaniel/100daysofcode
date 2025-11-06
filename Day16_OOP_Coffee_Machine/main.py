from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()


value = True

while value:
    selection = input(f"Choose an item from the MENU ({menu.get_items()}): ").lower()
    if selection == 'off':
        print('Goodbye')
        value = False
    elif selection == 'report':
        coffee.report()
        money.report()
    elif selection == menu.find_drink(selection).name:
        if coffee.is_resource_sufficient(menu.find_drink(selection)) and money.make_payment(menu.find_drink(selection).cost):
            coffee.make_coffee(menu.find_drink(selection))
    else:
        print('It seems that wasn\'t an option')