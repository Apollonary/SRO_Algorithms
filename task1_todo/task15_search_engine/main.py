graph = {
    "page1": ["page2", "page3"],
    "page2": ["page4"],
    "page3": [],
    "page4": []
}

def search(start, target):
    visited = set()

    def dfs(node):
        if node == target:
            return True
        visited.add(node)
        for n in graph[node]:
            if n not in visited:
                if dfs(n):
                    return True
        return False

    return dfs(start)

print(search("page1", "page4"))
