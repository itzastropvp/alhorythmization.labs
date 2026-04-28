import datetime
from calculator import Calculator
with open("history.txt", "a", encoding="utf-8") as f:
    f.write(f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | {Calculator.add(5, 3)}\n")
    f.write(f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | {Calculator.multiply(4, 2)}\n")
    f.write(f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | {Calculator.divide(10, 2)}\n")