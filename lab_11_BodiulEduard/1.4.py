import random
first = 0
second = 0
third = 0
fourth = 0
fifth = 0
sixth = 0
for gran in range (0, 1000):
    percent = random.randint(1, 6)
    if percent == 1:
        first += 1
    elif percent == 2:
        second += 1
    elif percent == 3:
        third += 1
    elif percent == 4:
        fourth += 1
    elif percent == 5:
        fifth += 1
    elif percent == 6:
        sixth += 1
print(f"Грань 1: {first/1000*100:.1f}%")
print(f"Грань 2: {second/1000*100:.1f}%")
print(f"Грань 3: {third/1000*100:.1f}%")
print(f"Грань 4: {fourth/1000*100:.1f}%")
print(f"Грань 5: {fifth/1000*100:.1f}%")
print(f"Грань 6: {sixth/1000*100:.1f}%")