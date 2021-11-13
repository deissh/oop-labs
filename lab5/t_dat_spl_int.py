from typing import List, Tuple

import bisect
from t_dat_filtered import TDat


class TDatSplitInt(TDat):
    def __init__(TDatFiltered):
        super().__init__()

    def __changes(self, x: List[float]) -> List[float]:
        return [
            x[i+1] - x[i] for i in range(len(x)-1)
        ]
    
    def __create_target(self, n: int, h: List[float], y: List[float]) -> float:
        return [0] + [6 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1]) / (h[i] + h[i-1]) for i in range(1, n - 1)] + [0]

    def __create_matrix(self, n: int, h: List[float]) -> Tuple[List[float], List[float], List[float]]:
        A = [h[i] / (h[i] + h[i + 1]) for i in range(n - 2)] + [0]
        B = [2] * n
        C = [0] + [h[i + 1] / (h[i] + h[i + 1]) for i in range(n - 2)]
        return A, B, C

    def __solve(self, A: List[float], B: List[float], C: List[float], D: List[float]):
        c_p = C + [0]
        d_p = [0] * len(B)
        X = [0] * len(B)

        c_p[0] = C[0] / B[0]
        d_p[0] = D[0] / B[0]
        for i in range(1, len(B)):
            c_p[i] = c_p[i] / (B[i] - c_p[i - 1] * A[i - 1])
            d_p[i] = (D[i] - d_p[i - 1] * A[i - 1]) / (B[i] - c_p[i - 1] * A[i - 1])

        X[-1] = d_p[-1]
        for i in range(len(B) - 2, -1, -1):
            X[i] = d_p[i] - c_p[i] * X[i + 1]

        return X

    def __prebuild_spline(self):
        x = list(self.points.keys())
        y = list(self.points.values())

        n = len(self.points)

        if n < 3:
            raise ValueError("arr len < 3")
        
        diff = self.__changes(x)

        A, B, C = self.__create_matrix(n, diff)
        D = self.__create_target(n, diff, y)
    
        M = self.__solve(A, B, C, D)

        coef = [[(M[i+1]-M[i])*diff[i]*diff[i]/6, M[i]*diff[i]*diff[i]/2, (y[i+1] - y[i] - (M[i+1]+2*M[i])*diff[i]*diff[i]/6), y[i]] for i in range(n-1)]

        def spline(value: float):
            idx = min(bisect.bisect(x, value) - 1, n - 2)
            z = (value - x[idx]) / diff[idx]
            C = coef [idx]

            return ((C[0] * z + C[1])* z + C[2]) * z + C[3]

        return spline

    def perform(self, x: int) -> float:
        # TODO: cached_property
        return self.__prebuild_spline()(x)

