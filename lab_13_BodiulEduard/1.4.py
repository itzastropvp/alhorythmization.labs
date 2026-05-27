list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
result = [x for x in set(list1) if x in list2]
print(result)