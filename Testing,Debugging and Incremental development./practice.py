def convert_height():
    height = int(input('Enter the height in inches:'))
    in_feet = int(height / 12)
    in_inches = int(height % 12)
    print("You are ", in_feet, in_inches, "\" tall") 

def before(n_const):
    n_const = ord(n_const)
    num3 = chr(n_const -1)
    num2 = chr(n_const -1)
    num1 = chr(n_const -1)
    print(n_const)
    print(num3)
    print(num2)
    print(num1)

def main():
    convert_height()
    n_const = input("Enter the letter:")
    before(n_const)    

main()

          

          







