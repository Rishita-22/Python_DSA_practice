def push(stack, top, max_size, ele):
    if top == max_size - 1:
        print("Stack Overflow")
    else:
        top += 1
        stack[top] = ele
        print(ele, "data inserted")
    return top

def pop(stack, top):
    if top == -1:
        print("No element or Underflow")
    else:
        print("Deleted element =", stack[top])
        top -= 1
    return top

def peek(stack, top):
    if top == -1:
        print("No element or Underflow")
    else:
        print("Top element =", stack[top])

def disp(stack, top):
    if top == -1:
        print("No element or Underflow")
    else:
        for i in range(top, -1, -1):
            print(stack[i])


if __name__ == "__main__":
    size = int(input("Enter stack size: "))
    stack = [None] * size
    top = -1

    while True:
        print("\nEnter your choice\n1.Push\n2.Pop\n3.Peek\n4.Display\n5.Exit")
        ch = int(input())
        if ch == 1:
            ele = int(input("Enter element to push: "))
            top = push(stack, top, size, ele)
        elif ch == 2:
            top = pop(stack, top)
        elif ch == 3:
            peek(stack, top)
        elif ch == 4:
            disp(stack, top)
        elif ch == 5:
            exit(0)
        else:
            print("Invalid choice")