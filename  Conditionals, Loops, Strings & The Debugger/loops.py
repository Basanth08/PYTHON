def count_down(number):
    sum = 0
    while number >= 0:
        sum = sum + number
        print(number)
        number = number - 1
    print("SUM",sum)

def count_up(number):
    current = 0
    sum = 0
    while current <= number:
        sum = sum + number
        print(current)
        current = current + 1
    print("SUM", sum)

def sum_of_odds(number):
    sum = 0 
    while True:
        number = int(input("Enter a number:"))
        if number == 0:
            break
        elif number % 2 == 0:
            continue
        sum = sum + number
    return sum

def main():
    count_down(8)
    count_up(8)
    sum_of_odds(10)

main()

