class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# BST insertion
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

# Find smallest element
def find_smallest(root):
    if root is None:
        return None
    current = root
    while current.left:
        current = current.left
    return current.data

# Main program
root = None
n = int(input("Enter number of elements: "))
for i in range(n):
    data = int(input(f"Enter element {i+1}: "))
    root = insert(root, data)

smallest = find_smallest(root)
print("Smallest element:", smallest)
