class Node:
    def init(self, value):
        self.value = value
        self.left = None
        self.right = None


def search(node, value):
    if node is None:
        return False
    if node.value == value:
        return True
    elif value < node.value:
        return search(node.left, value)
    else:
        return search(node.right, value)


# Проверка
root = Node(5)
root.left = Node(3)
root.right = Node(7)

print(search(root, 7))
print(search(root, 10))
