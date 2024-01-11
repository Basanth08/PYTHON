credits = 0
GPA = 0
ID = 0
def make_student(id,name):
    return [id, name, credits, GPA]

def add_student(population,id,name):
    for index in range(len(population)):
        student = population[index]
        if student[ID] == id:
            population.pop(index)
            break
    new_student = make_student(id,name)
    population += [new_student]
def get_student(population,id):
    for student in population:
        if student[ID] == id:
            return student
    return None
def add_credits(population,id):
    student = get_student(population,id)
    if student is not None:
        return student[credits]
    else:
        return None
def main():
    # student1 = make_student(1, "John")
    # student2 = make_student(2, "Jane")
    # student3 = make_student(3, "Jack")
    # student4 = make_student(4, "Jill")
    # print(student1)
    # print(student2)
    # print(student3)
    # print(student4)
    
if __name__ =="__main__":
    main()
