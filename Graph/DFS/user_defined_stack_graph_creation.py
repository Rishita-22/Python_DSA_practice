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


# Graph creation using adjacency list
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = {i: [] for i in range(1, n + 1)}

for i in range(e):
    u, v = map(int, input("Enter edge: ").split())

    graph[u].append(v)
    graph[v].append(u)


# Starting vertex
start = int(input("Enter starting vertex: "))

# DFS
visited = set()
stack = Stack()

stack.push(start)

print("DFS Traversal:", end=" ")

while not stack.is_empty():

    node = stack.pop()

    if node not in visited:
        visited.add(node)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.push(neighbour)