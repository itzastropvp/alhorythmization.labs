class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        return f"Книга: {self.title}, Автор: {self.author}"
b = Book("1984", "Джордж Орвелл")
print(b.get_info())