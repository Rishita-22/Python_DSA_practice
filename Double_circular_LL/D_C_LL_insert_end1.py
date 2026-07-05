class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SL:
    head = None  # static-like variable (same for all methods)

    @staticmethod
    def create():
        c = 0
        ch = 'y'
        ptr = None

        while ch == 'y':
            c += 1
            data = int(input(f"Enter node{c} data: "))
            cur = Node(data)
            cur.next = cur
            cur.prev = cur
            if SL.head is None:
                SL.head = cur
            else:
                cur.prev = ptr
                ptr.next = cur
                cur.next = SL.head
                SL.head.prev = cur
            ptr = cur
            ch = input("To create new node press y: ")

    @staticmethod
    def insert_end():
        data = int(input("Enter data to insert at end: "))
        cur = Node(data)

        if SL.head is None:
            cur.next = cur
            cur.prev = cur
            SL.head = cur
            return

        SL.head.prev.next = cur
        cur.prev = SL.head.prev
        cur.next = SL.head
        SL.head.prev = cur

    @staticmethod
    def dispf():
        print("Elements are:")

        if SL.head is None:
            print("List is empty")

        ptr = SL.head
        while ptr.next is not SL.head:
            print(ptr.data)
            ptr = ptr.next
        print(ptr.data)
    @staticmethod
    def dispb():
        print("Elements are:")

        if SL.head is None:
            print("List is empty")

        ptr = SL.head
        while ptr.next is not SL.head:
            print(ptr.data)
            ptr = ptr.next
        print(ptr.data)


# main equivalent
if __name__ == "__main__":
    SL.create()
    SL.dispf()
    SL.dispb()

    SL.insert_end()
    SL.dispf()
    SL.dispb()
