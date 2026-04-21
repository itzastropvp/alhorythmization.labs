def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    max_rest = find_max(lst[1:])
    if lst[0] > max_rest:
        return lst[0]
    else:
        return max_rest
print(find_max([3, 4, 5, 6]))