import activities
def test_exponent():
    # setup
    x = 3
    y = 2
    expected = 9

    #invoke
    actual = activities.exponent(3,2)

    #analyze
    assert actual == expected

def test_exponent_negative():
    #setup
    x = 2 
    y = -3
    expected = -8
    #invoke
    try:
        actual = activities.exponent(2,-3)
        assert False
    #analyze
    except ValueError:
        assert actual == expected
        

