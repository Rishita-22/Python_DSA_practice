# User-defined Stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


# Graph
graph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4: [2, 3]
}

visited = set()
stack = Stack()

# Start from 1
stack.push(1)

print("DFS Traversal:", end=" ")

while not stack.is_empty():

    node = stack.pop()

    if node not in visited:

        visited.add(node)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.push(neighbour)