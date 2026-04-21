try:
    area = lambda x,y: x*y
    print(area(3, 5))
except TypeError:
    print("Помилка (підказка: функція має приймати два аргументи)")