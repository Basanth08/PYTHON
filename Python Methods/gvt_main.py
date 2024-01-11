import gvt

def main():
    a = gvt.Card('goat', 45, 'legendary', 'goat', 15, 10)
    b = gvt.Card('not goat', 15, 'normal', 'troll', 25, 30)
    c = gvt.Card('similar goat', 45, 'legendary', 'goat', 15, 10)
    d = gvt.Card('what goat', 30, 'fancy', 'goat', 75, 5)
    
    print(a)
    
    a.damage(b.get_attack())
    print(a.get_hp())
    b.damage(a.get_attack())
    print(b.get_hp())
    print(a == c)
    print(a == b)
    
    hand = [a, b, c, d]
    hand.sort()
    
    for card in hand:
        print(card)
    
main()
