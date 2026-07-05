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
    def delete_end():
        if SL.head is None:  
            print("no element")
            return

        if SL.head.next is None:  
            print("delete element =", SL.head.data)
            SL.head = None
            return

        
        ptr = SL.head
        while ptr.next.next is not None:
            ptr = ptr.next

        print("delete element =", ptr.next.data)
        ptr.next = None

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

    SL.delete_end()
    SL.disp()
