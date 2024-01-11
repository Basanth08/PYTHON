import random
min = -100
max = 100

def absolute_difference(a,b):
    if a > b:
        return a-b
    else:
        return b-a
    
    
def main():
    c = random.randint(min,max)
    d = random.randint(min,max)
    anss = absolute_difference(c,d)
    a = str(c)
    b = str(d)
    ans = str (anss)
    print( str(a) + "-" + str(b) + "=" + str(ans))


    

if __name__ == "__main__":
    main()