
import math
import pytest
from geomlib import Circle, Triangle, area_of, make_shape, is_right_triangle, register_shape, Shape, area_from_spec

def test_circle_area():
    c = Circle(2)
    assert math.isclose(c.area(), math.pi * 4, rel_tol=1e-12)

def test_circle_bad_radius():
    with pytest.raises(ValueError):
        Circle(0)

def test_triangle_area_345():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0, rel_tol=1e-12)

def test_triangle_inequality():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)  # вырожденный

def test_right_triangle_check():
    assert is_right_triangle(3, 4, 5) is True
    assert is_right_triangle(2, 3, 4) is False
    assert Triangle(3,4,5).is_right() is True

def test_area_of_protocol():
    shapes: list[Shape] = [Circle(1), Triangle(3, 4, 5)]
    areas = [area_of(s) for s in shapes]
    assert math.isclose(areas[0], math.pi, rel_tol=1e-12)
    assert math.isclose(areas[1], 6.0, rel_tol=1e-12)

def test_factory_circle():
    s = make_shape({"type": "circle", "radius": 3})
    assert math.isclose(area_of(s), math.pi * 9, rel_tol=1e-12)

def test_factory_triangle():
    s = make_shape({"type": "triangle", "a": 3, "b": 4, "c": 5})
    assert math.isclose(area_of(s), 6.0, rel_tol=1e-12)

def test_area_from_spec():
    assert math.isclose(area_from_spec({"type":"circle","radius":1}), math.pi, rel_tol=1e-12)

def test_extend_with_new_shape():
    # Пример лёгкого добавления новой фигуры через реестр
    from dataclasses import dataclass
    @dataclass(frozen=True)
    class Rectangle:
        w: float
        h: float
        def area(self) -> float:
            if self.w <= 0 or self.h <= 0:
                raise ValueError("sides must be positive")
            return self.w * self.h

    register_shape("rectangle")(Rectangle)

    r = make_shape({"type": "rectangle", "w": 2, "h": 5})
    assert math.isclose(area_of(r), 10.0, rel_tol=1e-12)
