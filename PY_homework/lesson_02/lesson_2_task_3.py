import math


def square(a):
    return math.ceil(a * a)


sq_a = int(input("Сторона квадрата: "))

print(f"Площадь квадрата: {square(sq_a)}")
