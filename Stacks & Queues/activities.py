import node

# def length(node, count=0):
#     if node is None:
#         return count
#     else:
#         node = node.get_next()
#         count += 1
#         return length(node, count)

# def total(node, sum=0):
#     if node is None:
#         return sum
#     else:
#         sum += node.get_value()
#         next = node.get_next()
#         return total(next, sum)

def length(node):
    count = 0
    while node is not None:
        count += 1
        node = node.get_next()
    return count

def total(node):
    sum = 0
    while node is not None:
        sum += node.get_value()
        node = node.get_next()
    return sum
'''
push(5)
5
push(8)
8
5
pop()
5
push(3)
3
5
pop()
5
push(1)
1
5
'''
def main():
    node1 = node.Node(3)
    node2 = node.Node(2, node1)
    node3 = node.Node(1, node2)
    print(node3)
    # \_[O.O]_/ \_[O.O]_/ C H A L L E N G E ! ! ! \_[O.O]_/ \_[O.O]_/ 
    node3 = node.Node(1,node.Node(2,node.Node(3)))
    print(node3)
    print(length(node3))
    print(total(node3))

if __name__ == "__main__":
    main()