class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.ht = 0


def height(node):
    if node is None:
        return 0

    lh = 0 if node.left is None else 1 + node.left.ht
    rh = 0 if node.right is None else 1 + node.right.ht

    return max(lh, rh)


def balFact(node):
    if node is None:
        return 0

    lh = 0 if node.left is None else 1 + node.left.ht
    rh = 0 if node.right is None else 1 + node.right.ht

    return lh - rh


def rotateright(x):
    y = x.left
    x.left = y.right
    y.right = x

    x.ht = height(x)
    y.ht = height(y)
    return y


def rotateleft(x):
    y = x.right
    x.right = y.left
    y.left = x

    x.ht = height(x)
    y.ht = height(y)
    return y


def LL(node):
    return rotateright(node)


def RR(node):
    return rotateleft(node)


def LR(node):
    node.left = rotateleft(node.left)
    return rotateright(node)


def RL(node):
    node.right = rotateright(node.right)
    return rotateleft(node)


def insert(node, x):    
    if node is None:
        return Node(x)

    if x > node.data:
        node.right = insert(node.right, x)
        if balFact(node) == -2:
            if x > node.right.data:
                node = RR(node)
            else:
                node = RL(node)

    elif x < node.data:
        node.left = insert(node.left, x)
        if balFact(node) == 2:
            if x < node.left.data:
                node = LL(node)
            else:
                node = LR(node)

    node.ht = height(node)
    return node


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(f"val : {node.data} ----- BF : {balFact(node)}")
        inorder(node.right)



# -------- MAIN --------
root = None

root = insert(root, 50)
print(root)
root = insert(root, 30)
print(root)
root = insert(root, 40)
print(root)
root = insert(root, 70)
print(root)
root = insert(root, 90)
print(root)
root = insert(root, 95)
print(root)
root = insert(root, 80)
print(root)
root = insert(root, 85)
print(root)
root = insert(root, 75)
print(root)

print("Pre Order of AVL : ")
inorder(root)