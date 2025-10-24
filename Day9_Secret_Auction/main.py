# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo

print(logo)
go = 'yes'
bids = {}
best_bid = 0
winner = ''

while go == 'yes':
    name = input("Type your name: ").lower()
    bid = int(input("Type your bid (in $):\n"))
    bids[name] = bid
    go = input("Is there another bidder? ('yes' or 'no')").lower()
    if go == 'no':
        print("alrighty then")
        for key in bids:
            if bids[key] > best_bid:
                best_bid = bids[key]
                winner = key 
        print(f'The winner of the bid is: {winner} with: {bids[key]} ')
    else:
        print('\n' * 100)