

import pytest
import math
from src.circle import Circle

# Фиксированные тест-кейсы
valid_circles = [
    (1, math.pi),       # Базовый случай
    (2, 4 * math.pi),   # Удвоенный радиус
    (0.5, 0.25 * math.pi),  # Дробный радиус
]

invalid_circles = [
    (0, ValueError),    # Нулевой радиус
    (-1, ValueError),   # Отрицательный радиус
    (-0.001, ValueError),  # Микроотрицательное значение
]

class TestCircle:
    @pytest.mark.parametrize("radius, expected_area", valid_circles)
    def test_valid_circles(self, radius, expected_area):
        circle = Circle(radius)
        assert math.isclose(circle.area(), expected_area)

    @pytest.mark.parametrize("radius, exception", invalid_circles)
    def test_invalid_circles(self, radius, exception):
        with pytest.raises(exception):
            Circle(radius)

    def test_area_calculation(self):
        assert math.isclose(Circle(1).area(), math.pi)