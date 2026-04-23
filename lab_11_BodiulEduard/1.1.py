import random
import string
a = 0
for i in range(5):
    passwd = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    a+=1
    print(f"{a}. {passwd}")