class Node:
    def init(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)


def preorder(node):
    if node:
        print(node.value)
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value)


# Проверка
root = Node(5)
root.left = Node(3)
root.right = Node(7)

print("Inorder:")
inorder(root)

print("Preorder:")
preorder(root)

print("Postorder:")
postorder(root)
