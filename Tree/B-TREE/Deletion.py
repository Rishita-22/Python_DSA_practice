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

    # ---------- DELETION ----------

    @staticmethod
    def min_keys():
        # minimum keys a non-root node must always have
        return (BTree.m + 1) // 2 - 1

    @staticmethod
    def delete(key):
        if BTree.root is None:
            print("Tree is empty")
            return

        BTree._delete(BTree.root, key)

        # if root became empty after deletion, shrink the tree by one level
        if len(BTree.root.keys) == 0:
            if not BTree.root.leaf:
                BTree.root = BTree.root.child[0]
            else:
                BTree.root = None

    @staticmethod
    def find_key(node, key):
        # returns index of first key >= given key
        idx = 0
        while idx < len(node.keys) and node.keys[idx] < key:
            idx += 1
        return idx

    @staticmethod
    def _delete(node, key):
        idx = BTree.find_key(node, key)

        # CASE 1: key is present in this node
        if idx < len(node.keys) and node.keys[idx] == key:
            if node.leaf:
                node.keys.pop(idx)              # simply remove it
            else:
                BTree.delete_internal(node, idx)
            return

        # CASE 2: key is not in this node
        if node.leaf:
            print(f"Key {key} not found in tree")
            return

        # key must be in the subtree rooted at child[idx]
        last_child = (idx == len(node.keys))

        # BEFORE descending, make sure that child has more than minimum keys
        if len(node.child[idx].keys) <= BTree.min_keys():
            BTree.fill(node, idx)

        # a merge above may have shifted indices, so re-check
        if last_child and idx > len(node.keys):
            BTree._delete(node.child[idx - 1], key)
        else:
            BTree._delete(node.child[idx], key)

    @staticmethod
    def delete_internal(node, idx):
        # key found inside an internal (non-leaf) node
        key = node.keys[idx]
        min_k = BTree.min_keys()

        if len(node.child[idx].keys) > min_k:
            # left child can spare a key -> replace with predecessor
            pred = BTree.get_predecessor(node, idx)
            node.keys[idx] = pred
            BTree._delete(node.child[idx], pred)

        elif len(node.child[idx + 1].keys) > min_k:
            # right child can spare a key -> replace with successor
            succ = BTree.get_successor(node, idx)
            node.keys[idx] = succ
            BTree._delete(node.child[idx + 1], succ)

        else:
            # neither child can spare a key -> merge them, then delete from merged node
            BTree.merge(node, idx)
            BTree._delete(node.child[idx], key)

    @staticmethod
    def get_predecessor(node, idx):
        # largest key in the left subtree (rightmost leaf)
        cur = node.child[idx]
        while not cur.leaf:
            cur = cur.child[-1]
        return cur.keys[-1]

    @staticmethod
    def get_successor(node, idx):
        # smallest key in the right subtree (leftmost leaf)
        cur = node.child[idx + 1]
        while not cur.leaf:
            cur = cur.child[0]
        return cur.keys[0]

    @staticmethod
    def fill(node, idx):
        # child[idx] has too few keys -> fix it by borrowing or merging
        min_k = BTree.min_keys()

        if idx != 0 and len(node.child[idx - 1].keys) > min_k:
            BTree.borrow_from_prev(node, idx)
        elif idx != len(node.keys) and len(node.child[idx + 1].keys) > min_k:
            BTree.borrow_from_next(node, idx)
        else:
            # no sibling can lend a key -> must merge
            if idx != len(node.keys):
                BTree.merge(node, idx)
            else:
                BTree.merge(node, idx - 1)

    @staticmethod
    def borrow_from_prev(node, idx):
        # pull one key down from parent, push left sibling's last key up
        child = node.child[idx]
        sibling = node.child[idx - 1]

        child.keys.insert(0, node.keys[idx - 1])
        if not child.leaf:
            child.child.insert(0, sibling.child.pop())

        node.keys[idx - 1] = sibling.keys.pop()

    @staticmethod
    def borrow_from_next(node, idx):
        # pull one key down from parent, push right sibling's first key up
        child = node.child[idx]
        sibling = node.child[idx + 1]

        child.keys.append(node.keys[idx])
        if not child.leaf:
            child.child.append(sibling.child.pop(0))

        node.keys[idx] = sibling.keys.pop(0)

    @staticmethod
    def merge(node, idx):
        # merge child[idx], the key between them, and child[idx+1] into one node
        child = node.child[idx]
        sibling = node.child[idx + 1]

        child.keys.append(node.keys[idx])
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.child.extend(sibling.child)

        node.keys.pop(idx)
        node.child.pop(idx + 1)

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

    ch = input("\nDo you want to delete a key? (y/n): ")
    while ch == 'y':
        dta = int(input("Enter key to delete: "))
        BTree.delete(dta)
        print("\nB-Tree structure after deletion:")
        BTree.display()
        ch = input("Delete another key? (y/n): ")