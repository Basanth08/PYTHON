class liststack:
    def __init__(self):
        self.elmnts = []
    
    def push(self,elmnts):
        self.elmnts.append(elmnts)
    
    def peek(self):
        if not self.is_empty():
            return self.elmnts[-1]
        
    def pop(self):
        if not self.is_empty():
            return self.elmnts.pop()
    
    def __len__(self):
        return len(self.elmnts)
    
    def is_empty(self):
        return len(self.elmnts) == 0

    def __repr__(self):
        return str(self.elmnts[::-1])
    
from list_stack import*
def main():  
  stack = liststack()
  print(stack)
  print(len(stack))
  print(stack.is_empty())
  # Pushing the elmnts
  stack.push(1) 
  stack.push(2)
  stack.push(3)
  stack.push(4)
  print(stack)
  stack.pop()
  print(stack)
  stack.push(4)
  print(stack)
  print(stack.peek())
  print(len(stack))
  print(stack.pop())
  print(stack.pop())
  print(stack)

if __name__ == "__main__":
    main()