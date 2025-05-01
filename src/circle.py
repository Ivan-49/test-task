from src.shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius:float):
        if radius <= 0: 
            raise ValueError('Радиус должнен быть пололжительным')
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius**2)