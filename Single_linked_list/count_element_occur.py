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
    def element_occurance(ele):
        if SL.head is None:  
            print("no element")
            return
        ptr = SL.head
        count = 0 ;
        while ptr is not None:
            if ptr.data == ele:
                count += 1
            ptr = ptr.next

        if count == 0:      
            print("No element is found")
        else:
            print(f"Element found {count} times(s)")
        
        

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

    SL.element_occurance(4)
    
