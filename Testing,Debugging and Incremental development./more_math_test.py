import math
import more_math

def test_factorial():

    x = 5
    expected = 120
    actual = more_math.fact(x)
    assert actual == expected 

def test_root():

    x = 9
    expected = 3
    actual = more_math.root(x)
    assert math.isclose(expected,actual,abs_tol=0.5)

def test_trunk():

    x = 3
    expected = 3
    actual = more_math.trunk(x)

    assert math.isclose(expected,actual,abs_tol=0.5)


