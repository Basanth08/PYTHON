import practice

def test_diff_1():

    #setup
    a = 6
    b = 5
    expected = 1

    #invoke

    actual = practice.absolute_difference(a,b)
  

    #analyze 

    assert expected == actual

def test_diff_2():

    #setup
    a = 7
    b = 4
    expected = 3

    #invoke

    actual = practice.absolute_difference(a,b)
  

    #analyze 

    assert expected == actual

def test_diff_3():

    #setup
    a = 8
    b = 9
    expected = 1

    #invoke

    actual = practice.absolute_difference(a,b)
  

    #analyze 

    assert expected == actual
