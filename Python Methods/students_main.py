from students import *

def main():
    b = Student("8946", "BV")
    b.add_credits(30)
    b.set_gpa(3.75)
    print_student(b)
    print("GPA:", b.get_gpa())


if __name__ =="__main__":
    main()