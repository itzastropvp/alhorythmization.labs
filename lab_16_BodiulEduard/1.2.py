class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")
        self.__age = value
person = Person("Іван", 25)
print(person.age)