import csv
import random

class Task:
    __slots__ = ["__name", "__location"]
    
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        
    def name(self):
        return self.__name
 
    def location(self):
        return self.__location
    
    def __str__(self):
        return self.__name + " in " + self.__location

def load_tasks(filename):
    tasks = []
    with open(filename) as f:
        for line in f:
            name, location = line.strip().split(',')
            task = Task(name, location) 
            tasks.append(task)
    return tasks

class Crewmate:
    __slots__ = ["__color", "__tasks", "__murdered"]
    
    def __init__(self, color): 
        self.__color = color
        self.__tasks = []
        self.__murdered = False
        
    def color(self):
        return self.__color
    
    def tasks(self):
        return self.__tasks
    
    def assign_tasks(self, num_tasks, available_tasks):
        self.__tasks = random.sample(available_tasks, num_tasks)
        
    def murdered(self):
        return self.__murdered
    
    def set_murdered(self, murdered):
        self.__murdered = murdered
        
    def __str__(self):
        if self.__murdered:
            return self.__color + " Crewmate (deceased)"
        else:
            return self.__color + " Crewmate"

    def __repr__(self):
        return "Crewmate:\n  color=" + str(self.__color) + "\n  murdered=" + str(self.__murdered) + "\n  tasks: " + str(self.__tasks)

class Ship:
    __slots__ = ('__tasks','__crew', '__imposters', '__cafeteria')

    def __init__(self, tasks):
        self.__tasks = tasks
        self.__crew = []
        self.__imposters = []
        self.__cafeteria = []

    def tasks(self):
        return self.__tasks
    
    def get_locations(self):
        locations = set(task.location() for task in self.__tasks)
        return list(locations)
    
    def run_journey(self, imposters_count):
        if not 1 <= imposters_count <= 4:
            raise ValueError("Imposters must be between 1 and 4")

    def create_crewmates(self, imposter_count):
        crew_colors = ["Black", "Blue", "Brown", "Cyan", "Green", "Pink", "Purple", "Red", "White", "Yellow"]
        random.shuffle(crew_colors)
        
        for i in range(10 - imposter_count):
            if not crew_colors:
                raise ValueError("Not enough unique colors for crewmates.")
            color = crew_colors.pop()
            crewmate = Crewmate(color)
            num_tasks = random.randint(3, 6)
            crewmate.assign_tasks(num_tasks, self.__tasks)
            self.__crew.append(crewmate) 

        for i in range(imposter_count):
            self.__imposters.append("Imposter")

def main():
    tasks = load_tasks('tasks_01.csv')
    while True:
        imposter_count_input = input("Enter the number of imposters (or press Enter to quit): ")
        if not imposter_count_input:
            print("Exiting the program. Goodbye!")
            break
        try:
            imposter_count = int(imposter_count_input)
            if not 1 <= imposter_count <= 4:
                raise ValueError("Invalid number of imposters. Must be between 1 and 4.")
            ship = Ship(tasks)
            ship.run_journey(imposter_count)
            ship.create_crewmates(imposter_count)    
        except ValueError as e:
            print("Error: " + str(e) + ". Please enter a valid number of imposters.")

if __name__ == "__main__":
    main()
