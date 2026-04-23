with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
maxx = 0
a = ""
for word in text:
    word = word.replace('\n', '')
    word = word.replace('.', '')
    word = word.split()
    for char in word:
        if len(char) > maxx:
            maxx = len(char)
            a = char
print(f"Найдовше слово: '{a}' ({maxx} символів)")