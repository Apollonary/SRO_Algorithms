from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])

bfs("A")
