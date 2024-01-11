import caesar_cipher
def test_caesar_cipher_1():

#setup

    x = "A"
    y = 3
    expected = "D"

#invoke

    actual = caesar_cipher.encrypt_letter(x,y)

#analyze

    assert actual == expected

def test_caesar_cipher_2():

    #setup 
    x = "G"
    y = 5
    expected = "L"

#invoke

    actual = caesar_cipher.encrypt_letter(x,y)

#analyze

    assert actual == expected


def test_caesar_cipher_3():

#setup

    x = "D"
    y = 10
    expected = "N"

#invoke

    actual = caesar_cipher.encrypt_letter(x,y)

#analyze

    assert actual == expected


def test_is_alphabetic_1():
    
    #setup
    x = "G"
    expected = True

    #onvoke
    actual = caesar_cipher.is_alphabetic(x)

    #analyze

    assert actual == expected

def test_is_alphabetic_1():
    
    #setup
    x = "H"
    expected = True

    #onvoke
    actual = caesar_cipher.is_alphabetic(x)

    #analyze

    assert actual == expected

def test_is_alphabetic_1():
    
    #setup
    x = "i"
    expected = False

    #onvoke
    actual = caesar_cipher.is_alphabetic(x)

    #analyze

    assert actual == expected
def test_encrypt_letter_1():
     #setup
    x = "@"
    y = None
    expected = " "

    #invoke

    actual = caesar_cipher.encrypted_letter(x,y)

    #analyze

    assert actual ==  expected

def test_encrypt_letter_2():
     #setup
    x = "4"
    y =  -6
    expected = " "

    #invoke

    actual = caesar_cipher.encrypted_letter(x,y)

    #analyze

    assert actual ==  expected

def test_decrypt_letter_1():

    #setup 
    x = "D"
    y = 3
    expected = "A"

#invoke

    actual = caesar_cipher.decrypt_letter(x,y)

#analyze

    assert actual == expected


