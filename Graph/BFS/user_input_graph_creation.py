from collections import deque

# Number of vertices and edges
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

# Create adjacency list
graph = {i: [] for i in range(1, n + 1)}

# Take edges as input
for i in range(e):
    u, v = map(int, input("Enter edge: ").split())

    graph[u].append(v)
    graph[v].append(u)   # For undirected graph

# Starting vertex
start = int(input("Enter starting vertex: "))

# BFS
visited = set()
queue = deque([start])
visited.add(start)

print("BFS Traversal:", end=" ")

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)