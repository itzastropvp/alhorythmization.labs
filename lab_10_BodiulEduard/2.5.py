students = [{'name': 'Anna', 'age': 22, 'avg_grade': 91}, {'name': 'Bob', 'age': 19, 'avg_grade': 78}, {'name': 'Charlie', 'age': 23, 'avg_grade': 88}]
result = list(map(lambda s: s['name'],filter(lambda s: s['age'] > 20 and s['avg_grade'] > 85, students)))
print(result)