from list_stack import*

def test_init():
    stack = liststack()
    assert stack.is_empty()
    assert len(stack) == 0

def test_repr():
    stack = liststack()
    stack.push("a")
    stack.push("b")
    assert repr(stack) == "['b', 'a']"

def test_push():
    stack = liststack()
    elements_to_push = [1]
    stack.push(elements_to_push)
    assert len(stack) == 1
 
def test_push_pop():
    stack = liststack()
    stack.push("a")  
    stack.push("b")
    assert stack.pop() == "b"
    assert stack.pop() == "a"

def test_peek():
    stack = liststack()
    stack.push("a")   
    assert stack.peek() == "a"
    

if __name__ == "__main__":
    main(())