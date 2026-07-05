class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def insert(root, data):
	if root is None:
		return Node(data)

	if data < root.data:
		root.left = insert(root.left, data)
	else:
		root.right = insert(root.right, data)
	return root

def inorder_iterative(root):
	stack = []
	current = root 
	while True:
		if current:
			stack.append(current)
			current = current.left
		elif stack:
			current = stack.pop()
			print(current.data, end=" ")
			current = current.right
		else:
			break

def preorder_iterative(root):
	if root is None:
		return
	stack = [root]
	while stack:
		node = stack.pop()
		print(node.data, end=" ")

		if node.right:
			stack.append(node.right)
		if node.left :
			stack.append(node.left)

def postorder_iterative(root):
	if root is None:
		return root
	stack1 = [root]
	stack2 = []
	while stack1:
		node = stack1.pop()
		stack2.append(node)
		if node.left:
			stack1.append(node.left)
		if node.right:
			stack1.append(node.right)
	while stack2:
		print(stack2.pop().data, end= " ")


root = None
n = int(input("Enter number of elements: "))

for i in range(n):
    data = int(input(f"Enter element {i + 1}: "))
    root = insert(root, data)

print("\nInorder Traversal (Iterative):")
inorder_iterative(root)

print("\nPreorder Traversal (Iterative):")
preorder_iterative(root)

print("\nPostorder Traversal (Iterative):")
postorder_iterative(root)

print()
