class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



head = Node(10)
second = Node(20)
third = Node(30)


head.next = second
second.next = third


print("Three Node Linked List:")
ptr = head
while ptr is not None:
    print(ptr.data, end=" -> ")
    ptr = ptr.next
print("None")
