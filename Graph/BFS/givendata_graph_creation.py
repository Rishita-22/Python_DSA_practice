from collections import deque

graph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2],
    4: [2]
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

bfs(graph, 1)