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
    def second_largest_element():
        if SL.head is None:
            print("No elements")
            return

        if SL.head.next is None:
            print("Not enough elements")
            return

        big = float('-inf')
        s_big = float('-inf')
        ptr = SL.head

        while ptr is not None:
            if ptr.data > big:
                s_big = big
                big = ptr.data
            if s_big < ptr.data and big >ptr.data :
                s_big = ptr.data

            ptr = ptr.next

        print("Largest element = ", big)
        print("Second largest element = ", s_big)

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
    SL.second_largest_element()
