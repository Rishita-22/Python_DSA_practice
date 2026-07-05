class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * max_size
        self.top = -1

    def push(self, ele):
        if self.top == self.max_size - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = ele
            print(ele, "data inserted")

    def pop(self):
        if self.top == -1:
            print("No element or Underflow")
        else:
            print("Deleted element =", self.stack[self.top])
            self.top -= 1

    def peek(self):
        if self.top == -1:
            print("No element or Underflow")
        else:
            print("Top element =", self.stack[self.top])

    def disp(self):
        if self.top == -1:
            print("No element or Underflow")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i])


if __name__ == "__main__":
    size = int(input("Enter stack size: "))
    s = Stack(size)

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
