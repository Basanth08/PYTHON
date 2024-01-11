import sorts

def test_split_odd():
    #setup
    x = [0,1,2,3,4,5,6,7,8,9,10]
    expected = ([0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10])
    #invoke
    actual = sorts.split(x)
    #analyze
    actual == expected

def test_split_even():
    #setup
    x = [1,2,3,4,5,6,7,8,9,0]
    expected = ([1, 2, 3, 4, 5], [6, 7, 8, 9, 0])
    #invoke
    actual = sorts.split(x)
    #analyze
    actual == expected

def test_partition():
    a = [ 4,7,6,9]
    expected = ([],[4],[7,6,9])
    actual = sorts.partition(a,4)
    actual == expected