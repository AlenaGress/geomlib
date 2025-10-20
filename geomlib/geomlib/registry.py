
from __future__ import annotations
from typing import Callable, Dict, Any
from .shapes import Shape, Circle, Triangle

# Реестр «тип -> конструктор»
_REGISTRY: Dict[str, Callable[..., Shape]] = {}

def register_shape(name: str) -> Callable[[Callable[..., Shape]], Callable[..., Shape]]:
    """Декоратор для регистрации новых фигур в фабрике."""
    def deco(ctor: Callable[..., Shape]) -> Callable[..., Shape]:
        _REGISTRY[name.lower()] = ctor
        return ctor
    return deco

# Зарегистрируем базовые фигуры
register_shape("circle")(Circle)
register_shape("triangle")(Triangle)

def make_shape(spec: Dict[str, Any]) -> Shape:
    """
    Универсальная фабрика из словаря/JSON.
    Пример: {"type":"circle","radius":2} или {"type":"triangle","a":3,"b":4,"c":5}
    """
    t = spec.get("type")
    if not t:
        raise ValueError("spec must contain 'type'")
    ctor = _REGISTRY.get(t.lower())
    if not ctor:
        raise ValueError(f"Unknown shape type: {t}")
    kwargs = {k: v for k, v in spec.items() if k != "type"}
    return ctor(**kwargs)  # type: ignore[arg-type]

def area_of(obj: Shape) -> float:
    """Вычислить площадь без знания конкретного класса."""
    return obj.area()

def area_from_spec(spec: Dict[str, Any]) -> float:
    """Удобный хелпер: площадь по JSON-описанию фигуры."""
    return area_of(make_shape(spec))
