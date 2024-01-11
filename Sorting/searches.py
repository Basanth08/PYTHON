def linear_search(a_list, target):
    """
    Searches a list for a target value.
    """
    for index in range(len(a_list)):
        if a_list[index] == target:
            return index
    return None

def increasing_comparator(a,b):
        return a<= b
 
def decreasing_comparator(a,b):
        return a>=b 
    
def binary_search(a_list, target, comparator = increasing_comparator, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(a_list) - 1

    if start > end:
        return None
    else:
        mid = (start + end) // 2
        if a_list[mid] == target:
            return mid
        elif comparator(a_list[mid] < target):
            start = mid + 1
            return binary_search(a_list, target, start, end)
        else:
            end = mid - 1
            return binary_search(a_list, target, start, end)

    
def main():
    a_list = list(range(1, 10000001))
    print(binary_search(a_list, 1))
    print(binary_search(a_list, 5000000))
    print(binary_search(a_list, 10000000))
    print(binary_search(a_list, 0))
    blist = list(range(1000,0,-1))
    print(binary_search(blist,400))
    print(binary_search(blist,20))
    print(increasing_comparator(11,3))
    print(decreasing_comparator(5,6))
    clist = list(range(1000000,1,-1))
    print(binary_search(clist,2,decreasing_comparator))
    print(binary_search(clist,100000,decreasing_comparator))
if __name__ == "__main__":
    main()