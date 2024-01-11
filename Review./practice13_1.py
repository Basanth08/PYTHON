import csv

def find_streets(filename, strname):
    """Prints all streets with given street name from CSV file"""
    
    try:
        with open(filename) as f:
            r = csv.reader(f)  
            h = next(r)
            f = False
            for row in r:
                if row[0].lower() == strname.lower():
                    street = row[0] + " " + row[1] + " " + row[2]
                    print(street)  
                    f = True 
            if not f:
                print("There are no streets found with the name: " + strname)
    except FileNotFoundError:
        print("File " + filename + " not found")
        
def most_popular(filename):
    """
    Time complexity:
    Since we iterate through each row once,O(n) where n is number of rows. 
    """
    street_cnt = { }
    try:
        with open(filename) as f: 
            r = csv.reader(f)
            next(r)
            for row in r:
                street_name = row[0]
                if street_name in street_cnt:
                    street_cnt[street_name] += 1
                else:
                    street_cnt[street_name] = 1
            The_most_popular = max(street_cnt, key=street_cnt.get) 
            return The_most_popular  
    except FileNotFoundError:
        print("File" + filename+  "not found")

def  main():
    find_streets("streets.csv", "mission bay") 
    print(most_popular("streets.csv"))
    
if __name__ == "__main__":
    main()