from typing import Set, List

import pytest
from t_dat_spl_int import TDatSplitInt

@pytest.mark.parametrize("points,value,expected", [
    [[{1, 100.109}, {2, 127}, {3,164}, {4,225}], 1.5, 112.598316309439],
    [[[1, 0], [3, 2], [5, 0], [7, -2], [9, 0]], 2.5, 1.828125],
    [[[1, 0], [3, 2], [5, 0], [7, -2], [9, 0]], 4.5, 0.734375]
])
def test_perform_interpolation(points: List[Set[int]], value: int, expected: int):
    cls = TDatSplitInt()

    [cls.append(x, lambda _: y) for (x, y) in points]

    assert cls.perform(value) == expected
