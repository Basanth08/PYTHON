from mixed_fractions import *
def test_subtract():
    a_fraction = 4/3  
    b_fraction = 1
    actual_subtract = a_fraction - b_fraction
    expected_subtract = 1/3
    assert round(expected_subtract,2) == round(actual_subtract,2)

def test_sum():
    a_fraction = Fraction(1,3,10)   # 1.3
    b_fraction = Fraction(4,6,10) # 4.6
    expected_sum = Fraction(5,9,10) # 5.9
    actual_sum = a_fraction + b_fraction 
    assert expected_sum == actual_sum
# def test_eq_1():
#     a_fraction = Fraction(-2,27,13)   #(-2 + 27/13)  
#     b_fraction = Fraction(0,7,91)
#     assert a_fraction == b_fraction 
         
# def test_eq_2():
#     x = 199933
#     y = 11111111111111111
#     z = x*y                 
#     a_fraction = z/x
#     b_fraction = y
#     assert a_fraction == b_fraction
    
# def test_neq():
#     a_fraction = Fraction(0,100000000000000000,3) #(100000000000000000/3)
#     b_fraction = Fraction(0,100000000000000001,3) #(100000000000000001/3)
#     assert a_fraction != b_fraction
    
# def test_lt():
#     a_fraction = Fraction(0,100000000000000000,3)
#     b_fraction = Fraction(0,100000000000000001,3)
#     assert a_fraction < b_fraction 

# def test_gt():
#     a_fraction = Fraction(0,100000000000000000,3)
#     b_fraction = Fraction(0,100000000000000001,3)
#     assert b_fraction > a_fraction

    