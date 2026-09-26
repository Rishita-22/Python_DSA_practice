# user input data graph creation using recursion

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

# Create adjacency list
graph = {i: [] for i in range(1, n + 1)}

# Input edges
for i in range(e):
    u, v = map(int, input("Enter edge: ").split())

    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

visited = set()

def dfs(node):
    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour)

dfs(start)


# user input data graph creation using stack

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = {i: [] for i in range(1, n + 1)}

for i in range(e):
    u, v = map(int, input("Enter edge: ").split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

visited = set()
stack = [start]

while stack:
    node = stack.pop()

    if node not in visited:
        visited.add(node)
        print(node, end=" ")

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)