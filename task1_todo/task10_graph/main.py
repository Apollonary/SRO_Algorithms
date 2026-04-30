graph = {
    "Иван": ["Петр", "Анна"],
    "Петр": ["Иван"],
    "Анна": ["Иван"]
}

for user in graph:
    print(user, "->", graph[user])
