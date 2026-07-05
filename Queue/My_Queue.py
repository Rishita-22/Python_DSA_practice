def enqueue(queue, rear, max_size, ele):
    global front 
    if rear == max_size - 1:
        print("Queue Overflow")
    else:
        if front == -1:
            front = 0
        rear += 1
        queue[rear] = ele
        print(ele, "data inserted")
    return rear

def dequeue(queue, front):
    global rear 
    if front == -1:
        print("No element or Underflow")
    else:
        print("Deleted element =", queue[front])
        if rear == front:
            rear = -1
            front = -1
            return front
        front += 1
    return front

def peek(queue, front):
    if front == -1:
        print("No element or Underflow")
    else:
        print("Front element =", queue[front])

def disp(queue, front):
    global rear
    if front == -1:
        print("No element or Underflow")
    else:
        for i in range(front, rear+1, 1):
            print(queue[i])


if __name__ == "__main__":
    size = int(input("Enter queue size: "))
    queue = [None] * size
    front = -1
    rear = -1
        
    

    while True:
        print("\nEnter your choice\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit")
        ch = int(input())
        if ch == 1:
            ele = int(input("Enter element to push: "))
            rear = enqueue(queue, rear, size, ele)
        elif ch == 2:
            front = dequeue(queue, front)
        elif ch == 3:
            peek(queue, front)
        elif ch == 4:
            disp(queue, front)
        elif ch == 5:
            exit(0)
        else:
            print("Invalid choice")