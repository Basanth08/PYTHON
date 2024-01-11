import plotter
''''
def print_lines(filename):
    my_file = open(filename)
    for line in my_file:
        stripped_line = line.strip()
        print(stripped_line)
    my_file.close()

def word_search(filename):
    string = input("Enter a word! ")
    my_file = open(filename)
    for line in my_file:
        if string.lower() == line.strip().lower():
            print("Found the word: ", string)
            return
    print("Didn't find the word.")
    my_file.close()

def longest_word(string):
    words = string.split()
    largest = ""
    for i in words:
        if len(i) > len(largest):
            largest = i
    return "Longest word: " + largest

def longest_words(filename):
    my_file = open(filename)
    for line in my_file:
        if line.strip():
            the_longest_word = longest_words(line) 
            print(the_longest_word)
    my_file.close()

def print_names(filename):
    file = open(filename)
    next(file)
    for line in file:
        split_line = line.split(",")
        print(split_line[1], split_line[0])
'''
def plot_grades(filename, column):
    with open(filename) as file:
        header = next(file).split(",")
        name = header[column]
        
        plotter.init("Grades for ", name, "Students", "Scores")
        for row in file:
            fields = row.split(",")
            score = float(fields[column])
            plotter.add_data_point(score)
        
        plotter.plot()

def main():

    #print_lines('data/alice.txt')

    #word_search('data/words.txt')

    #print(longest_word("Hello everybody my name is basanth and im fro hyderabad."))

    #longest_words('data/alice.txt')

   # print_names('data/grades_010.csv')
    plot_grades('data/grades_010.csv', 10)


if __name__ == "__main__":
    main()

