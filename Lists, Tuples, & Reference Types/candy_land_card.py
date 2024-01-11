import random
def make_deck():
    colours = ('R','P','Y','B','O','G')
    deck = []
    
    for i in range(len(colours)):
        for j in range(6):
           deck = deck + [(1,colours[i],  'S' + colours[i])]
    for i in range(len(colours)):
        for j in range(4):
           deck = deck + [(2,colours[i],  'D' + colours[i])]

    special_1 = (9,20,42,69,92,102,117)
    special_2 = ('CC','IC','JJ','GP','LP','PS','BB')

    for i in range(7):
        deck = deck + [(special_1[i],'X',special_2[i])]

    return deck

def shuffle(deck):
    random.seed(47)
    length = len(deck)
    for i in range(0, length-1):
        j = random.randint(i, length-1)
        temp = deck[i]
        deck[i] = deck[j]
        deck [j] = temp
    return deck

def draw(deck):
    if len(deck) == 0:
        return None
    return deck.pop()


def main():
    deck = make_deck()
    print("The length of deck can be:", len(deck))
    print("")
    print("The Deck is:", deck)
    print("")
    shuffled_deck = shuffle(deck)
    print("Heres the Shuffled deck:", shuffled_deck)
    print("")
    print("Drawing the cards:")
    for i in range(68):
        print(draw(shuffled_deck))
    print("")
    print("Length of the deck is :", len(shuffled_deck))

if __name__ == "__main__":
    main()
