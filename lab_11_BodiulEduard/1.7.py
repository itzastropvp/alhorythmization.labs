with open("numbers.txt", "r", encoding="utf-8") as f:
    numbers = f.readlines()
suma = 0
for i in numbers:
    suma+=int(i)
print(f"Сума чисел: {suma}")