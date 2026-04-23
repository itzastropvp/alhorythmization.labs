with open('poem.txt', 'r', encoding="utf-8") as f:
    poem = f.readlines()
i = 0
for word in poem:
    word = word.strip()
    word = word.split()
    for char in word:
        i += 1
print(f"Рядків: {len(poem)}")
print(f"Слів: {i}")
