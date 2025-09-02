print(r'''
*******************************************************************************



                                   /\
                              /\  //\\
                       /\    //\\///\\\        /\
                      //\\  ///\////\\\\  /\  //\\
         /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \
        / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \
       /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       *
      /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\
     / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\
    / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\
   /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\
  /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\       |
 / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |           |
/ ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo  |
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
if input('Would you like to go "left" or "right"?\n').lower() == "left":
    print("You have entered the woods, it seems like a nice place.")
    if input('You found a river, would you "wait" for a boat or "swim"?\n').lower() == "wait":
        print("The boat helps you cross safe")
        door = input('You have found 3 doors, "red" "blue" and "yellow", which one will you open?\n').lower()
        if  door == "red":
            print("Oh no, this door seems to be filled with magma, you burn to death")
        elif door == "blue":
            print("Oh no, this door has a guard minotaur on the other side, he was waiting for a meal")
        elif door == "yellow":
            print("It seems you found my treasure. Congratz!\nLets have a party!")
            print('''
⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣟⡀⠀⣸⣿⣿⣿⠋⠙⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⣿⣇⣀⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣾⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠃⠐⠺⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠛⢿⣿⣿⣿⣆⠹⣿⣿⣿⣿⣿⣿⠟⣡⣴⠀⢸⡿⠂⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣧⣤⣼⣿⡛⠛⠛⠀⠙⣿⣿⣿⣿⠏⠰⠿⢿⣧⣤⣤⣶⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⢻⣿⣿⣿⡿⠋⡁⠀⣶⣶⠀⣿⣿⣿⣯⠁⠈⣻⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⠁⣼⣿⣄⠉⣁⣴⣿⣿⣿⣷⣷⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠉⠻⣿⣇⣰⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⡿⢿⣿
⣿⣿⣿⣿⣿⠙⣷⡀⠀⠀⠀⠀⠈⠻⣿⣿⣿⠛⢿⡟⢀⣄⠙⠿⠟⠋⣁⣤⣾⣿
⣿⣿⣿⣿⣇⠀⠈⠻⣄⠀⠀⠀⠀⠀⠈⢻⣿⣷⣄⣠⣾⣿⣷⣶⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠻⣦⣄⠀⠈⠳⣄⠀⠀⠀⠀⠀⢻⣿⣿⣿⡟⠉⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣇⠀⠀⠙⠷⣦⣀⠈⠻⣦⣄⣀⠀⣸⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡟⠙⠷⣦⣀⠀⠈⠙⢻⣶⣤⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠃⣀⣀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ''')
        else:
            print("Oh no, it seems you were not able to choose and starved")
    else:
        print("Oh no, it is salmon season, rivers are not safe to swim")
else:
    print("Oh no, you tried to enter the woods but found a bear cub, and mama bear mauled you")

