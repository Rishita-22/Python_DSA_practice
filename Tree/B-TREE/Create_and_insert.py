class Node:
    def __init__(self, leaf=True):
        self.keys = []      # keys stored in this node
        self.child = []     # child pointers (only used if leaf=False)
        self.leaf = leaf    # True if this node has no children


class BTree:
    root = None
    m = 4   # ORDER of the tree -> max children = m, max keys = m-1
            # change this to 3 for a 2-3 tree, keep 4 for 2-3-4 tree

    # ---------- INSERTION ----------

    @staticmethod
    def insert(key):
        root = BTree.root

        # tree empty -> first key becomes root
        if root is None:
            BTree.root = Node()
            BTree.root.keys.append(key)
            return

        # if root is already full (has m-1 keys), it must split BEFORE inserting
        if len(root.keys) == BTree.m - 1:
            new_root = Node(leaf=False)
            new_root.child.append(root)
            BTree.split_child(new_root, 0)   # split old root, push median up
            BTree.root = new_root            # tree grows one level taller
            BTree.insert_nonfull(new_root, key)
        else:
            BTree.insert_nonfull(root, key)

    @staticmethod
    def split_child(parent, i):
        # splits the FULL child at index i of 'parent'
        m = BTree.m
        full_child = parent.child[i]

        mid = (m - 1) // 2          # lower-middle index (our fixed convention)
        median_key = full_child.keys[mid]

        # right half becomes a brand new node
        new_node = Node(leaf=full_child.leaf)
        new_node.keys = full_child.keys[mid + 1:]

        # left half stays in the old node
        full_child.keys = full_child.keys[:mid]

        # if it's an internal node, split its children too
        if not full_child.leaf:
            new_node.child = full_child.child[mid + 1:]
            full_child.child = full_child.child[:mid + 1]

        # push median key up into parent, and attach new_node as a child
        parent.keys.insert(i, median_key)
        parent.child.insert(i + 1, new_node)

    @staticmethod
    def insert_nonfull(node, key):
        i = len(node.keys) - 1

        if node.leaf:
            # shift keys right to make room, then place key in sorted position
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            # find which child to go into
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            # if that child is full, split it first (preemptive split)
            if len(node.child[i].keys) == BTree.m - 1:
                BTree.split_child(node, i)
                if key > node.keys[i]:
                    i += 1

            BTree.insert_nonfull(node.child[i], key)

    # ---------- CREATE (interactive, like your SL.create) ----------

    @staticmethod
    def create():
        c = 0
        ch = 'y'
        while ch == 'y':
            c += 1
            dta = int(input(f"Enter key {c}: "))
            BTree.insert(dta)
            ch = input("To insert new key press y: ")

    # ---------- DISPLAY ----------

    @staticmethod
    def display(node=None, level=0):
        if node is None:
            node = BTree.root
        if node is None:
            print("Tree is empty")
            return

        print("Level", level, ":", node.keys)
        if not node.leaf:
            for c in node.child:
                BTree.display(c, level + 1)


if __name__ == "__main__":
    BTree.create()
    print("\nB-Tree structure (level by level):")
    BTree.display()