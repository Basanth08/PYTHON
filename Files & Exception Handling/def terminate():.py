def terminate():
    """
    Prompts the user for confirmation to quit the program.

    Returns:
        bool: True if user confirms quitting, False otherwise.
    """
    quit = input("Are you sure (y/n): ")
    if quit == 'y' or quit == 'Y':
        return True
    return False

def student_lab_average(record):
    """
    Calculates the average of lab grades for a given student record.

    Args:
        record (list): A list representing a student record with grades.

    Returns:
        float: The average of the lab grades.
    """
    sum = 0
    for i in range(2,18):
        grade = record[i]
        if grade == '':
            grade = 0
        sum += float(grade)
    average = sum / 16
    return average

def main():
    """
    Main function to process student records and calculate statistics.
    """
    total_avg = 0
    record_count = 0
    class_min = 100
    class_max = 0
    while True:
        prompt = input("Enter a command or 'quit' to quit: ")
        if prompt == "quit":
            if terminate() == True:
                print("Goodbye!")
                break
            continue
        try:
            with open(prompt) as file:
                next(file)
                print("Lab Averages from:", prompt)
                print("—----------------------------------------------------------")
                print("Student                                         Lab Average")
                print("—----------------------------------------------------------")
                for line in file:
                    record = line.strip().split(",")
                    avg = student_lab_average(record)
                    record_count += 1
                    total_avg += avg
                    if avg < class_min:
                        class_min = avg
                    if avg > class_max:
                        class_max = avg
                    name_length = len(record[1]) + len(record[0])   # Necessary code in order to left align the grades.
                    print(record[1], record[0], end="")             # Necessary code in order to left align the grades.
                    print(" " * (46 - name_length), avg)            # Necessary code in order to left align the grades.
            
                print("—----------------------------------------------------------")
                print("Class Average                                  ", total_avg/record_count)
                print("Class Minimum                                  ", class_min)
                print("Class Maximum                                  ", class_max)    
        except:
            print("No such file:", prompt)

if __name__ == "__main__":
    main()
