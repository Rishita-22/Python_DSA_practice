class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_node():
    data = input("Enter node data (or 'None' to skip): ")
    if data.lower() == "none":
        return None

    node = Node(int(data))
    print(f"Enter left child of {data}:")
    node.left = create_node()

    print(f"Enter right child of {data}:")
    node.right = create_node()

    return node


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# ---------- MAIN PROGRAM ----------
print("Create Binary Tree:")
root = create_node()

print("\nInorder Traversal of the Binary Tree:")
inorder(root)
print()
