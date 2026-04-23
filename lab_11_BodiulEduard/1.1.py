import random
import string

for i in range(5):
    passwd = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    print(passwd)