class PasswordManager:
    def __init__(self, password):
        self.__password = password
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, new_password):
        if len(new_password) < 8 or not any(char.isdigit() for char in new_password):
            raise ValueError("Пароль має містити принаймні 8 символів та хоча б одну цифру")
        else:
            self.__password = new_password
            print(new_password)
pm = PasswordManager(password="")
pm.password = "qwerty"