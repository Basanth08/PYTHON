import activities
import random
PI = 3.14

def test_squared_8():

    #setup
    x = 8
    expected = 64

    actual = activities.squared(x)

def test_cubed_2():

    #setup
    x = 2
    expected = 8
    actual = activities.cubed(x)

def coin_toss_heads():

    #setup
    random.seed(1)
    expected = "heads"
    actual = activities.coin_toss_heads()

def coin_toss_tails():
    #setup
    random.seed(2)
    expected = "tails"
    actual= activities.coin_toss_tails()

    #analyze
    assert actual == expected 
    
test_squared_8()
test_cubed_2()
coin_toss_heads()
coin_toss_tails()







