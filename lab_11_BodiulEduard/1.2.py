import math
def circle(radius):
    plosha = math.pi * radius**2
    length = 2 * math.pi * radius
    plosha = round(plosha, 2)
    length = round(length, 2)
    return (plosha, length)
print(circle(5))