import datetime
n = input("Користувач вводить: ")
with open("diary.txt", "w", encoding='utf-8') as f:
    f.write(f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {n}")