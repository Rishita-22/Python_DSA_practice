# User-defined Queue

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0


# Number of vertices and edges
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

# Create adjacency list
graph = {i: [] for i in range(1, n + 1)}

# Input edges
for i in range(e):
    u, v = map(int, input("Enter edge: ").split())

    graph[u].append(v)
    graph[v].append(u)


# Starting vertex
start = int(input("Enter starting vertex: "))

# BFS
visited = set()
q = Queue()

q.enqueue(start)
visited.add(start)

print("BFS Traversal:", end=" ")

while not q.is_empty():

    node = q.dequeue()
    print(node, end=" ")

    for neighbour in graph[node]:

        if neighbour not in visited:
            visited.add(neighbour)
            q.enqueue(neighbour)