import node
class Stack:
    __slots__ = ["__top", "__size"]

    def __init__(self) -> None:
        self.__top = None
        self.__size = 0

    def is_empty(self):
        if self.__top == None:
            return True
        else:
            return False

    def __str__(self):
        return self.__str__helper(self.__top)

    def __str_helper(self, node, string=""):
        if node is None:
            return "[" + string[2:] + "]"
        else:
            string += "," + str(node.get_value())
            node = node.get_next()
            return self.__str_helper(node, string)

    def push(self, value):
        new_node = node.Node(value, self.__top)
        self.__top = new_node
        self.__size += 1

    def __len__(self):
        length = 0
        size = self.__size
        node = self.__top
        while node is not None:
            length += 1
            size += 1
            node = node.get_next()
        return length

    def peek(self):
        if self.__top is None:
            raise IndexError("peek from empty stack")
        value = self.__top.get_value()
        return value

    def pop(self):
        top = self.__top
