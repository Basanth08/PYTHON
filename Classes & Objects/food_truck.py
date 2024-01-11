class Combo:
    def __init__(self, code, items):
        self.code = code  
        self.items = items 

    def price(self, prices):
        total = 0
        for code in self.items:  
            name = codes[code] 
            price = prices[name] 
            total = total + price 
        return total    
    
prices = {"soda": 1.95, "milk shake": 2.95, "tea": 2.15,
          "burger": 3.95, "cheese burger": 4.45, "chicken fingers": 4.95, 
          "fries": 1.95, "roti channa": 2.95, "cole slaw": 2.45,}

# codes = {"soda": "s", "milk shake": "ms", "tea": "t", 
#          "burger": "b", "cheese burger": "cb", "chicken fingers": "cf",
#          "fries": "f", "roti channa": "rc", "cole slaw": "cs" }

codes = {}
for names, price in prices.items():
    code = ""
    for element in names.split():
        code = code + element[0]
    codes[code] = names

menu = {
  'drinks': {
    's': 'soda',
    'ms': 'milk shake',
    't': 'tea'
  },
  'entrees': {  
    'b': 'burger',
    'cb': 'cheese burger',
    'cf': 'chicken fingers'
  },
  'sides': {
    'f': 'fries',
    'rc': 'roti channa', 
    'cs': 'cole slaw'
  }
}
def print_menu():
  for category in menu:
    print(category)
    for code, name in menu[category].items():
      price = prices[name]
      print(name, '(', code, ') $', price) 
    print()

def print_order(order):
  total = 0
  for combo in order:
    print(combo.items[0], combo.items[1], combo.items[2])  
    total = total + combo.price(prices)
  print('Total: $', total)

def main():
  print_menu()
  order = []
  while True:  
    drinks = input("What would you like to drink: ")
    if drinks not in codes:
        print("Invalid drink code. Try again.")
        continue
    entree = input("What would you like for your entree: ")
    if entree not in codes:
        print("Invalid entree code. Try again.")
        continue
    side = input("What would you like for your side: ")
    if side not in codes:
        print("Invalid side code. Try again.")
        continue   
    combo = Combo(codes[drinks],[drinks, entree, side])
    order.append(combo)
    
    print("Drink:", combo.items[0])
    print("Entree:", combo.items[1]) 
    print("Side:", combo.items[2])
    print("Price:", combo.price(prices))
    
    anything_else = input("Would you like to add another combo (Y/N): ")
    if (anything_else =="N" or anything_else =="n"):
       break
  print("Your order is:")
  print_order(order)

if __name__ == "__main__":
    main()
