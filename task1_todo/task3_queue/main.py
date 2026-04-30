queue = []

while True:
    print("\n1. Добавить клиента\n2. Обслужить клиента\n3. Показать очередь\n4. Выход")
    choice = input("Выбор: ")

    if choice == "1":
        name = input("Имя клиента: ")
        queue.append(name)

    elif choice == "2":
        if queue:
            print("Обслужен:", queue.pop(0))
        else:
            print("Очередь пуста")

    elif choice == "3":
        print("Очередь:", queue)

    elif choice == "4":
        break
