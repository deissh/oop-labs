from typing import Set, List

import pytest
from t_dat_spl_int import TDatSplitInt

@pytest.mark.parametrize("points,value,expected", [
    [[{1, 100.109}, {2, 127}, {3, 164}, {4, 225}], 1.5, 113.57747090081477],
    [[[1, 3], [3, 2], [5, 0], [7, -2], [9, -6]], 6, -0.85],
    [[[1, 3], [3, 2], [5, 1], [7, -2], [9, 0]], 4.5, 1.22265625],

    # test peeks
    [[[1, 1], [2, 1], [3, -2], [4, 1], [5, 1]], 4.5, 1],
    [[[1, 1], [2, 1], [3, -2], [4, 1], [5, 1]], 3, 1],
])
def test_perform_interpolation(points: List[Set[int]], value: int, expected: int):
    cls = TDatSplitInt()

    [cls.append(x, lambda _: y) for (x, y) in points]

    print(cls.points)

    assert cls.perform(value) == expected
