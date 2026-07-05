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
    def separate_even_odd():
        if SL.head is None:
            print("No elements in the list")
            return

        even_head = even_ptr = None
        odd_head = odd_ptr = None

        ptr = SL.head
        while ptr is not None:
            # Create a new node for each element
            new_node = Node(ptr.data)

            # Check even or odd
            if ptr.data % 2 == 0:
                if even_head is None:
                    even_head = new_node
                    even_ptr = new_node
                else:
                    even_ptr.next = new_node
                    even_ptr = new_node
            else:
                if odd_head is None:
                    odd_head = new_node
                    odd_ptr = new_node
                else:
                    odd_ptr.next = new_node
                    odd_ptr = new_node

            ptr = ptr.next

        # Display both lists
        print("\nEven elements linked list:")
        temp = even_head
        if temp is None:
            print("No even elements")
        else:
            while temp is not None:
                print(temp.data)
                temp = temp.next

        print("\nOdd elements linked list:")
        temp = odd_head
        if temp is None:
            print("No odd elements")
        else:
            while temp is not None:
                print(temp.data)
                temp = temp.next

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
    SL.separate_even_odd()
