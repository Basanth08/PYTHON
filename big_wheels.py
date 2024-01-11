import array_utils
import random

def create_big_wheel():
    return array_utils.range_array(5, 105, 5)

def print_big_wheel_values(big_wheel_array):
    
def spin_wheel(big_wheel_array):
    

def run_round(big_wheel_array, spin_threshold):
    count = 0
    value = spin_wheel(big_wheel_array)
    while value < 100 and value < spin_threshold and count < 2:
        value += spin_wheel(big_wheel_array)
        count += 1
    return value

def read_results_recursion(results_array, i=0):
    if i < len(results_array):
        print(results_array[i])
        read_results_recursion(results_array, i + 1)

def results_sum_recursion(results_array, i=0):
    if i < len(results_array):
        return results_array[i] + results_sum_recursion(results_array, i + 1)
    return 0

def rounds_check_recursion(results_array, i=0, count=0):
    if i < len(results_array):
        if results_array[i] <= 100:
            count += 1
        return rounds_check_recursion(results_array, i + 1, count)
    return count

def main():
    try:
        print()
        threshold = int(input("Enter the threshold to trigger a second spin: "))
        rounds = int(input("Enter the number of rounds to run the simulation (1-100): "))

        







        else:
            print("Please enter a valid number between 1 and 100 for rounds.")
    except ValueError:
        print("Please enter a valid number for the threshold and rounds.")

if __name__ == "__main__":
    main()
