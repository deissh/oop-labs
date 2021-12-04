from typing import Dict, Callable, Optional, Set

from t_dat import TDat, FxType


class TDatFiltered(TDat):
    def __is_not_peek(self, v) -> bool:
        x, y = v
        keys = sorted(self._points.keys())

        left = max(filter(lambda i: i < x, keys), default=0)
        right = min(filter(lambda i: i > x, keys), default=0)

        f_x = self._points[x]
        f_max = self._points[self.max]
        f_min = self._points[self.max]
        f_l = self._points.get(left, f_min)
        f_r = self._points.get(right, f_max)

        k = 100

        if len(keys) > 2 and f_x - f_r > (f_max - f_min) * k and f_x - f_l > (f_max - f_min) * k:
            return False
        if len(keys) > 2 and f_r - f_x > (f_max - f_min) * k and f_l - f_x > (f_max - f_min) * k:
            return False

        return True

    @property
    def points(self):
        # return self._points
        return {
            k: v
            for k, v in filter(self.__is_not_peek, self._points.items())
        }

    @points.setter
    def points(self, value):
        self._points = value