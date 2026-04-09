import random
import string


def generate_password(length):
    letters = string.ascii_letters
    password = "".join(random.choice(letters) for i in range(length))
    print(password)
generate_password(5)