import total_cost

def test_total_cost_1():

    #setup
    quantity = 4
    expected = 200

    #invoke
    actual = total_cost.calculate_total_cost(quantity)
    
    
    #analyze 
    assert actual == expected

def test_total_cost_2():
    #setup
    quantity = 18
    expected = 810
    
    #invoke
    actual = total_cost.calculate_total_cost(quantity)
    
    #analyze 
    assert actual == expected

def test_total_cost_3():
    #setup
    quantity = 72
    expected = 2304
    
    #invoke
    actual = total_cost.calculate_total_cost(quantity)
    
    #analyze 
    assert actual == expected