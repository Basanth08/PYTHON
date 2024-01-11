import idiots_delight
import cards 

def test_deal_hand():
    deck = cards.make_deck()
    hand, new_deck = idiots_delight.deal_hand(deck)
    assert len(hand) == 4

def test_deal_hand_1():
    deck = cards.make_deck()
    hand, new_deck = idiots_delight.deal_hand(deck)
    assert len(new_deck) == 48
        
def test_discard():
    deck = cards.make_deck()
    hand = idiots_delight.deal_hand(deck)
    discarding = idiots_delight.discard(hand,4)
    assert discarding == ()

def test_play_round():
    deck = cards.make_deck()
    hand,new_deck= idiots_delight.deal_hand(deck)
    deck, hand = idiots_delight.play_round(deck,hand)
    assert len(hand) == 5

 