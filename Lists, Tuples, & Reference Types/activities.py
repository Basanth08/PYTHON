import random
import arrays
'''
def tuples(a_tuple):
    print("Length:", len(a_tuple))
    print("Tuple:", a_tuple)
    print("Tuple elements: ", end="")
    for i in a_tuple:
        print(i, end = " ")

def packer():
    a = "Hello"
    b = 25
    c = False
    d = 44.4
    return a,b,c,d

def lists():
    x = ["Hello", 42, 42.5, True, ["hello", 2]]
    for i in range(len(x)):
        print(i,":", x[i])
    x[1] = 99
    return x

def make_list(a_sequence):
    a_list = []
    for i in a_sequence:
        a_list.append(i)
        print(a_list)
    return a_list

def scale(a_list, scalar):
    for i in range(len(a_list)):
        new_i = a_list[i] * scalar
        a_list[i] = new_i
    return a_list

def mutator(a_list, an_int):
    print("mutator in:", an_int, a_list)
    an_int = an_int * 5
    a_list[0] = a_list[0] * 5
    print("mutator out:", an_int, a_list)

def cat(a_list, b_list):
    return a_list + b_list

def extender(a_list, b_list):
    a_list += b_list
    return a_list

def inserter(a_list, value):
    middle = int(len(a_list)/2)
    new_list = a_list.insert(middle,value)
    return new_list

def popper(a_list):
    for i in range(len(a_list)):
        randomi = random.randint(0,len(a_list)-1)
        a_list.pop(randomi)
        print(a_list)

def popper_recursion(a_list):
    print(a_list)
    if len(a_list) == 0:
        return
    else:
        a_list.pop()
        return popper_recursion(a_list)

def array_insert(an_array, index, value):
    length = len(an_array)
    if length ==0:
        return arrays.Array(1, value)
    else:
        inserted = arrays.Array(length + 1)
        for i in range(index):
            inserted[i] = an_array[i]
        inserted[index] = value
        for i in range(index+1, length+1):
            inserted[i] = an_array[i-1]
        return inserted

def array_pop(an_array, index):
    length = len(an_array)
    if length ==0:
        return arrays.Array(1)
    else:
        popped = arrays.Array(length - 1)
        for i in range(index):
            popped[i] = an_array[i]
        for i in range(index+1, length):
            popped[i-1] = an_array[i]
        return popped, an_array[index]

def rgb_tuple():
    red = random.random()
    green = random.random()
    blue = random.random()
    return (red, blue, green)

def tuple_equality(tup1, tup2):
    print(tup1, tup2, sep= '\n')
    print("is", tup1 is tup2)
    print("==",tup1 == tup2)

def reverse_sequence(seq):
    alist = []
    for i in range(len(seq)-1, -1, -1):
        alist.append(seq[i])
    return alist
def slices():
    alist = []
    quote = "The best way to get"
    # The best way to get something done… if you, if you hold it near and dear to you, that you uh, um like to be able to uh… … anyway… I’m… r-ready to get a lot done." - Joe Biden
    for i in quote:
        alist.append(i)
    
    print(alist[0:3])
    print(alist[4:8])
    print(alist[9:12])
    print(alist[13:15])
    print(alist[16:19])

def dices(seq):
    if seq == []:
        return
    else:
        print(seq[0:1])
        return dices(seq[1:])
        
def swapper(a_list):
    length = len(a_list)
    if length <2:
        return a_list
    else:
        mid_point = length//2
        swapped_list = []
        for i in range(mid_point,length):
            swapped_list.append(a_list[i])
        for i in range(mid_point):
            swapped_list.append(a_list[i])

    return swapped_list

#[1,2,3,4,5,6,7,8]
def chunky(a_list,size):
    start =0
    stop = size
    chunk = a_list[start:stop]
    while chunk:
        print(chunk)
        start = stop
        stop = start + size
        chunk = a_list[start:stop]

    return chunk
    
def comprehension():
    print([0 for _  in range(15)])
    print([i for i in range(13)])
    print([i for i in  range(20) if i%2 ==0])   
    print([i for i in range(50) if i%3==0 or i%5==0]) 
    print([item for  item in "foobar"])

def make_table(rows,columns,value):
    table = []
    for _ in range(rows):
        row = [value] * columns
        table.append(row)
        print(row)
    return table


def random_list(size):
    a_list = [random.randint(0,100) for _ in range(size)]
    return a_list

def sorted_test(a_list,backward=False):
    print("before:",a_list)
    sorted_list = sorted(a_list, reverse = backward)
    print("after:",a_list)
    print("sorted",sorted_list)
'''
def sort_cards(hand):
    print(hand)
    print(hand.sort())

def main():
    '''
    x = ("a", 123, False)
    tuples(x)
    print()
    print("")
    packed = (packer())
    print("Packed:", packed)
    packed_a = packed[0]
    packed_b = packed[1]
    packed_c = packed[2]
    packed_d = packed[3]
    print(packed_a)
    print(packed_b)
    print(packed_c)
    print(packed_d)
    print("")
    print("List:")
    print(lists())
    print("")
    print("Mutating list:")
    print(make_list([1,2,3,4,5,6,7,8,9,10]))
    listA = [1,2,3,4,5,6,7,8,9,10]
    print("Before:", listA)
    listB = scale(listA, 5)
    print(listB, end = '\n\n')
    an_int = 7
    a_list = [an_int]
    print("before:", an_int, a_list)
    mutator(a_list, an_int)
    print("after:", an_int, a_list, end = '\n\n')
    print("Concatenation:")
    b_list = ['a','b','c']
    c_list = [1,2,3]
    cat_list = cat(b_list, c_list)
    print(b_list, c_list, cat_list, sep = '\n')
    b_list = ['a','b','c']
    c_list = [1,2,3]
    cat_list = cat(b_list, c_list)
    d_list = ["Harry"]
    e_list = ["Potter"]
    de_list = extender(d_list, e_list)
    print(d_list, e_list, de_list, sep = '\n')
    print("is d_list de_list?", d_list is de_list, end = '\n\n')
    print(".insert(index, value) function")
    empty_list = []
    inserter(empty_list, 3)
    print(empty_list)
    inserter(empty_list, 4)
    print(empty_list)
    inserter(empty_list, 'apple')
    print(empty_list, '\n')
    print(".pop(index, value) function")
    full_list = [1,2,3,4,5,6,7,8,9]
    popper(full_list)
    full_list2 = [1,2,3,4,5,6,7,8,9]
    popper_recursion(full_list2)
    print("")
    print("Array_Insert")
    fresh_array = [0,1,2,3,4,5,6,7,8,9,10]
    print(fresh_array)
    fresher_array = array_insert(fresh_array, 4, 24)
    print(fresher_array)
    print(array_pop(fresher_array, 2),end='\n\n')
    print(rgb_tuple())
    print(rgb_tuple())
    print(rgb_tuple())
    print("")
    print("is vs ==")
    print("-------------------")
    list1 = ["apple", 4, 7.3]
    tuple1 = tuple(list1)
    tuple_equality(list1, tuple1)
    tuple2 = tuple(list1)
    tuple_equality(tuple1, tuple2)
    tuple3 = (4, 7.3, "apple")
    tuple_equality(tuple2, tuple3)
    fresh_array2 = [0,1,2,3,4,5,6,7,8,9,10]
    print(fresh_array2)
    print(reverse_sequence(fresh_array2))
    fresh_array3 = ["apple", "banana", "orange"]
    print(fresh_array3)
    print(reverse_sequence(fresh_array3))
    fresh_array4 = [5,7,9,11,13,15]
    print(fresh_array4)
    print(reverse_sequence(fresh_array4))
    slices()
    fresh_array5 = [0,1,2,3,4,5,6,7,8,9,10]
    dices(fresh_array5)
    
    a_list = [1,2,3,4,5,6]
    print(swapper(a_list))


    a_list = [1,2,3,4,5,6,7,8,9,10]
    result = chunky(a_list,2)
    print(result)
    
    print(comprehension())

result = make_table(3,3,5)
print(result)

    result = random_list(9)
    print(result)
    a_list = [1,3,2,4,5,7,98,76,1,56,87]
    result = sorted_test(a_list)
    print(result)


'''
    hand = [(5,"H") , (2,"D"), (10,"S"), (7,"S"), (10,"c")]
    sort_cards(hand)
if __name__ == "__main__":
    main()