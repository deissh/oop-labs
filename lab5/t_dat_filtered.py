from typing import Dict, Callable, Optional

from t_dat import TDat, FxType


class TDatFiltered(TDat):
    @property
    def points(self) -> Dict[int, float]:
        return self._points
