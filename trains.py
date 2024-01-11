import node_stack
"""
Problem 1
"""
class Product:
    __slots__ = ["__product_code", "__name"]

    def __init__(self, product_code, name):
        self.__product_code = product_code
        self.__name = name

    def get_code(self):
        return self.__product_code
    
    def get_name(self):
        return self.__name
    
    def __eq__(self, other):
        return (
        self.__product_code == other.__product_code and 
        self.__name == other.__name 
        )

    def _hash_(self):
        return hash(self.__product_code)
    
    def _str_(self):
        return self.__product_code + " " +self.__name
    
    def _lt_(self, other):
        return self.__product_code < other.__product_code
   
"""
Problem 02
"""
class TrainCar:
    __slots__ = ["__capacity"]
    def _init_(self, capacity):
        self.__capacity = capacity

    def get_capacity(self):
        return self.__capacity

    def is_empty(self):
        return True

    def is_full(self):
        return False

    def _str_(self):
        return "[]"

"""
Problem 03
"""
class TrainCar:
    __slots__ = ["__capacity", "__products"]
    def _init_(self, capacity):
        self.__capacity = capacity
        self.__products = []

    def get_capacity(self):
        return self.__capacity

    def is_empty(self):
        return len(self.__products) == 0

    def is_full(self):
        return len(self.__products) >= self.__capacity

    def load(self, product):
        if self.is_full():
            raise ValueError("Train car is full!")
        self.__products.insert(0, product)

    def unload(self):
        if self.is_empty():
            raise ValueError("Train car is empty!") 
        return self.__products.pop(0)

    def _str_(self):
        return str(self.__products)
   
"""
Problem 4

"""
def load_train(products, capacity):
    train = []
    current_car = None
    for product in products:
        if current_car is None or current_car.is_full():
            current_car = TrainCar(capacity)
            train.append(current_car)
        current_car.load(product)
    return train

"""
Problem 5
"""
def unload_train(train):
    products = []
    for car in train:
        while not car.is_empty():
            products.append(car.unload())
    return products

  
    