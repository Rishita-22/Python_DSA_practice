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
    def even_odd_count():
        if SL.head is None:
            print("No elements in the list")
            return

        even = 0
        odd = 0
        ptr = SL.head

        while ptr is not None:
            if ptr.data % 2 == 0:
                even += 1
            else:
                odd += 1
            ptr = ptr.next

        print(f"Total even elements: {even}")
        print(f"Total odd elements: {odd}")

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
    SL.even_odd_count()
