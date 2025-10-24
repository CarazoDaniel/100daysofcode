from art import logo
print(logo)
import random

def compare(guess,number):
    '''compare the first to second, true or false and print a hint'''
    if guess == number:
        return True
    elif guess < number:
        print("Too low")
        return False
    else:
        print("Too High")
        return False
    
def dificulty():
    '''set live number to 10 or 5'''
    if input("Do you want to on 'hard' or 'easy'?").lower() == 'easy':
        return 10
    else:
        return 5
    
def new_number():
    '''A random int between 1 and 100'''
    return random.randint(1, 100)

print("Welcome to the guessing Game")
print("You have to guess a specific number between 1 and 100, you can choose hard for 5 attempts or easy for 10")
atempt = dificulty()
boss = new_number()

while (atempt > 0):
    guess = int(input("What is your guess? "))
    if compare(guess,boss):
        print(f'That is the correct guess, the number was {boss}')
        break 
    elif atempt == 1:
        atempt -= 1
        print("Last Chance!")
    else:
        atempt -= 1
        print(f"You have {atempt} left")