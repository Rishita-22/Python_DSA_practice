# Stack implementation using a list
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Function to calculate factorial using stack
def factorial(n):
    stack = Stack()
    # Push all numbers from n down to 1 into the stack
    for i in range(n, 0, -1):
        stack.push(i)

    result = 1
    # Pop numbers from stack and multiply
    while not stack.is_empty():
        result *= stack.pop()

    return result

# Example usage
num = 5
print(f"Factorial of {num} is {factorial(num)}")
