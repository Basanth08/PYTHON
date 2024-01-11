import arrays, array_utils
import random
import time
import searches
'''
def making_arrays():
    print(arrays.Array(5))
    print(arrays.Array(1, 0))
    print(arrays.Array(10, ""))
    print(arrays.Array(20, False))

def while_fill(an_array):
    length = len(an_array)
    counter = 0
    while counter < length:
        an_array[counter] = counter
        counter += 1
    return an_array

def for_fill(an_array):
    length = len(an_array)
    for i in range(length):
        an_array[i] = i
    return an_array
'''
def roll_the_die(sides):
    return random.randint(1,sides)
'''
def linear_search_timer(an_array, target):
    begin = time.perf_counter()
    print(searches.linear_search(an_array, target))
    end = time.perf_counter()
    elapsed = end - begin
    print("elapsed time: " + str(elapsed))

def linear_timer():
    arr = arrays.Array(10000001)
    for i in range(len(arr)):
        arr[i] = i
    linear_search_timer(arr, 1)
    linear_search_timer(arr, 5000000)
    linear_search_timer(arr, 10000000)


def print_odds(an_array):
    for i in range(len(an_array)):
        if an_array[i] % 2 != 0:
            print(an_array[i], end = " ")

def print_odds_rec(an_array, index = 0):
    if index >= len(an_array):
        print()
    else:
        if an_array[index] % 2 == 1:
            print(an_array[index], end = " ")
        print_odds_rec(an_array, index+1)

def countdown(n):
    if n < 0:       # base case 1 (input validation) T(N), N<0 = Undefined
        raise ValueError("Undefined")
    elif n == 0:    # base case 2 T(0) = 0
        print(n)
        return 0
    else:
        print(n, end = " ")
        return n + countdown(n-1) # recrusive case T(N) = N + T(N-1)

def factorial(N):
    if N < 0:
        raise ValueError("Undefined")
    elif N == 0 or N == 1:
        print(N)
        return 1
    else:
        return N * factorial(N-1)
    
def count_up(num):
    if num == 0:
        print(num)
    else:
        count_up(num - 1)
        print(num)  

def binary_search(an_array, target, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(an_array)-1
    if start > end:
        return None
    
    midpoint = (start + end) // 2
    if an_array[midpoint] == target:
        return midpoint
    elif an_array[midpoint] < target:
        start = midpoint + 1
        return binary_search(an_array, target, start, end)
    else:
        end = midpoint - 1
        return binary_search(an_array, target, start, end)

def binary_search_timer(an_array,target):
    start = time.perf_counter()
    searches.binary_search(an_array,target)
    stop = time.perf_counter
    return stop - start
'''

def main():
    '''
    print("")
    print("Making Arrays:")
    making_arrays()
    
    array = arrays.Array(15)
    array_while = arrays.Array(10)
    array_for = arrays.Array(10)
    print("")
    print("While Loop:")
    print("Before:", array_while)
    print("After:",while_fill(array_while))
    print("")
    print("For Loop:")
    print("Before:",array_for)
    print("After:", for_fill(array_for))
    print("")
    '''
    print("Dice:")
    i = 0
    random.seed(1)
    while i < 10:
        print(roll_the_die(6))
        i += 1
    '''
    for i in range(len(array)):
        array[i] = i
    print("")
    print("Linear_search_timer:")
    linear_search_timer(array, 10)
    print("")
    print("Linear_timer: ")
    linear_timer()
    new_array = arrays.Array(41)
    filled_array = for_fill(new_array)
    print_odds(filled_array)
    print_odds_rec(filled_array)
    print(countdown(100000))
    print(factorial(200))
    count_up(10)
    an_array= array_utils.range_array(0,100001)
    print(binary_search(an_array, 30))
'''

if __name__ == "__main__":
    main()