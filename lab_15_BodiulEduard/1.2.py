class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
class Extend_Student(Student):
    def __init__(self, name, student_id, major):
        super().__init__(name, student_id)
        self.major = major
    def display_method(self):
        return f"Студент: {self.name}, ID: {self.student_id}, Спеціальність: {self.major}"
s = Extend_Student("Олена Петренко", "S12345", "Комп'ютерні науки")
print(s.display_method())