class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return self.rear == self.max_size - 1

    def is_empty(self):
        return self.front == -1

    def enqueue(self, ele):
        if self.is_full():
            print("Queue Overflow")
            return
        if self.is_empty():
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = ele
        print(ele, "inserted")

    def dequeue(self):
        if self.is_empty():
            print("No element or Underflow")
            return
        print("Deleted element =", self.queue[self.front])
        if self.front == self.rear:  # only one element was present
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

    def peek(self):
        if self.is_empty():
            print("No element or Underflow")
        else:
            print("Front element =", self.queue[self.front])

    def display(self):
        if self.is_empty():
            print("No element or Underflow")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


if __name__ == "__main__":
    size = int(input("Enter queue size: "))
    q = Queue(size)

    while True:
        print("\nEnter your choice\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit")
        try:
            ch = int(input("Choice: "))
        except ValueError:
            print("Enter a valid number")
            continue

        if ch == 1:
            try:
                ele = int(input("Enter element to enqueue: "))
            except ValueError:
                print("Enter a valid integer")
                continue
            q.enqueue(ele)
        elif ch == 2:
            q.dequeue()
        elif ch == 3:
            q.peek()
        elif ch == 4:
            q.display()
        elif ch == 5:
            print("Exiting.")
            break
        else:
            print("Invalid choice")
