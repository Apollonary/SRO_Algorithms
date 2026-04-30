stack = []

expression = input("Введите выражение: ")

for char in expression:
    if char.isdigit():
        stack.append(int(char))
    else:
        b = stack.pop()
        a = stack.pop()

        if char == "+":
            stack.append(a + b)
        elif char == "*":
            stack.append(a * b)

print("Результат:", stack[0])
