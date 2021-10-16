from typing import Set

import pytest
from t_dat_lint_int import TDatLintInt


@pytest.mark.parametrize("points,value,expected", [
    [{1, 3}, 1, 2],
    [{1, 3}, 2, 4],
    [{1, 3}, 3, 6],
])
def test_perform_interpolation(points: Set[int], value: int, expected: int):
    def fx(x: int) -> float:
        return x * 2

    cls = TDatLintInt()

    [cls.append(k, fx) for k in points]

    assert cls.perform(value) == expected
