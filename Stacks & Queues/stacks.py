from list_stack import*

def process_file(filename):
    main_stack = liststack()
    with open(filename) as file:
        for line in file:
            line_stack = liststack()  
            for char in line:
                if char != '\n':
                    line_stack.push(char)
            main_stack.push(line_stack)
    return main_stack

def process_stack(main_stack):
    while not main_stack.is_empty():
        line_stack = main_stack.pop()
        while not line_stack.is_empty():
            print(line_stack.pop(), end='')
        print()

def main():
  stack = process_file('walrus.txt')
  process_stack(stack)

if __name__ == "__main__":
  main()