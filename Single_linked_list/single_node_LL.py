class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



head = Node(10)


print("Single Node Linked List:")
ptr = head
while ptr is not None:
    print(ptr.data, end=" -> ")
    ptr = ptr.next
print("None")
