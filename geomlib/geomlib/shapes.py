
from __future__ import annotations
from dataclasses import dataclass
from math import pi, sqrt
from typing import Protocol

class Shape(Protocol):
    """Протокол для фигуры с площадью — позволяет вычислять площадь без знания конкретного типа."""
    def area(self) -> float: ...

@dataclass(frozen=True)
class Circle:
    radius: float

    def __post_init__(self):
        if self.radius <= 0:
            raise ValueError("Radius must be positive")

    def area(self) -> float:
        return pi * self.radius * self.radius

@dataclass(frozen=True)
class Triangle:
    a: float
    b: float
    c: float

    def __post_init__(self):
        sides = sorted((self.a, self.b, self.c))
        if any(s <= 0 for s in sides):
            raise ValueError("Sides must be positive")
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Triangle inequality violated")

    def area(self) -> float:
        # Формула Герона
        p = (self.a + self.b + self.c) / 2.0
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right(self, *, rel_tol: float = 1e-9) -> bool:
        from .utils import is_right_triangle
        return is_right_triangle(self.a, self.b, self.c, rel_tol=rel_tol)
