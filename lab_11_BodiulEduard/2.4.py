import os
FILE_NAME = "passwords.txt"
SHIFT = 2
def encrypt(text):
    result = ""
    for ch in text:
        result += chr(ord(ch) + SHIFT)
    return result
def decrypt(text):
    result = ""
    for ch in text:
        result += chr(ord(ch) - SHIFT)
    return result
def load_data():
    data = {}
    if not os.path.exists(FILE_NAME):
        return data
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if ":" not in line:
                    raise ValueError("Невірний формат рядка")

                site, enc_pass = line.split(":", 1)
                data[site] = enc_pass
    except FileNotFoundError:
        print("Файл не знайдено, створюється новий...")
    except PermissionError:
        print("Немає доступу до файлу!")
    except ValueError as e:
        print("Помилка формату даних:", e)
    return data
def save_data(data):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for site, enc_pass in data.items():
                f.write(f"{site}:{enc_pass}\n")
    except PermissionError:
        print("Помилка: немає доступу для запису!")
def add_record(site, password):
    data = load_data()
    data[site] = encrypt(password)
    save_data(data)
    print(f"Додано запис для {site}")
def find_password(site):
    data = load_data()
    try:
        enc_pass = data[site]
        print(f"Пароль для {site}: {decrypt(enc_pass)}")
    except KeyError:
        print("Запис не знайдено!")
def delete_record(site):
    data = load_data()
    try:
        del data[site]
        save_data(data)
        print(f"Запис для {site} видалено")
    except KeyError:
        print("Немає такого запису!")
add_record("google.com", "myPass123")
add_record("github.com", "dev2024")
find_password("google.com")