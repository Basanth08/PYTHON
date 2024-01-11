import arrays
import time
import random
import hashlib
def unique_array(an_array,value):
    is_present = True
    for i in range(len(an_array)):
            if an_array[i] == value:
                is_present = False
            if an_array[i] == None and is_present:
                an_array[i] == value
    return an_array
    
def fill_array(length):
    an_array = arrays.Array(length,None)    
    for i in range(length):
        unique_array(an_array,i)
    return an_array

def unique_list(a_list,value):
    is_present = True
    for i in range(len(a_list)):
            if a_list[i] == value:
                is_present = False
            if a_list[i] == None and is_present:
                a_list.append(value)
    return a_list

def fill_list(length):
    a_list = []    
    for i in range(length):
        unique_array(a_list,i)
    return a_list

def sets():
    a_set = {1,2,3,4}
    print(a_set)
    a_set.add(6)
    a_set.add(9)
    a_set.add(20)
    print(a_set)
    string = "Helloworld"
    astring = set(string)
    print(astring)

def unique_set(a_set,value):
    if value not in a_set:
          a_set.add(value)

def coupon_collector(n):
    boxes = 0
    coupon_set = set()
    while len(coupon_set) < n:
         r = random.randint(1,n)
         coupon_set.add(r)
         boxes = boxes + 1
    return boxes
def mixup():
     stringchars = "basanth"
     stringset = set(stringchars)
     for i in stringset:
          print(i , end = "  ")
     print("")

def unique_words(filename):
    a_set = set()
    with open(filename) as file:
         for line in file:
              words = line.split()
              for word in words:
                   a_set.add(word.lower())
    return a_set

def names():
    names = dict()
    names["three"] = "kumar"
    names["two"] = "basanth"
    names["one"] = "varaganti"
    return names
  
def print_dict(dictionary):
  for key in dictionary:
    value = dictionary[key]
    print(key, ":", value)

         
    # is_present = True
    # for i in range(len(a_set)):
    #         if a_set[i] == value:
    #             is_present = False
    #         if a_set[i] == None and is_present:
    #             a_set.append(value)
    # return a_set

# def fill_set(length):
#     a_set = set()    
#     for i in range(length):
#         unique_array(a_set,i)
#     return a_set
     
def count_words(filename):
    count = 0
    with open(filename) as file:
        for lines in file:
            words = lines.split()
            for word in words:
                word = words.lower()
                if word in count_words:
                    count_words[word] += 1
                else:
                    count_words[word] = 1

    return count_words

def find_maximum(dict):
    max_value = max(dict.values())
    for key, value in dict.items():
        if value == max_value:
            return {key:value}
def hashes():
    print(hash("Hello World!"))
    print(hash("Hello world!"))
    print(hash("A"*100000))
    print(hash("A"*10000000000))

def collisions(filename,length,hash_func=hash):
  
  array = [None] * length
  
  count = 0
  
  with open(filename) as f:
    for line in f:
      line = line.strip()
      if line:
        hash_code = hash_func(line)
        index = hash_code % length
        if array[index] is None:
          array[index] = line
          count += 1
        else:
          return count
  
  return count

def ascii_codes(a_string):
    for char in a_string:
        print(char,'i',ord(char), sep = " ")  

def main():
    # an_array = [11,22,33,44,455,None]
    # array = unique_array(an_array,4)
    # print(array)
    # start_time = time.time()
    # fillarray = fill_array(5000)
    # print(fillarray)
    # elapsed_time = time.time() - start_time
    # print("Elapsed time: %s" % elapsed_time)
    # # sets()
    # n = 10
    # coups =  coupon_collector(n)
    # print(coups)
    # mixing = mixup()
    # print(mixing)
    # counting = unique_words('data/alice.txt')
    # print(counting)
    # name = names()
    # print(name["two"])
#     my_dict = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York"
#   }
#     print_dict(my_dict)
    # count_words('data/alice.txt')
    # my_dict = {'a':5, 'b':10, 'c':20}
    # max_pair = find_maximum(my_dict)
    # print(max_pair)
    # hashes()
    # filename = "data/alice.txt"
    # print("hashes before collision (10):",collisions(filename,10,hash))
    # ascii_codes("j")
if __name__ == "__main__":
    main()

