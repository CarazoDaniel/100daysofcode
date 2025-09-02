# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# num_friends = len(friends) - 1
# paying_friend = random.randint(0,num_friends)
# print(f"The friend to pay is {friends[paying_friend]}")

# random.choice(friends)

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# import random
# hands = [rock,paper,scissors]
# player = int(input('What do you choose?'
#       'Type 0 for "Rock", 1 for "Paper" and 2 for "Scissors"\n'))
# print (f'You chose {player} \n {hands[player]}')
# snek = random.choice(hands)
# print (snek)
# print(f'The computer chose {snek}')
# if snek == hands[player]:
#     print("It seems to be a Draw!")
# elif snek == scissors and hands[player] == paper:
#     print("It seems you have Lost, better luck next time")
# elif snek == paper and hands[player] == rock:
#     print("It seems you have Lost, better luck next time")
# elif snek == rock and hands[player] == scissors:
#     print("It seems you have Lost, better luck next time")
# elif snek == scissors and hands[player] == rock:
#     print("You have become the Master!")
# elif snek == paper and hands[player] == scissors:
#     print("You have become the Master!")
# elif snek == rock and hands[player] == paper:
#     print("You have become the Master!")
# else:
#     print("I'm not feeling well Mr.Stark")

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")