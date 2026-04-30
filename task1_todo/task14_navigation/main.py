graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

def find_route(start, end):
    if start == end:
        return [start]

    for n in graph[start]:
        path = find_route(n, end)
        if path:
            return [start] + path

    return None

print(find_route("A", "D"))
