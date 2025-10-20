
# geomlib

Библиотека на Python для вычисления площадей геометрических фигур. 
Поддерживает круг и треугольник, легко расширяется с помощью реестра типов.

## Возможности
- Площадь круга по радиусу
- Площадь треугольника по трём сторонам (формула Герона)
- Проверка, является ли треугольник прямоугольным
- Единый интерфейс `Shape.area()` — можно вычислять площадь без знания конкретного класса
- Фабрика `make_shape(spec)` и хелпер `area_from_spec(spec)` — удобно создавать фигуры из `dict/JSON`
- Лёгкое добавление новых фигур через `register_shape("name")(Ctor)`

## Установка (локально)
```bash
pip install -e .
```
или
```bash
pip install .
```

## Пример использования
```python
from geomlib import Circle, Triangle, area_of, make_shape, is_right_triangle, area_from_spec

print(area_of(Circle(2)))                 # 12.566...
print(area_of(Triangle(3, 4, 5)))         # 6.0
print(is_right_triangle(3, 4, 5))         # True

spec = {"type": "circle", "radius": 3}
print(area_from_spec(spec))               # 28.274...
```

## Тесты
```bash
pip install -e ".[dev]"
pytest -q
```

## Расширение: новая фигура
```python
from dataclasses import dataclass
from geomlib import register_shape, make_shape, area_of

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
print(area_of(r))  # 10.0
```

## Требования
- Python 3.9+

## Лицензия
MIT
