class Fruit:
    __slots__ = ["type", "price"]

    def __init__(self,type="None",price=0):
        self.type = type
        self.price = price

APPLE = Fruit("apple", 1.35)
ORANGE = Fruit("orange", 1.00)
BANANA = Fruit()

def add_to_basket(basket, fruit):
    if fruit == APPLE.type.lower():
        basket.append(APPLE)
    elif fruit == ORANGE.type.lower():
        basket.append(ORANGE)
    elif fruit == "":
        return ""
    else:
        print("Unknown Fruit")

def price_getter(basket):
    price_sum = 0
    for i in basket:
        price_sum+=i.price
    return price_sum

def fruit_count(basket, fruit):
    count = 0
    for i in basket:
        if i.type == fruit.type:
            count+=1
    return count

def main():
    basket = []
    fruit = None
    while fruit !="":
        fruit = input("Enter the name of fruit to add to basket, or nothing to stop shopping. ")
        add_to_basket(basket, fruit)
    print(price_getter(basket))
    print(fruit_count(basket,APPLE))

if __name__ == "__main__":
    main()

