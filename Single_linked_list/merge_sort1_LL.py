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
        SL.display_list(self.head)

    @staticmethod
    def append_test(Chead, data):
        if Chead is None:
            Chead = Node(data)
            return Chead
        temp = Chead
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)
        return Chead

    @staticmethod
    def display_list(head):
        print("Elements are:")
        ptr = head
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

    ptr1 = A.head
    ptr2 = B.head
    Chead = None

    while ptr1 is not None and ptr2 is not None:
        if ptr1.data < ptr2.data:
            Chead = SL.append_test(Chead, ptr1.data)
            ptr1 = ptr1.next
        else:
            Chead = SL.append_test(Chead, ptr2.data)
            ptr2 = ptr2.next

    while ptr1 is not None:
        Chead = SL.append_test(Chead, ptr1.data)
        ptr1 = ptr1.next

    while ptr2 is not None:
        Chead = SL.append_test(Chead, ptr2.data)
        ptr2 = ptr2.next

    return Chead


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

    print("\nMerged list:")
    merged_head = merge(list1, list2)
    SL.display_list(merged_head)
