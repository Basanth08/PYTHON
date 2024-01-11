import csv
def division():
    attempts = 3
    while True:
        try:
            numerator = input("Enter a numerator: ")
            denominator = input("Enter a denominator: ")
            if numerator == "" or denominator == "":
                break
            try:
                quotient = float(int(numerator) / int(denominator))
                print("Quotient of ", numerator, "/", denominator, "=", quotient)
            except ZeroDivisionError as zde:
                attempts -= 1
                if attempts > 0:
                    print("Cannot divide by zero.", attempts, "attempts remaining.")
                else:
                    raise zde
        except ValueError as ve:
            attempts -= 1
            if attempts > 0:
                print("Not a float.", attempts, "attempts remaining.")
            else:
                raise ve

def password():
    password = input("Enter a password: ")
    if len(password) < 10 or len(password) > 20:
        raise ValueError("Invalid password")
    confirm = input("Confirm your password: ")
    if password != confirm:
        raise ValueError("Passwords do not match!")       

def exponent(base,power):
    result = 1
    for i in range(power):
        result = result * base
    return result

def exponent_2(base,power):
    result = 1
    if power < 0:
        raise ValueError
    
    for i in range(power):
        result = result + base
    return result

def opener(filename):
    try:
        with open(filename) as file:
            return True
    except:
        print("File cannot be opened:",filename)
        return False


def names_and_addresses_01(filename):
    with open(filename) as csv_file:
        next(csv_file)
        for row in csv_file:
            fields = row.split(",")
            print("name: ", fields[0], "address:", fields[1])

def first_only(filename):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            print(row[0])

def main():
    division()
    password()
if __name__ == "__main__":
    main()