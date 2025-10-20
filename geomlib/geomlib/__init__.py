
from .shapes import Circle, Triangle, Shape
from .registry import register_shape, make_shape, area_of, area_from_spec
from .utils import is_right_triangle

__all__ = [
    "Shape", "Circle", "Triangle",
    "register_shape", "make_shape", "area_of", "area_from_spec",
    "is_right_triangle",
]
