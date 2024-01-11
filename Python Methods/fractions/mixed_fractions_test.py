from mixed_fractions import *

TUPLES = [(3, 1, 2), (3, -1, 1), (2, 0, 1)]
FRACTIONS = [Fraction(w, n, d) for w, n, d in TUPLES]

# def test_unique_sorted_list():
#     actual = mixed_fractions.unique_sorted_list(FRACTIONS)  
#     assert [FRACTIONS[1], FRACTIONS[0]] == actual

def test_simplify():
    fraction = Fraction(5,4,3)
    simplified_fraction = fraction.simplify()
    assert simplified_fraction.get_fraction() == (6,1,3)

# def test_add():
#     f1 = Fraction(1, 3, 4)
#     f2 = Fraction(1, 2, 5)
#     expected = Fraction(0, 17, 20).simplify()
#     actual = f1.add(f2)
#     assert expected == actual

# def test_add():
#     fraction1 = Fraction(3,2,1) #1+2/3 = 5/3
#     fraction2 = Fraction(2,3,4) #2+3/4 = 11/4
#     result = fraction1.add(fraction2)
#     assert result.get_fraction() == (6,1,4)

def test_partition():
    actual = mixed_fractions.partition(FRACTIONS)
    assert 2 == len(actual)
    assert FRACTIONS[0] in actual
    assert FRACTIONS[1] in actual
    assert FRACTIONS[2] in actual
    assert [FRACTIONS[0]] == actual[FRACTIONS[0]]
    assert [FRACTIONS[1], FRACTIONS[2]] == actual[FRACTIONS[1]]

def test_find_all():
    a_partition = mixed_fractions.partition(FRACTIONS) 
     
    actual = mixed_fractions.find_all(a_partition, FRACTIONS[0])                                 
    assert [FRACTIONS[0]] == actual
    
    actual = mixed_fractions.find_all(a_partition, mixed_fractions.Fraction(2,3,2))  
    assert [FRACTIONS[0]] == actual
    
    actual = mixed_fractions.find_all(a_partition, FRACTIONS[2])                                 
    assert [FRACTIONS[1], FRACTIONS[2]] == actual
    
    actual = mixed_fractions.find_all(a_partition, mixed_fractions.Fraction(3,-2,2))                                 
    assert [FRACTIONS[1], FRACTIONS[2]] == actual

def test_find_all_Empty():
    a_partition = mixed_fractions.partition(FRACTIONS)
    actual = mixed_fractions.find_all(a_partition, mixed_fractions.Fraction(1,2,3))                                 
    assert [] == actual
