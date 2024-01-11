'''import arrays
def making_arrays():
    print(arrays.Array(5))
    print(arrays.Array(1, 0))
    print(arrays.Array(10, ""))
    print(arrays.Array(20, False))

making_arrays()

def while_fill(an_array):
    length = len(an_array)
    counter = 0
    while counter < len(an_array):
         an_array[counter] = counter
         counter = counter + 1
    return an_array

while_fill()

def find_max(array):
    if not array:
        return None
    max_element = array[0]
    for element in array:
        if element > max_element:
            max_element = element
    
    return max_element

array = [11,22,33,44,55]
maximum = find_max(array)
print('Maximim element:',maximum)

def find_min(array):
    if not array:
        return None
    min_element =array[0]
    for element in array:
        if element<min_element:
            min_element = element
        
        return min_element

array = [22,33,44,55,66]
minimum = find_min(array)
print('Min element:',minimum)

def sum(array):
    sum = 0
    for element in array:
        sum = sum + element
    return sum

my_array = [1,2,3,4,5]
result = sum(my_array)
print('The sum of the array is:',result)


def reverse_array(array):
    left = 0
    right = len(array)-1
    while left < right:
        array[left], array[right] = array[right], array[left]

        left = left +1
        right = right +1

    consider_array = [11,22,3,44,55]
    reverse_array(consider_array)
    print("Reversed array:",consider_array)
    
def is_sorted_ascending(array):
    is_sorted = True
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            is_sorted  = False
            break
    return is_sorted

my = [11,22,33,44,55]
print('the array sorted is:',is_sorted_ascending(my))

def find_element_frequency(array,element):
    count = 0
    for item in array:
        if item == element:
               count = count + 1
    return count

my_array = [1,2,3,4,5,6]
element_to_find = 2
frequency = find_element_frequency(my_array,element_to_find)
print('The frequency of the element to find',frequency)

def remove_duplicates(array):
    unique_set = set()
    unique_array = []
    for item in array:
        if item not in array:
            unique_set.add(item)
            unique_array.append(item)
    return unique_array

my_array = [ 11,11,22,22,33,44,55,66,77]
unique_result = remove_duplicates(my_array)
print('Array with duplicates removed:',unique_result)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
n = 5
result = factorial(n)
print('The Factorial of a number is:',result)

def fibonacci(n):
    if n<0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=10
result = fibonacci(n)
print('The febonacci series is:',fibonacci(n))


def sum_of_natural_numbers(n):
    if n<0:
        return 0
    else:
        return n + sum_of_natural_numbers(n-1)

n = 5
result = sum_of_natural_numbers(n)
print('The sum is :',sum_of_natural_numbers(n))
'''