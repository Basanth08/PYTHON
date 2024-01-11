import cards
import random
def test_make_card():
    card = cards.make_card(5, "Hearts")
    assert card == (5, "Hearts", "5 of Hearts", " 5H")

def test_of_diamonds():
    card = cards.make_card(6,"Diamonds")
    assert card == (6, "Diamonds", "6 of Diamonds" , " 6D")

def test_make_deck():
    card = cards.make_card(2,"Clubs")
    deck = cards.make_deck()
    dec_value=deck[0]
    assert card == dec_value

def test_draw():
    deck = cards.make_deck()
    hand = []
    card = (14, 'Spades', 'Ace of Spades', 'AS')
    drawing = cards.draw(deck,hand)
    assert card  == drawing
    assert len(deck) == 51
    assert len(hand) == 1

def equit(a,b):
    set_a=set(a)
    set_b=set(b)
    return set_a == set_b

print(equit([1,2,3],[4,3,2,1]))