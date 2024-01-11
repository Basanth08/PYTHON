import random
import math
PI = 3.14

def squared(x):
    return math.pow(x,2)

def cubed(x):
    return math.pow(x,3)

#def even_or_odd(x):
   # if x % 2 == 0:
      #  return "even"
   # if x % 2 != 0:
       # return "odd"
    
def coin_toss_heads(number):
    number = random.randint(1,2)
    if number == 1:
        return "heads"
      
def coin_toss_tails(number):
    number = random.randint(1,2)
    if number == 2:
        return "tails"
    
#def circum_circle(r):
   # circum = 2 * PI * r
   #return circum

#def area(r):
 #   area = PI * r * r
  #  return area
    
def main():
    n = int(input("Enter a value:"))
    print("The square of the value is:", squared(n))
    print("The cube of the value is:", cubed(n))
   # print("Even or odd:",even_or_odd(n))
    print("is it heads or tails  :", coin_toss_heads(n))
    print("it is tails:",coin_toss_tails(n))
   # print("circumference of circle:",circum_circle(n))
   # print("area of circle:", area(n))

if __name__ == "__main__":
    main()

