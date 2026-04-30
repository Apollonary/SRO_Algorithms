class Node:
    def init(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def init(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# Проверка
ll = LinkedList()
ll.add("A")
ll.add("B")
ll.add("C")

ll.print_list()
