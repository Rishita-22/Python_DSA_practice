class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SL:
    def __init__(self):
        self.head = None   

    def create(self):
        c = 0
        ch = 'y'
        ptr = None

        while ch.lower() == 'y':
            c += 1
            data = int(input(f"Enter node {c} data: "))
            cur = Node(data)

            if self.head is None:
                self.head = cur
            else:
                ptr.next = cur

            ptr = cur
            ch = input("To create new node press y: ")

    def disp(self):
        print("Elements are:")
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end=" -> ")
            ptr = ptr.next
        print("None")


def merge(A, B):
    
    if A.head is None and B.head is None:
        print("Both lists are empty")
        return None

    if A.head is None:
        return B.head

    if B.head is None:
        return A.head

    temp = A.head
    while temp.next is not None:
        temp = temp.next

    temp.next = B.head
    return A.head



if __name__ == "__main__":
    print("Create first linked list:")
    list1 = SL()
    list1.create()

    print("\nCreate second linked list:")
    list2 = SL()
    list2.create()

    print("\nList 1:")
    list1.disp()

    print("\nList 2:")
    list2.disp()

    
    merged_head = merge(list1, list2)
    print("\nMerged List:")

    
    ptr = merged_head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    print("None")
