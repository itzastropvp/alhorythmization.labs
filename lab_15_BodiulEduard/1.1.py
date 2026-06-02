from unicodedata import digit
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        return f"ASDAD"
    def get_info(self):
        return f"{self.name} - {self.species}"
class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    def make_sound(self):
        return f"Гав!"
dog = Dog("Рекс", "Собака домашній")
print(dog.get_info())
print(dog.make_sound())