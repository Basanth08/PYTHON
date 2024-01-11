import sorts
import time
def insertion_sort_function_timer(a_list):
    start = time.perf_counter()
    sorts.insertion_sort_wo_swap(a_list)
    end = time.perf_counter()

    elapsed_time = end - start
    return elapsed_time

def main():
    my_list = [4, 2, 7, 1, 9, 5]
    print("Original list:", my_list)

    # Measure the execution time of insertion_sort_wo_swap
    time_taken = insertion_sort_function_timer(my_list)

    print("Sorted list:", my_list)
    print("Time taken for sorting:" + str(time_taken) + "seconds")

if __name__ == "__main__":
    main()
    
    

