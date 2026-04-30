class Node:
    def init(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def init(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add(node.right, value)

    def print_tree(self, node):
        if node:
            self.print_tree(node.left)
            print(node.value)
            self.print_tree(node.right)


# Проверка
tree = BinaryTree()
tree.add(5)
tree.add(3)
tree.add(7)
tree.add(1)

tree.print_tree(tree.root)
