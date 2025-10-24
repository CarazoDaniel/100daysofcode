cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
from art import logo
import random

def draw_card(hand):
    '''add a random card to hand'''
    next_card = random.randint(0, len(cards)-1)
    hand.append(cards[next_card])
    return hand
def calculate_hand(hand):
    '''calculate the sum of cards'''
    sum = 0
    for card in hand:
        sum += card
        if sum > 21 and card == 11:
            sum -= 10
    return sum

def blackjack():
    print(logo)
    dealer_hand = []
    player_hand = []
    dealer_hand = draw_card(dealer_hand)
    dealer_hand = draw_card(dealer_hand)
    player_hand = draw_card(player_hand)
    player_hand = draw_card(player_hand)
    print(f'Your hand is: {player_hand}')
    print(f'The dealer has a: {dealer_hand[0]}')
    if input("Do you want to play a hand of Blackjack? 'y' or 'n'").lower() == 'y':
        go = True
        print(f"You have {player_hand} a: {calculate_hand(player_hand)}")
        while go:
            game = input("Do you want a new card? 'y' or 'n'").lower()
            if game == 'y':
                player_hand = draw_card(player_hand)
                print(f"You have {player_hand} a: {calculate_hand(player_hand)}")
                if calculate_hand(player_hand) > 21:
                    print(f'You loose, the goal is to have 21 not over. the house has {calculate_hand(dealer_hand)}')
                    go = False
            if game == 'n':
                while calculate_hand(dealer_hand) < 16:
                    dealer_hand = draw_card(dealer_hand)
                    print(f'The dealer draws: {dealer_hand}')

                if calculate_hand(dealer_hand) >= 17 and calculate_hand(dealer_hand) <= 21:
                    if calculate_hand(dealer_hand) >= calculate_hand(player_hand):
                        print(f'You lost, the dealer has a better hand, you have {player_hand} and the dealer has {dealer_hand}')
                        go = False
                    if calculate_hand(dealer_hand) < calculate_hand(player_hand):
                        print(f'You Win, you have a better hand, you have {player_hand} and the dealer has {dealer_hand}')
                        go = False
                else:
                    print(f'You Win, it seems the dealer went over, you have {player_hand} and the dealer has {dealer_hand}')
                    go = False
        if input("Do you want to play again? 'y' or 'n'").lower() == 'y':
            print('\n' *20)
            blackjack()

blackjack()
