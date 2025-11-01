from data import MENU, resources

##check resources
##proces coins
##process transaction
def print_resources():
    for key, value in resources.items():
        print(f"{key}: {value}")

def payment(selection):
    '''Recieves drink and returns true if payment is completed'''
    try:
        quaters = int(input("How many quaters? "))
        if quaters < 0:
            raise ValueError("Please enter only positive numbers")
    except ValueError:
        print("invalid number")
        quaters = int(input("How many quaters? "))
    try:
        dimes = int(input("How many dimes? "))
        if dimes < 0:
            raise ValueError("Please enter only positive numbers")
    except ValueError:
        print("invalid number")
        dimes = int(input("How many dimes? "))    
    try:
        nickles = int(input("How many nickles? "))
        if nickles < 0:
            raise ValueError("Please enter only positive numbers")
    except ValueError:
        print("invalid number")
        nickles = int(input("How many nickles? "))    
    try:
        pennies = int(input("How many pennies? "))
        if pennies < 0:
            raise ValueError("Please enter only positive numbers")
    except ValueError:
        print("invalid number")
        pennies = int(input("How many pennies? "))
    total = quaters * 0.25 + dimes * 0.1 + nickles * 0.05+ pennies * 0.01
    if total >= MENU[selection]['cost']:
        print('payment succesful.')
        resources['money'] += MENU[selection]['cost']
        print(f'you payed {total}')
        print(f'Your change is :{total - MENU[selection]['cost']}')
        return True
    else:
        print('It seems you have not payed the proper ammount')
        print(f'you payed {total}, it is returned.')
        return False
    


def make_drink(selection):
    '''recieves the type of drink, returns true if completed.'''
    for key, value in MENU[selection]['ingredients'].items():
        if resources[key] < MENU[selection]['ingredients'][key]:
            print('Resources are limited, we cannot finish your drink')
            return False
    if payment(selection):
        for key, value in MENU[selection]['ingredients'].items():
            resources[key] -= MENU[selection]['ingredients'][key]   
        print(f'Grab your {selection} from the bottom. ')
        return True
    else:
        return False

def lunch():
    value = True
    front_menu = ''
    for key, value in MENU.items():
        front_menu += key
        front_menu += ' '

    while value:
        selection = input(f"Choose an item from the MENU ({front_menu}): ").lower()
        if selection in MENU:
            if make_drink(selection):
                print(f'here is your {selection}')
            
        elif selection == 'off':
            print('Goodbye')
            value = False
        elif selection == 'report':
            print_resources()
        else:
            print('It seems that wasn\'t an option')
        
lunch()