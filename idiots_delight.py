import cards
import random

def deal_hand(deck):
    hand = []
    cards.shuffle(deck)
    for i in range(4):
        hand.append(deck.pop())
    return hand,deck

def discard(hand,number):
    if number == 4:
        hand = hand[4:]
    elif number == 2:
        hand = hand[:2] + hand[4:]
    return hand

def play_round(deck,hand):
    while len(hand) < 4 and deck:
        hand.append(deck.pop())
    if len(hand) >= 4:
        for i in range(len(hand) - 3):
            if hand[i][1] == hand[i+3][1]:
                hand = discard(hand, 4)
                break 
            elif hand[i+1][0] == hand[i+2][0]:
                hand = discard(hand, 2)
                break
        if deck:
            hand.append(deck.pop())
        print("Hand;",hand)
        return deck, hand
    
def main():
    deck = cards.make_deck()
    hand,deck = deal_hand(deck)
    print("Hands:",hand)
    while deck:
        deck, hand = play_round(deck, hand)
    print("Game over! You have", len(hand), "cards left.")
    if len(hand) == 0:
        print("You won!")
    else:
        print("Try again!")       

if __name__ == "__main__":
    main()

