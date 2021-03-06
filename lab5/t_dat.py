from typing import Dict, Callable, Optional

FxType = Callable[[int], float]


class TDat:
    _points: Dict[int, float]
    _x_min: Optional[int]
    _x_max: Optional[int]

    def __init__(self, x_min: int = None, x_max: int = None):
        self.points = {}
        self._x_min = x_min
        self._x_max = x_max

    @property
    def points(self) -> Dict[int, float]:
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    @property
    def max(self) -> int:
        return self._x_max or max(self._points.keys(), default=0)

    @max.setter
    def max(self, value: int):
        self._x_max = value

    @property
    def min(self) -> int:
        return self._x_min or min(self._points.keys(), default=0)

    @min.setter
    def min(self, value: int):
        self._x_min = value

    def append(self, x: int, fx: FxType):
        self._points[x] = fx(x)

    def clear(self):
        self._points.clear()

    def perform(self, x: int) -> float:
        return self._points.get(x) or .0

