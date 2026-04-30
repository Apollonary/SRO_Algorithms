from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

def shortest_path(start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node == end:
            return path

        if node not in visited:
            visited.add(node)
            for n in graph[node]:
                queue.append((n, path + [n]))

    return None

print(shortest_path("A", "D"))
