import calculator
import math

def test_add():
    #setup
     x = 8
     y = 2
     expected = "8+2=10"

     #invoke

     actual = calculator.add(x,y)

     #analyze

     assert expected == actual

def test_sub():
     #setup
     x = 4
     y = 2
     expected = "4-2=2"

     #invoke 
     actual = calculator.sub(x,y)

     #analyze

     assert expected == actual

def test_mul():
     #setup
     x = 2
     y = 3
     expected = "2*3=6"

     #invoke
     actual = calculator.mul(x,y)

     #analyze
     assert expected == actual

def test_div():
     #setup
     x = 4
     y = 2
     expected = "4/2=2.0"

     #invoke
     actual = calculator.div(x,y)

     #analyze

     assert expected == actual

def test_exp():
     #setup
     x = 3
     y = 2
     expected = "3**2=9.0"

     #invoke

     actual = calculator.exp(x,y)

     #analyze

     assert expected == actual

