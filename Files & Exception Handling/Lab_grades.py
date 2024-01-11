import csv
def terminate():
    prompt = input("Do you want to quit? (y/n): ")
    if prompt.lower() == 'y':
        return True
    else:
        return False

def student_lab_average(students_record):
    sum = 0
    for i in range(2,18):
        students_grade = students_record[i]
        if students_grade == '':
            students_grade = 0
        sum = sum + float(students_grade)
    average = sum / 16
    return average

def main():
    class_min = 100
    class_max = 0
    total_average = 0
    count_of_record = 0 

    while True:
        filename = input("Enter a filename or 'quit' to quit: ")
        if filename == "quit":
            print("Goodbye!")
            break

        try:
            with open(filename) as file:
                next(file)  # Skip the header line
                print("Lab Averages from:", filename)
                print("—----------------------------------------------------------")
                print("Student                                         Lab Average")
                print("—----------------------------------------------------------")

                for line in file:
                    record = line.strip().split(",")
                    students_average = student_lab_average(record)
                    count_of_record = count_of_record + 1
                    total_average = total_average + students_average
                    if students_average < class_min:
                        class_min = students_average
                    if students_average > class_max:
                        class_max = students_average

                    name_length = len(record[1]) + len(record[0])
                    print(record[1], record[0], end="")
                    print(" " * (46 - name_length), students_average)

                print("—----------------------------------------------------------")
                print("Class Average                                  ", total_average / count_of_record)
                print("Class Minimum                                  ", class_min)
                print("Class Maximum                                  ", class_max)

        except FileNotFoundError:
            print("No such file:", filename)

if __name__ == "__main__":
    main()
