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
def reverse_no(n):
    stack = Stack()
    
    while (n!=0):
        num = n%10
        stack.push(num)
        n //= 10

    result = 0
    # Pop numbers from stack and multiply
    while not stack.is_empty():
        result = result*10 + stack.pop()

    return result

# Example usage
num = 125
print(f"Reverse of {num} is {reverse_no(num)}")
