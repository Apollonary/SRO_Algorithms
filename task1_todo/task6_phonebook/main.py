class Contact:
    def init(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None


class PhoneBook:
    def init(self):
        self.head = None

    def add(self, name, phone):
        new = Contact(name, phone)
        new.next = self.head
        self.head = new

    def find(self, name):
        current = self.head
        while current:
            if current.name == name:
                print(current.name, current.phone)
                return
            current = current.next
        print("Не найдено")

    def delete(self, name):
        current = self.head
        prev = None

        while current:
            if current.name == name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next


# Проверка
pb = PhoneBook()
pb.add("Иван", "123")
pb.add("Петр", "456")

pb.find("Иван")
pb.delete("Иван")
pb.find("Иван")
