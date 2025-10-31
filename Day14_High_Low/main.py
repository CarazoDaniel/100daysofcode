from art import logo
from art import vs
from data import data
import random
MAX_LIST = len(data)-1


def compare(first,second):
    '''This will compare 2 entries selected from data'''
    if int(data[first]['follower_count']) > int(data[second]['follower_count']):
        print('You got it!')
        return True
    else:
        print(f'You\'re wrong, {data[second]['name']} has the higher follower count!')
        return False

def next_one(last):
    '''A random int between 0 and length, recieves last one'''
    num = random.randint(0, MAX_LIST)
    if num == last:
        return num - 1
    else:
        return num
    
def show_info(entry):
    '''print the info of a data entry'''
    print(f"{data[entry]['name']} a {data[entry]['description']} from {data[entry]['country']}")

def choose(first,second):
    '''Here the user chooses between A or B, func returns compare ordered.'''
    value = True
    while value:
        selection = input("Choose between A or B:").lower()
        if selection == 'a':
            return compare(first,second)
        elif selection == 'b':
            return compare(second,first)



def game():
    '''play'''
    play = True
    first = random.randint(0, MAX_LIST)
    second = next_one(first)
    count = 0 


    while play:
        print("\n"*10)
        print(logo)
        if count > 0:
            print(f'Current score: {count}!')
        print("Compare A: ")
        show_info(first)
        print(vs)
        print("Compare B: ")
        show_info(second)
        if choose(first,second):
            first = second
            second = next_one(first)
            count += 1
        else:
            play = False
            print(f'You Scored: {count}')            
        
        

            


game()




