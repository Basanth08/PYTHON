import csv
import re
import matplotlib.pyplot as plt  # Replace with your actual plotting library

def plot_grades(filename, first_name, last_name):
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            student_name = line[0]
            if first_name in student_name and last_name in student_name:
                grades = [float(grade) if grade else 0.0 for grade in line[3:]]
                plot_student_grades(first_name + " " + last_name, grades)

def plot_student_grades(student_name, grades):
    plt.figure()
    plt.bar(range(len(grades)), grades)
    plt.title(student_name + " - Grade Items")
    plt.xlabel("Grade Item")
    plt.ylabel("Score")
    plt.show()

def get_average(filename, column):
    total_grade = 0.0
    count = 0
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            grade = line[column]
            if grade:
                total_grade += float(grade)
                count += 1
    if count == 0:
        return 0.0
    return round(total_grade / count, 1)

def plot_class_average(filename):
    averages = [get_average(filename, i) for i in range(3, 30)]
    plot_class_averages("Class Averages " + filename, averages)

def plot_class_averages(title, averages):
    plt.figure()
    plt.bar(range(len(averages)), averages)
    plt.title(title)
    plt.xlabel("Grade Item")
    plt.ylabel("Average")
    plt.show()

def main():
    plot_grades("data/full_grades_100.csv", "Vikram", "Coldivar")
    plot_grades("data/full_grades_100.csv", "Blake", "Gommer")
    plot_class_average("data/full_grades_999.csv")

if __name__ == "__main__":
    main()
