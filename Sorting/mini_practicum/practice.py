def in_place_reverse(a_list):
    n = len(a_list)
    for i in range(n//2):
        a_list.insert(i, a_list.pop(-i-1))
        

#the time complexity is O(n). 
def make_multiplication_table():
    '''Using list comprehension'''
    return [[i*j for i in range(1,11)] for j in range(1,11)]



def main():
    a_list = ['a','b', 2, 4, 5] 
    print("Original list:", a_list) 
    in_place_reverse(a_list) 
    print("Reversed list:", a_list) 
    multiplication= make_multiplication_table()
    for row in multiplication:
        print(row)

  


if __name__ =="__main__":
    main()


