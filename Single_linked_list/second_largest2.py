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
            data = int(input(f"Enter node {c} data: "))
            cur = Node(data)

            if SL.head is None:
                SL.head = cur
            else:
                ptr.next = cur

            ptr = cur
            ch = input("To create new node press y: ")

    @staticmethod
    def secd_largest():
        if SL.head is None:
            print("NO ELEMENT")
            return
        if SL.head.next is None:
            print("NOT ENOUGH ELEMENTS")
            return

        big = float('-inf')
        secd_big = float('-inf')

        ptr = SL.head
        while ptr is not None:
            if ptr.data > big:
                secd_big = big
                big = ptr.data
            elif ptr.data > secd_big and ptr.data != big:
                secd_big = ptr.data
            ptr = ptr.next

        if secd_big == float('-inf'):
            print("All elements are equal → No 2nd largest")
        else:
            print("Second largest element =", secd_big)

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
    SL.secd_largest()