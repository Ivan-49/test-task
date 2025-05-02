from abc import ABC, abstractclassmethod


class Shape(ABC):
    @abstractclassmethod
    def area(self) -> float:
        pass
