# given data graph creation using recursion

graph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2],
    4: [2]
}

visited = set()

def dfs(node):
    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour)

dfs(1)



# given data graph creation using stack

graph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2],
    4: [2]
}

visited = set()
stack = [1]

while stack:
    node = stack.pop()

    if node not in visited:
        visited.add(node)
        print(node, end=" ")

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)