
from __future__ import annotations

def is_right_triangle(a: float, b: float, c: float, *, rel_tol: float = 1e-9) -> bool:
    """
    Проверка прямоугольности по теореме Пифагора с учётом численной погрешности.
    Не валидирует стороны (валидность — в Triangle.__post_init__). 
    """
    sides = sorted((a, b, c))
    x, y, z = sides
    return abs(x*x + y*y - z*z) <= rel_tol * max(1.0, x*x + y*y, z*z)
