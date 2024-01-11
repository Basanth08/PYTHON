class student:
    __slots__ = ["id", "name", "credits", "gpa"]
    def __init__(self,id,name):
    
        self.id = id
        self.name = name
        self.credits = 0.0
        self.gpa = 0.0

def print_student(student):
    print("Student1",student.id, ",",student.name, ",",student.credits,",",student.gpa)

def main():
    student1 = student("098", "Sai")
    # student2 = student()
    # student1.id = ""
    # student1.name = ""
    # student1.credits = 0.0
    # student1.gpa = 3.60
    print_student(student1)
    # print_student(student2)
if __name__ =="__main__":
    main()