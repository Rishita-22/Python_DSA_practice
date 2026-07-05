class Node:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



head = Node(10)
second = Node(20)


head.next = second


print("Two Node Linked List:")
ptr = head
while ptr is not None:
    print(ptr.data, end=" -> ")
    ptr = ptr.next
print("None")
