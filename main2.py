# N1
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self, other):
        return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


a = Point(int(input("type x coordinate: ")), int(input("type y coordinate:  ")))
b = Point(int(input("type x1 coordinate: ")), int(input("type y1 coordinate:  ")))
print(a)
print(b)
print(a + b)


# N2
def staircase(n):
    if n < 2:
        return 1
    else:
        return staircase(n - 1) + staircase(n - 2)


stairs = 10
print(staircase(stairs))
# N3
def roman_to_integer(s: str):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    return res


print(roman_to_integer("MMLIV"))
# N4
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if other is int(other):
            return Vector(other * self.x, other * self.y)
        else:
            return "error"

    def __rmul__(self, other):
        if other is int(other):
            return Vector(self.x * other, self.y)
        else:
            return "error"


v1 = Vector(2, 4)
v2 = Vector(5, 7)
print(v1.__add__(v2))
print(v1 + v2)
print(v1.__mul__(3))
print(v1 * 3)
print(v1.__rmul__(4))
