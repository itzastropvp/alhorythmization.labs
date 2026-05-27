from collections import namedtuple
Student = namedtuple("Student", ["first_name", "last_name", "group", "average_mark"])
def get_best_student(students):
    if not students:
        return None
    best = max(students, key=lambda s: s.average_mark)
    return f"{best.last_name} {best.first_name[0]}."
students = [
    Student("Іван", "Петренко", "КН-101", 4.5),
    Student("Марія", "Сидоренко", "КН-101", 4.8),
    Student("Петро", "Іваненко", "КН-102", 4.5)
]
print(get_best_student(students))