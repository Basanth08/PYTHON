import csv

def opener(filename):
    try:
        with open(filename) as file:
            return True
    except:
        print("File cannot be opened:", filename)
        return False

def names_and_addresses(filename):
    with open(filename) as file:
        file_reader = csv.reader(file)
        next(file_reader)
        for line in file_reader:
            print("name:", line[0], "address:", line[1])

def first_only(filename):
    with open(filename) as file:
        file_reader = csv.reader(file)
        next(file_reader)
        for line in file_reader:
            print(line[0])
            
def average(filename, column):
    total = 0
    count = 0
    with open(filename) as file:
        file_reader = csv.reader(file)
        next(file_reader)
        for line in file_reader:
            grade =  line[column]
            if grade == "":
                grade = 0
            total = total + float(grade)
            count =  count + 1
    average = total / count
    return round(average, 2)

def main():
    # file = input("Enter a file name.")
    # opener(file)
    first_only('data/full_grades_010.csv')
    names_and_addresses('data/full_grades_010.csv')
    print(average('data/full+grades_010.csv', 3))
if __name__ == "__main__":
    main()