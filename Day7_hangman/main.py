import random
import hangman_words
import hangman_art


lives = 6

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []
while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    display = ""
    if guess not in guessed_letters:
        guessed_letters += guess
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)


        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that is not in the word.\nYou lose a life")
            if lives == 0:
                game_over = True

                # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
                print(f"***********************IT WAS {chosen_word} YOU LOSE**********************")

        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")

        print(hangman_art.stages[lives])
    else:
        print(f"You already guessed that\n You have guessed: {guessed_letters}")

# the placeholder can also be a list to be easily modified and not make the string every loop.
# this however needs a difference for printing     print("".join(placeholder))