def is_upper(character):
    value = ord(character)
    if value >= 64 and value <= 91:
        return True
    else:
        return False

def is_lower(character):
    value = ord(character)
    if value >= 97 and value <= 122:
        return True
    else:
        return False


def is_digit(character):
    value = ord(character)
    if value >= 48 and value <= 57:
        return True
    else:
        return False
   
def group_characters(string):
    index = 0
    newString = ''
    while(index<len(string)):
        if(is_digit(string[index])==True):
            newString = newString + string[index]
        index = index + 1
    index = 0
    while(index<len(string)):
        if(is_lower(string[index])==True):
            newString = newString + string[index]
        index = index + 1
    index = 0
    while(index<len(string)):
        if(is_upper(string[index])==True):
            newString = newString + string[index]
        index = index + 1
    return (newString)
        

def main():
    while True:
        string = input('Enter a string consisting of letters and digits: ')
        if string == '':
            break

        grouped_string = group_characters(string)
        print(grouped_string)


if __name__ == '__main__':
    main()