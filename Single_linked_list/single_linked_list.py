class Node:
    def __init__(self, data):
        self.data = data   # store value
        self.next = None   # link to next node

def main():
    head = None
    ptr = None
    c = 0
    ch = 'y'

    while ch == 'y':
        c += 1
        data = int(input(f"Enter node {c} data: "))
        cur = Node(data)

        if head is None:       # if list is empty
            head = cur         # first node becomes head
        else:
            ptr.next = cur     # link previous node to new one

        ptr = cur              # move tail pointer to new node
        ch = input("To create new node press y: ")

    print("Elements are: ")
    ptr = head
    while ptr is not None:     # traverse and print
        print(ptr.data)
        ptr = ptr.next

if __name__ == "__main__":
    main()













