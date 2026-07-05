class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to insert a node into the BST
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


# Inorder Traversal (Left → Root → Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# ---------- MAIN PROGRAM ----------
root = None
n = int(input("Enter number of elements: "))

for i in range(n):
    data = int(input(f"Enter element {i + 1}: "))
    root = insert(root, data)

print("\nInorder Traversal of the Binary Search Tree:")
inorder(root)
print()
