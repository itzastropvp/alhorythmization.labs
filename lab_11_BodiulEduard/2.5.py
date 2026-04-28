def read_numbers(filename):
    numbers = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    numbers.append(int(line))
                except ValueError:
                    print(f"Невірне число у файлі {filename}: {line}")
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено!")
    except PermissionError:
        print(f"Немає доступу до файлу {filename}!")
    return numbers
def write_numbers(filename, numbers):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for num in numbers:
                f.write(f"{num}\n")
    except PermissionError:
        print(f"Помилка запису у файл {filename}!")
def merge():
    file1_numbers = read_numbers("file1.txt")
    file2_numbers = read_numbers("file2.txt")
    all_numbers = file1_numbers + file2_numbers
    unique_sorted = sorted(set(all_numbers))
    write_numbers("merged.txt", unique_sorted)
merge()