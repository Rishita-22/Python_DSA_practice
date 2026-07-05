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
            cur = Node(dta)   # fixed here

            if SL.head is None:
                SL.head = cur
            else:
                ptr.next = cur

            ptr = cur
            ch = input("To create new node press y: ")

    @staticmethod
    def insert_beg():
        dta = int(input("Enter data to insert at beginning: "))
        cur = Node(dta)

        # new node points to the old head
        cur.next = SL.head

        # update head to new node
        SL.head = cur

    @staticmethod
    def disp():
        print("Elements are:")
        ptr = SL.head
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next


# main equivalent
if __name__ == "__main__":
    SL.create()
    SL.disp()

    # Insert at beginning
    SL.insert_beg()
    SL.disp()
