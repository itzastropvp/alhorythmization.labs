def flexible_average(*args):
    numbers = [x for x in args if isinstance(x, (int, float))]
    if len (numbers) == 0:
        return None
    return sum(numbers) / len(numbers)
print(flexible_average(1, 'a', 3))