import pytest
import math
from src.triangle import Triangle

# Генерация тестовых данных
valid_triangles = [
    (3, 4, 5),      # Прямоугольный
    (2, 2, 3),      # Обычный
    (100, 101, 200) # Тупой (но валидный)
]

invalid_triangles = [
    (0, 1, 2),       # Нулевая сторона
    (-1, 2, 2),      # Отрицательная сторона
    (1, 2, 4),       # Нарушение неравенства
    (1, 1, 2)        # Вырожденный (сумма двух сторон == третьей)
]

class TestTriangle:
    @pytest.mark.parametrize("a, b, c", valid_triangles)
    def test_valid_triangles(self, a, b, c):
        triangle = Triangle(a, b, c)
        assert triangle.area() > 0  # Площадь должна быть положительной

    @pytest.mark.parametrize("a, b, c", invalid_triangles)
    def test_invalid_triangles(self, a, b, c):
        with pytest.raises(ValueError):
            Triangle(a, b, c)

    def test_area_calculation(self):
        assert math.isclose(Triangle(3, 4, 5).area(), 6.0)

