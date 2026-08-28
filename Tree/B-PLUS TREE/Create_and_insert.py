class Node:
    def __init__(self, leaf=True):
        self.keys = []      # keys stored in this node
        self.child = []     # child pointers (only used if leaf=False)
        self.leaf = leaf    # True if this is a leaf (holds real data)
        self.next = None    # only used by LEAF nodes - links to the next leaf


class BPlusTree:
    root = None
    m = 4   # ORDER of the tree -> max children = m, max keys = m-1

    # ---------- INSERTION ----------

    @staticmethod
    def insert(key):
        root = BPlusTree.root

        # tree empty -> first key becomes root (root starts as a leaf)
        if root is None:
            node = Node(leaf=True)
            node.keys.append(key)
            BPlusTree.root = node
            return

        # descend to the correct leaf, remembering the path taken
        # path = list of (parent_node, child_index) pairs
        path = []
        node = root
        while not node.leaf:
            i = 0
            while i < len(node.keys) and key >= node.keys[i]:
                i += 1
            path.append((node, i))
            node = node.child[i]

        leaf = node
        BPlusTree.insert_in_leaf(leaf, key)

        # if leaf did not overflow, we're done
        if len(leaf.keys) < BPlusTree.m:
            return

        # leaf overflowed -> split it, then fix the parent chain
        new_leaf, up_key = BPlusTree.split_leaf(leaf)
        BPlusTree.insert_in_parent(path, leaf, up_key, new_leaf)

    @staticmethod
    def insert_in_leaf(leaf, key):
        # plain sorted insertion into a leaf's key list
        i = len(leaf.keys) - 1
        leaf.keys.append(None)
        while i >= 0 and key < leaf.keys[i]:
            leaf.keys[i + 1] = leaf.keys[i]
            i -= 1
        leaf.keys[i + 1] = key

    @staticmethod
    def split_leaf(leaf):
        m = BPlusTree.m
        mid = (m + 1) // 2     # left half keeps this many keys (ceil(m/2))

        new_leaf = Node(leaf=True)
        new_leaf.keys = leaf.keys[mid:]     # right half
        leaf.keys = leaf.keys[:mid]         # left half stays here

        # keep the leaf-level linked list connected
        new_leaf.next = leaf.next
        leaf.next = new_leaf

        # IMPORTANT: key is COPIED up (not removed) - it still lives in new_leaf
        up_key = new_leaf.keys[0]
        return new_leaf, up_key

    @staticmethod
    def insert_in_parent(path, left_node, up_key, right_node):
        # no parent means left_node WAS the root -> create a new root
        if not path:
            new_root = Node(leaf=False)
            new_root.keys = [up_key]
            new_root.child = [left_node, right_node]
            BPlusTree.root = new_root
            return

        parent, idx = path.pop()   # go back one step up the path we recorded

        # insert the new key and the new right-hand child into the parent
        parent.keys.insert(idx, up_key)
        parent.child.insert(idx + 1, right_node)

        # if parent didn't overflow, we're done
        if len(parent.keys) < BPlusTree.m:
            return

        # parent overflowed -> split it (internal split: key MOVES up, no copy)
        new_internal, moved_key = BPlusTree.split_internal(parent)
        BPlusTree.insert_in_parent(path, parent, moved_key, new_internal)

    @staticmethod
    def split_internal(node):
        m = BPlusTree.m
        mid = m // 2                 # index of the key that moves up

        moved_key = node.keys[mid]   # this key leaves 'node' completely

        new_node = Node(leaf=False)
        new_node.keys = node.keys[mid + 1:]
        new_node.child = node.child[mid + 1:]

        node.keys = node.keys[:mid]
        node.child = node.child[:mid + 1]

        return new_node, moved_key

    # ---------- CREATE (interactive, like your SL.create) ----------

    @staticmethod
    def create():
        c = 0
        ch = 'y'
        while ch == 'y':
            c += 1
            dta = int(input(f"Enter key {c}: "))
            BPlusTree.insert(dta)
            ch = input("To insert new key press y: ")

    # ---------- DISPLAY ----------

    @staticmethod
    def display(node=None, level=0):
        if node is None:
            node = BPlusTree.root
        if node is None:
            print("Tree is empty")
            return

        tag = "LEAF" if node.leaf else "INTR"
        print(f"Level {level} [{tag}]:", node.keys)
        if not node.leaf:
            for c in node.child:
                BPlusTree.display(c, level + 1)

    @staticmethod
    def display_leaves():
        # walk the linked list across the bottom row - shows all data in sorted order
        node = BPlusTree.root
        if node is None:
            print("Tree is empty")
            return
        while not node.leaf:
            node = node.child[0]

        print("Leaf chain:", end=" ")
        while node is not None:
            print(node.keys, end=" -> ")
            node = node.next
        print("None")


if __name__ == "__main__":
    BPlusTree.create()
    print("\nB+ Tree structure (level by level):")
    BPlusTree.display()
    print()
    BPlusTree.display_leaves()