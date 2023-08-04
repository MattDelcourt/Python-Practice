'''
This program simulates a simplified version of 
blackjack between two virtual players:
 The cards have the following values:
     Numeric cards are assigned the value they printed on them. (2 of spades has a 
        value of 2, the 5 of hearts has a value of 5 etc.,)
     Jacks, Queens and Kings have a value of 10
     Aces are valued at 1 or 11 depending on the player’s choice.
The program then deals cards to each player until one player’s hand is worth more 
than 21 points. When that happens, the other player is the winner. (It is possible that 
both players exceed 21 , in which case neither player wins)
The program then repeats until all the cards have been dealt from the deck.
If a player is dealt an ace, the program should decide the value of the card according to 
the following rule:
     the ace will be assigned a value of 11
     unless that makes the player’s hand exceed 21 points in that case the ace is assigned a value of 1.

'''

import random

def main():
    # Create a deck of cards.
    deck = create_deck()

    # Deal the cards.
    deal_cards(deck)
'''
The create_deck function returns a dictionary
representing a deck of cards.
'''
def create_deck():
    '''
    Create a dictionary with each card and its value
    stored as key-value pairs.
    '''
    deck = {'Ace of Spades':11, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4,'5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':11, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':11, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':11, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    # Return the deck.
    return deck
'''
The deal_cards function deals a specified number of cards
from the deck.
'''
def deal_cards(deck):
    # Initialize an accumulator for the hand value.
    myValue = 0
    opntValue = 0
    hand_value = 0
    aceM = False
    aceO = False
    dealer = 0
    player = 0
    opponent = 0

    '''
    Deal the cards and accumulate their values.
    and check for Ace value
    '''
    for count in range(len(deck)):
        while myValue < 21 or opntValue < 21:
            if len(deck) != 0:
                card, value = random.choice(list(deck.items()))
                print(card)
                myValue += value
                if card == 11:
                    aceM = True
                if aceM and myValue > 21:
                    myValue -= 10
                card, value = random.choice(list(deck.items()))
                print(card)
                opntValue += value
                if card == 11:
                    aceO = True
                if aceO and opntValue > 21:
                    opntValue -= 10 
            else:
                break 
    
        if myValue > 21 and opntValue > 21:
            print("Dealer Wins")
            dealer += 1
        elif myValue > 21:
            print("opponent Wins")
            opponent += 1
        elif opntValue > 21:
            print("You Win")
            player += 1
        myValue = 0
        opntValue = 0
    
    #call game done
    print("game is over\nDealer won:",dealer,"\nOpponent Won:",opponent,"\nPlayer Won:",player)

# Call the main function.
main()
