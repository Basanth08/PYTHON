def square(x):
    return x ** 2
def double(x):
    return x * 2
def negate(x):
    return x * -1
def apply_transformation(a_list, function):
    new_list = []
    index = 0
    while index<len(a_list):
        new_list.append(function(a_list[index]))
        index += 1
    return new_list

def main():
    blist = [11,22,33,44,55,66,77]
    print(apply_transformation(blist,square(blist)))

if __name__ == "__main__":
    main()