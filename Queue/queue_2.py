# Global variables
front = -1
rear = -1
queue = []
max_size = 0

def enqueue(ele):
    global front, rear, queue, max_size
    if rear == max_size - 1:
        print("Queue Overflow")
    else:
        if front == -1:   # inserting first element
            front = 0
        rear += 1
        queue[rear] = ele
        print(ele, "inserted")


def dequeue():
    global front, rear, queue
    if front == -1:
        print("No element or Underflow")
    else:
        print("Deleted element =", queue[front])
        if rear == front:  # last element being removed
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
    else:
        for i in range(front, rear + 1):
            print(queue[i], end=" ")
        print()


# ---------- main ----------
if __name__ == "__main__":
    max_size = int(input("Enter queue size: "))
    queue = [None] * max_size   # allocate fixed-size list

    while True:
        print("\nEnter your choice\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit")
        ch = int(input("Choice: "))

        if ch == 1:
            ele = int(input("Enter element to enqueue: "))
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
