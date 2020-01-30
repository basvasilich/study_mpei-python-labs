import math


class Triangle:
    def __init__(self):
        self.sides = [0, 0, 0]
        while not self.check():
            self.sides = self.input()

    @staticmethod
    def input() -> list:
        t_str = input('Input sides of triangle (1,2,3): ')
        return list(map(lambda i: float(i), t_str.split(',')))

    def check(self) -> bool:
        a, b, c = self.sides
        return a < b + c or b < a + c or c < a + b

    def get_perimeter(self) -> float:
        return sum(self.sides)

    def get_area(self) -> float:
        a, b, c = self.sides
        p = self.get_perimeter() * 0.5
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


triangle1 = Triangle()
triangle2 = Triangle()

if triangle1.get_perimeter() > triangle2.get_perimeter():
    print("Perimeter and area of triangle 1 > triangle 2")
elif triangle2.get_perimeter() > triangle1.get_perimeter():
    print("Perimeter and area of triangle 2 > triangle 1")
else:
    print("Perimeter and area of triangle 1 = triangle 2")
