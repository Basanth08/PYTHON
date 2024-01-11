import math
def add(x,y):

    result = x + y
    result_string = str(x) + "+" + str(y) + "=" + str(result)
    return result_string

def sub(x,y):
    result = x - y
    result_string = str(x) + "-" + str(y) + "=" + str(result)
    return result_string

def mul(x,y):
    result = x * y
    result_string=str(x) + "*" + str(y) + "=" + str(result)
    return result_string

def div(x,y):
    result = x / y
    result_string = str(x) + "/" + str(y) + "=" + str(result)
    return result_string

def exp(x,y):
    result = math.pow(x,y)
    result_string = str(x) + "**" + str(y) + "=" + str(result)
    return result_string

def main():
    x = int(input("Enter the value of x:"))
    y = int(input("Enter the value of y:"))
    print(add(x,y))
    print(sub(x,y))
    print(mul(x,y))
    print(div(x,y))
    print(exp(x,y))

if __name__ == "__main__":
    main()
