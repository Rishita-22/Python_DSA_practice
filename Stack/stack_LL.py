class Node:
    def __init__(self, ele):
        self.data=ele 
        self.next=None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, ele):
        cur=Node(ele)
        cur.next=self.top
        self.top = cur
        print(ele, "data inserted")

    def pop(self):
        if self.top == None:
            print("No element or Underflow")
            return
        print("Deleted element =", self.top.data)
        self.top=self.top.next

    def peek(self):
        if self.top == None:
            print("No element or Underflow")
        else:
            print("Top element =", self.top.data)

    def disp(self):
        if self.top == None:
            print("No element or Underflow")
        else:
            temp=self.top
            while temp!=None:
                print(temp.data)
                temp=temp.next


if __name__ == "__main__":
    s = Stack()

    while True:
        print("\nEnter your choice\n1.Push\n2.Pop\n3.Peek\n4.Display\n5.Exit")
        ch = int(input())
        if ch == 1:
            ele = int(input("Enter element to push: "))
            s.push(ele)
        elif ch == 2:
            s.pop()
        elif ch == 3:
            s.peek()
        elif ch == 4:
            s.disp()
        elif ch == 5:
            exit(0)
        else:
            print("Invalid choice")
