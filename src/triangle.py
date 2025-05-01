from src.shape import Shape
import math

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if min(a, b, c) <= 0:
            raise ValueError("Стороны должны быть положительными числами")
        if not self._is_valid(a, b, c):
            raise ValueError("Треугольник с такими сторонами не существует")
        
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    @staticmethod
    def _is_valid(a, b, c) -> bool:
        return a + b > c and a + c > b and b + c > a
