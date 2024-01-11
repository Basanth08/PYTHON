global_variable = ord('A') - 1

def alphabet_position(G, global_variable):
    V = ord(G) - global_variable
    print(G, 'is in position ', V, 'in the alphabet')

def convert_to_ascii(code):
    char = ord(code)
    print(char)

def convert_from_ascii(cha):
    ch = chr(cha)
    print(ch)

def main():
    
    h = input('Enter a capital alphabet:')
    alphabet_position(h, global_variable)
    alphabet_position('G' , 123)
    alphabet_position('I' , 100)

main()
