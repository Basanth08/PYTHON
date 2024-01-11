import random

def create_ascii_range_string(start, stop):
    '''
    This is a function to create a string of ASCII characters 
    '''
    str = ""
    for i in range(start, stop):
        str = str + chr(i)
    return str
    
def create_uppercase_letters_string():
    '''
    for uppercase letters (A-Z)
    '''
    return str(create_ascii_range_string(65,91))

def create_lowercase_letters_string():
    '''
    for lowercase letters (a-z)
    '''
    return str(create_ascii_range_string(97,123))

def create_digits_string():
    '''
    This Function creates a string for the digits (0-9)
    '''
    return str(create_ascii_range_string(48,58))

def create_symbols_string():
    '''
    This Function is to create a string for symbols
    '''
    return str(create_ascii_range_string(33,48) + create_ascii_range_string(58,65) + create_ascii_range_string(91,97) + create_ascii_range_string(123,127))

def get_random_char_from_string(string):
    '''
    Function to get a random character from a given string
    '''
    random_letter = string[random.randrange(0, len(string))]
    return random_letter

def generate_random_password(num_upps, num_lows, num_digs, num_symbs):
    '''
    Function to generate a random password based on specified criteria
    '''
    password = ""

    while True:
        choice = random.randint(1,4)
        if choice == 1 and num_upps> 0: 
            letter = get_random_char_from_string(create_uppercase_letters_string())
            num_upps -= 1
            password = password + letter

        if choice == 2 and num_lows > 0: 
            letter = get_random_char_from_string(create_lowercase_letters_string())
            num_lows -= 1
            password = password + letter
            
        if choice == 3 and num_digs > 0: 
            letter = get_random_char_from_string(create_digits_string())
            num_digs -= 1
            password = password + letter

        if choice == 4 and num_symbs > 0: 
            letter = get_random_char_from_string(create_symbols_string())
            num_symbs-= 1
            password = password + letter
        
        if num_upps == 0 and num_lows == 0 and num_digs == 0 and num_symbs == 0: 
            return "Password: " + password

def main():
    while True:
        input_prompt = input("Enter <num uppers> <num lowers> <num digits> <num symbols>: ")
        value = input_prompt.split(" ")
        if input_prompt == "": 
            print("Goodbye!")
            break
        if len(value) != 4: 
            print("Please enter exactly 4 values")
            continue
        print(generate_random_password(int(value[0]),int(value[1]),int(value[2]),int(value[3])))

if __name__ == "__main__":
    main()