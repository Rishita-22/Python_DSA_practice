# Global variables
front = -1
rear = -1
queue = []
max_size = 0

def enqueue(ele):
    global front, rear, queue, max_size
    if rear == max_size - 1:
        print("Queue Overflow")
        return
    if front == -1:   # first element being inserted
        front = 0
    rear += 1
    queue[rear] = ele
    print(ele, "data inserted")


def dequeue():
    global front, rear, queue
    if front == -1:
        print("No element or Underflow")
        return
    print("Deleted element =", queue[front])
    if rear == front:  # removed last element -> reset queue
        front = -1
        rear = -1
    else:
        front += 1


def peek():
    global front, queue
    if front == -1:
        print("No element or Underflow")
    else:
        print("Front element =", queue[front])


def disp():
    global front, rear, queue
    if front == -1:
        print("No element or Underflow")
        return
    # print elements from front to rear (left-to-right)
    for i in range(front, rear + 1):
        print(queue[i], end=" ")
    print()


if __name__ == "__main__":
    # initialize
    while True:
        try:
            max_size = int(input("Enter queue size: "))
            if max_size <= 0:
                print("Size must be positive.")
                continue
            break
        except ValueError:
            print("Enter a valid integer for size.")

    queue = [None] * max_size
    front = -1
    rear = -1

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
            enqueue(ele)
        elif ch == 2:
            dequeue()
        elif ch == 3:
            peek()
        elif ch == 4:
            disp()
        elif ch == 5:
            print("Exiting.")
            break
        else:
            print("Invalid choice")
