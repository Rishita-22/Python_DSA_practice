class Node:
    def __init__(self, ele):
        self.data=ele 
        self.next=None

class Queue:
    def __init__(self):
        self.front = None
        self.rear=None

    def enqueue(self, ele):
        cur=Node(ele)
        print(ele, "data inserted")
        if self.front==None:
            self.front=cur
            self.rear=cur
            return
        self.rear.next=cur
        self.rear=cur

    def dequeue(self):
        if self.front == None:
            print("No element or Underflow")
            return
        print("Deleted element =", self.front.data)
        if self.front==self.rear:
            self.front=None
            self.rear=None
            return
        self.front=self.front.next

    def peek(self):
        if self.front == None:
            print("No element or Underflow")
        else:
            print("Top element =", self.front.data)

    def disp(self):
        if self.front == None:
            print("No element or Underflow")
        else:
            temp=self.front
            while temp!=None:
                print(temp.data)
                temp=temp.next


if __name__ == "__main__":
    q = Queue()

    while True:
        print("\nEnter your choice\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit")
        ch = int(input())
        if ch == 1:
            ele = int(input("Enter element to push: "))
            q.enqueue(ele)
        elif ch == 2:
            q.dequeue()
        elif ch == 3:
            q.peek()
        elif ch == 4:
            q.disp()
        elif ch == 5:
            exit(0)
        else:
            print("Invalid choice")
