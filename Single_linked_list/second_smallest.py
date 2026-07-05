class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SL:
    head = None  

    @staticmethod
    def create():
        c = 0
        ch = 'y'
        ptr = None

        while ch == 'y':
            c += 1
            dta = int(input(f"Enter node {c} data: "))
            cur = Node(dta)

            if SL.head is None:
                SL.head = cur
            else:
                ptr.next = cur

            ptr = cur
            ch = input("To create new node press y: ")

    @staticmethod
    def second_smallest_element():
        if SL.head is None:
            print("No elements")
            return

        if SL.head.next is None:
            print("Not enough elements")
            return

        small = float('inf')
        s_small = float('inf')
        ptr = SL.head

        while ptr is not None:
            if ptr.data < small:
                s_small = small
                small = ptr.data
            if ptr.data > small and ptr.data < s_small:
                s_small = ptr.data

            ptr = ptr.next

        print("Smallest element = ", small)
        print("Second smallest element = ", s_small)

    @staticmethod
    def disp():
            if SL.head is None:
                print("List is empty")
                return
            print("Elements are:")
            ptr = SL.head
            while ptr is not None:
                print(ptr.data)
                ptr = ptr.next


if __name__ == "__main__":
    SL.create()
    SL.disp()
    SL.second_smallest_element()
