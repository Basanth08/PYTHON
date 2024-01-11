def calculate_total_cost(quantity):
    if(quantity >= 1 and quantity < 10):
        total_quantity = 50 * quantity
    elif(quantity >= 10 and quantity < 20):
        total_quantity = 45 * quantity
    elif(quantity >= 20 and quantity < 30):
        total_quantity = 38 * quantity
    else:
        total_quantity = 32 * quantity    
    return total_quantity

def main():
    quantity = int(input("What is the quantity purchased: "))
    if(quantity<=0):
        print("Goodbye!")
    else:
        print("Total cost: ",str(calculate_total_cost(quantity)))

if __name__ == "__main__":
    main()
