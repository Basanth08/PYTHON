import random
RANKS = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
SUITS = ["Clubs","Diamonds","Hearts","Spades"]
FACES = ("J","Q","K","A")

def make_card(rank,suit):

    if rank == 11:
        name = "Jack of " + suit
    elif rank == 12:
        name = "Queen of " + suit
    elif rank == 13:
        name = "king of " + suit
    elif rank == 14:
        name = "Ace of " +suit
    else:
        name = str(rank) + " of " + suit

    if rank == 11:
        shorthand = FACES[0]+suit[0]    
    elif rank == 12:
        shorthand = FACES[1]+suit[0] 
    elif rank == 13:
        shorthand = FACES[2]+suit[0] 
    elif rank == 14:
        shorthand = FACES[3]+suit[0]         
    else:
        if rank >=10:
            rank_str = str(rank)
        else :
            rank_str=' ' + str(rank)
        shorthand = rank_str + suit[0]
    if rank<10:
        shorthand = " " + str(rank)+suit[0]

    card = (rank,suit,name,shorthand)
    return card

def make_deck():
    deck = []
    RANKS = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    SUITS = ["Clubs","Diamonds","Hearts","Spades"]
    for suit in SUITS:
        for rank in RANKS:
            deck.append(make_card(rank,suit))
    return deck

def shuffle(deck):
    for i in range(len(deck)-1, 0,-1):
        j = random.randint(0,i)
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp

    return deck

def draw(deck,hand):
    if deck:
        card = deck.pop()
        hand.append(card)
        return card
    else:
        return None
    
def deal_one_hand(deck,number_of_cards):
    hand = []
    for i in range(number_of_cards):
        card = draw(deck,hand)
        if card is None:
            break
    return hand

def main():
    output=make_card(5,"Hearts")
    print(output)
    print("Hey guys lets play cards!")
    deck = make_deck()
    print("Making deck: ",deck)

    shuffling = shuffle(deck)
    print("Shuffling the deck:",shuffling)

    deal1 = deal_one_hand(deck,5)
    deal2 = deal_one_hand(deck,5)
    print("Dealing with the cards,deal1: ",deal1)
    print("Dealing with cards, deal2:",deal2)
    print("Drawing 3 cards for deal 1...") 
    for i in range(3):
            draw(deck, deal1)
    print("deal 1:", deal1)
    print("deal 2:", deal2)

if __name__ == "__main__":
    main()