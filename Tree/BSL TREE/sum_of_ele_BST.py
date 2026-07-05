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

# Sum of elements (iterative)
def sum_of_elements(root):
    if root is None:
        return 0
    stack = [root]
    total = 0
    while stack:
        node = stack.pop()
        total += node.data
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return total

# Main program
root = None
n = int(input("Enter number of elements: "))
for i in range(n):
    data = int(input(f"Enter element {i+1}: "))
    root = insert(root, data)

total_sum = sum_of_elements(root)
print("Sum of all elements:", total_sum)
