from t_dat_filtered import TDatFiltered, FxType


class TDatLintInt(TDatFiltered):
    def __init__(self):
        super().__init__()

    def _interpolate(self, x1: int, x2: int) -> FxType:
        def fx(x: int) -> float:
            return (
                self.points.get(x1) + ((self.points.get(x2) - self.points.get(x1)) / (x2 - x1)) * (x - x1)
            )

        return fx

    def perform(self, x: int) -> float:
        value = self.points.get(x)
        if value is not None:
            return value

        keys = sorted(self.points.keys())

        _min = max(filter(lambda i: i < x, keys), default=0)
        _max = min(filter(lambda i: i > x, keys), default=0)

        return self._interpolate(_min, _max)(x)
