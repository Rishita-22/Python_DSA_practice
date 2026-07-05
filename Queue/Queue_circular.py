class CQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = -1
        self.rear = -1
    def enqueue(self, ele):
        if (self.front==0 and self.rear==self.max_size-1) or (self.rear+1==self.front):
            print("CQueue Overflow")
        else:
            if self.front == -1:
                self.front = 0
            if self.rear==self.max_size-1:
                self.rear=0
            else:
                self.rear += 1
            self.queue[self.rear] = ele
            print(ele, "data inserted")
    def dequeue(self):
        if self.front == -1:
            print("No element or Underflow")
        else:
            print("Deleted element =", self.queue[self.front])
            if self.front==self.max_size-1:
                self.front=0
                return
            if self.rear == self.front:
                # queue becomes empty
                self.rear = -1
                self.front = -1
            else:
                self.front += 1

    def peek(self):
        if self.front == -1:
            print("No element or Underflow")
        else:
            print("Front element =", self.queue[self.front])

    def disp(self):
        if self.front == -1:
            print("No element or Underflow")
        else:
            if self.front<=self.rear:
                for i in range(self.front,self.rear+1,1):
                    print(self.queue[i])
            else:
                for i in range(self.front,self.max_size,1):
                    print(self.queue[i])
                for i in range(0,self.rear+1,1):
                    print(self.queue[i])   

if __name__ == "__main__":
    size = int(input("Enter queue size: "))
    q =CQueue(size)

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