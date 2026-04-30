text = input("Введите текст: ").lower()
words = text.split()

print("Количество слов:", len(words))

unique_words = set(words)

print("Повторяющиеся слова:")
for word in unique_words:
    count = words.count(word)
    if count > 1:
        print(word, "-", count)
