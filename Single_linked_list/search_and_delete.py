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
    def search_element(ele):
        if SL.head is None:  
            print("no element")
            return
        ptr = SL.head
        while ptr is not None:
            if ptr.data == ele:
                break
            ptr = ptr.next

        if ptr is None:
            print("No element is found")
        else:
            print("Element found")
        
     @staticmethod
    def delete_element(ele):
        if SL.head is None:
            print("List is empty, nothing to delete")
            return

        # If head node is the element to delete
        if SL.head.data == ele:
            SL.head = SL.head.next
            print(f"Element {ele} deleted")
            return

        ptr = SL.head
        while ptr.next is not None and ptr.next.data != ele:
            ptr = ptr.next

        if ptr.next is None:
            print(f"Element {ele} not found")
        else:
            ptr.next = ptr.next.next
            print(f"Element {ele} deleted")


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

    SL.search_element(4)
    
