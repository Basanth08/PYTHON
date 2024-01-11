from food_truck import *

def test_price():
    combo = Combo('test', ['s', 'b', 'rc'])
    expected_total = prices['soda'] + prices['burger'] + prices['roti channa']
    assert combo.price(prices) == expected_total

def test_code():
    expected_codes = {
         "s" :"soda", "ms":"milk shake", "t":"tea", 
         "b":"burger","cb":"cheese burger","cf":"chicken fingers",
         "f":"fries","rc":"roti channa","cs":"cole slaw"
    }
    assert codes == expected_codes 