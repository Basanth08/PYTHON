import random
def random_list(length):
    a_list = [random.randint(0,length) for i in range(length)]
    return a_list
def swap(a_list,a,b):
    temp = a_list[a]
    a_list[a] = a_list[b]
    a_list[b] = temp
    return a_list

def shift(a_list,index):
    while index > 0 and a_list[index] < a_list[index - 1]:
        swap(a_list,index,index -1)
        index -= 1
    return a_list
       
def insertion_sort(a_list):
    for i in range(len(a_list)):
        shift(a_list,i)
    return a_list

def shift_wo_swap(a_list,index):
    target = a_list[index]
    target_index = index
    while target_index > 0 and a_list[target_index-1] > target:
        a_list[target_index] = a_list[target_index - 1]
        target_index -= 1
    a_list[target_index] = target
    return a_list

def insertion_sort_wo_swap(a_list):
    for i in range(len(a_list)):
        shift_wo_swap(a_list,i)
    return a_list

def split(alist):
    l =len(alist)
    midpoint = l//2
    l_slice = alist[:midpoint]
    r_slice = alist[midpoint :]
    return l_slice , r_slice

def merge(left, right):
    merged = []
    i1 = 0
    i2 = 0
    while i1 < len(left) and i2 < len(right):
        if left[i1] <= right[i2]:
            merged.append(left[i1])
            i1 = i1 + 1
        else:
            merged.append(right[i2])
            i2 = i2 + 1
    if i1 < len(left):
            for j in range(i1,len(left)):
                merged.append(j)
    else:
        for j in range(i2,len(right)):
            merged.append()
    return merged

def partition(alist,pivot):
    less_than =[]
    same = []
    more_than = []

    for i in alist:
        if i < pivot:
            less_than.append(i)
        elif i == pivot:
            same.append(i)
        else:
            more_than.append(i)
    return less_than , same, more_than
def quicksort(alist):
    if len(alist)<2:
        return alist
    else:
        pivot =alist[0]
        less,same,more = partition(alist,pivot)
        sorted_less = quicksort(less)
        sorted_more = quicksort(more)
        sorted_less +=same
        sorted_more += sorted_more
        return sorted_less

def main():
    print(random_list(5))
    a_list = random_list(10)
    print("Here's the list before swapping",a_list)
    print("Values after swapping",swap(a_list,4,5))
    print("Values after swapping",swap(a_list,3,8))
    vlist = random_list(10)
    print("shifting",shift(vlist,6))
    b_list = [3,2,4,5,6,8,9]
    print("Before",b_list)
    print("after",shift(b_list,4))
    c_list = random_list(10)
    print(insertion_sort(c_list))
    dlist = [11,22,33,44,55]
    print(insertion_sort_wo_swap(dlist))
    print(insertion_sort_wo_swap(dlist))
    elist = list(range(1,10))
    print(split(elist))
    oddlist = [0,1,2,3,4,5,6,7,8,9,10]
    evenlist = [1,2,3,4,5,6,7,8,9,0]
    print(split(oddlist))
    print(split(evenlist))
    hlist = [1,22,33,4,55,6,77]
    print(partition(hlist,33))
if __name__ == "__main__":
    main()















