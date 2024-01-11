import arrays
import array_utils
import math
def max(array,index=0,max_value=None):
    if len(array) == 0:
        return None
    if index == len(array):
        return max_value
    if max_value is None or array[index] > max_value:
        max_value = array[index]
    return max(array, index + 1, max_value)

def power(base,exponent):
    if exponent < 0:
         return 'Undefined'
    if exponent == 0:
         return 1
    if exponent == 1:
         return base
    if exponent %2 ==1:
         return base * power(base,exponent//2)*power(base,exponent//2)
    else:
         return power(base,exponent//2) * power(base,exponent//2)
                  

def main():
    an_array = array_utils.range_array(0,10)
    largest = max(an_array)
    print(largest)
    result = power(4,7)
    print(result)

if __name__ == "__main__":
    main()