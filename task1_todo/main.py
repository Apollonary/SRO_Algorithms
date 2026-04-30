tasks = []

while True:
    print("\n1. Добавить\n2. Удалить\n3. Показать\n4. Выход")
    choice = input("Выбор: ")

    if choice == "1":
        task = input("Введите задачу: ")
        tasks.append(task)

    elif choice == "2":
        task = input("Что удалить: ")
        if task in tasks:
            tasks.remove(task)

    elif choice == "3":
        print(tasks)

    elif choice == "4":
        break
