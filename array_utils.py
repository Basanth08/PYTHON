import random, arrays

def random_array(size, min_value =0, max_value=None):
    random.seed(1)
    if max_value == None:
        max_value = size
    array = arrays.Array(10)
    for i in range(len(array)):
        array[i] = random.randint(min_value, max_value)
    return array

def range_array(start, stop, step = 1):
    array_range = range(start, stop, step)
    array_range_length = len(array_range)
    array = arrays.Array(array_range_length)
    for i in range(len(array)):
        array[i] = array_range[i]
    return array

def main():
    print(random_array(10))
    print(range_array(1,10,1))

if __name__ == "__main__":
    main()