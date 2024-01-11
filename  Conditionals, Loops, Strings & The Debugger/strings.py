def indexing():
    a_string = "varagantibasanth"
    print(len(a_string))
    print(a_string[1])
    print(a_string[14])
    print(a_string[5] + a_string[8])
    print(a_string[-2] + a_string[-5]) 
def concat():
    a = "cat"
    b = "tail"
    a = a+b

    print(a)

    x = "age" + str(22)
    print(x)



def main():
    indexing()
    concat()


if __name__ == "__main__":
    main()