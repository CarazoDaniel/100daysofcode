import pandas

naot = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter:row.code  for (index,row) in naot.iterrows()}

print(nato)
def generate_word():    
    word = input("Input word to convert: ").upper()
    try:
        output = [nato[letter] for letter in word if letter in nato]
    except KeyError:
        print("Sorry, words or letters only")
        generate_word()
    else:
        print(output)

generate_word()