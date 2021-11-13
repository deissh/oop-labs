from typing import Dict, Callable, Optional

from t_dat import TDat, FxType


class TDatFiltered(TDat):
    def append(self, x: int, fx: FxType):
        
        keys = sorted(self.points.keys())

        left = max(filter(lambda i: i < x, keys))
        right = min(filter(lambda i: i > x, keys))

        if fx(x) - fx(right) > (fx(self._x_max) - fx(self._x_min)) * len(keys) and fx(x) - fx(left) > (fx(self._x_max) - fx(self._x_min)) * len(keys):
            return

        if fx(right) - fx(x) > (fx(self._x_max) - fx(self._x_min)) * len(keys) and fx(left) - fx(x) > (fx(self._x_max) - fx(self._x_min)) * len(keys):
            return

        self.points[x] = fx(x)
