import group_characters

def test_is_upper_1():
    #setup
    character = 'H'
    expected = True
    
    #invoke
    actual = group_characters.is_upper(character)
    
    #analyze
    assert actual == expected

def test_is_lower_1():
    #setup
    character = 'h'
    expected = True


    #invoke
    actual = group_characters.is_lower(character)

    #analyze
    assert actual == expected

def test_is_digit_1():
    #setup
    character = '4'
    expected = True
    #invoke
    actual = group_characters.is_digit(character)
    #analyze
    assert actual == expected

def test_group_characters_true():
    #setup
    string = '3633sdfhgrt453'
    expected = '3633453sdfhgrt'
    
    #invoke
    actual = group_characters.group_characters(string)
    
    #analyze
    assert actual == expected

