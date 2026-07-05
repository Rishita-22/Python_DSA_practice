class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to insert elements into the binary tree (level order)
def insert_level_order(arr, root, i, n):
    if i < n:
        temp = Node(arr[i])
        root = temp

        # insert left child
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

        # insert right child
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root


# Inorder traversal (Left → Root → Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# ---------- MAIN PROGRAM ----------
n = int(input("Enter number of elements: "))
elements = []

for i in range(n):
    data = int(input(f"Enter element {i + 1}: "))
    elements.append(data)

root = None
root = insert_level_order(elements, root, 0, n)

print("\nInorder Traversal of the Binary Tree:")
inorder(root)
print()
