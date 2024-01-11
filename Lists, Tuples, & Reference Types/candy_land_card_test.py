import candy_land_card

def test_for_single_colour():
    a = candy_land_card.make_deck()
    b = (1,'G','SG')
    c = a[32]
    assert b == c
    

