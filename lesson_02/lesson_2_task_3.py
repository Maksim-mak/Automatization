import math


def square(side):
    area = side * side

    return math.ceil(area)


side_length = 3.4
result = square(side_length)

print(f"Площадь квадрата со стороной {side_length} равна {result}.")
