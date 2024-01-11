import math
import random 
PI = 3.14


#defining the fact function.
#Here x is the parameter.We only fing the factorila for the numbers greater than zero.
def fact(x):
    if x > 0:
        return math.factorial(x)
    else:
        return 0
    #if you give negative number as the input you get zero as the output.

#we use the root func to find the roots of the number.
def root(x):
    if x > 0:
        return math.sqrt(float(x))
    else:
        return 0
#we get zero as the output when we give negative numbers as the input.
#Trunk func gives the truncated integer part of a number.
def trunk(x):
    if x > 0:
        return math.trunc(x)
    else:
        return 0
#we get zero as the output if we negative numbers as the input.
def main():
    n = int(input("Enter the value:"))
    print("The Factorial of the value is:",fact(n))
    print("The Square root of the value is:",root(n))
    print("The trunc value is:",trunk(n))


if __name__ == "__main__":
    main()

