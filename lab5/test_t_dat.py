from typing import Optional, Set
import pytest
from t_dat import TDat


@pytest.mark.parametrize("x_min,x_max,expected_min,expected_max", [
    (None, 0, 0, 0),
    (None, 5, 0, 5),
    (-3, None, -3, 0),
    (-5, 5, -5, 5),
])
def test_min_max_as_pre_def(
        x_min: Optional[int], x_max: Optional[int], expected_min: int, expected_max: int
):
    cls = TDat(x_min=x_min, x_max=x_max)

    assert cls.min == expected_min
    assert cls.max == expected_max

    cls = TDat()
    cls.min = x_min
    cls.max = x_max

    assert cls.min == expected_min
    assert cls.max == expected_max


@pytest.mark.parametrize("points,x_min,x_max,expected_min,expected_max", [
    [{}, 0, 10, 0, 10],
    [{1, 2}, None, 10, 1, 10],
    [{1, 10}, None, None, 1, 10],
    [{1, 10}, 3, None, 3, 10],
    [{-5, 5}, None, None, -5, 5],
])
def test_min_max_as_computed(
        points: Set[int], x_min: Optional[int], x_max: Optional[int], expected_min: int, expected_max: int
):
    cls = TDat(x_min=x_min, x_max=x_max)

    [cls.append(k, lambda x: x * 2) for k in points]

    assert cls.min == expected_min
    assert cls.max == expected_max


@pytest.mark.parametrize("points,value,expected", [
    [{1, 2, 3, 4}, 1, 2],
    [{1, 2, 3, 4}, 2, 4],
    [{1, 2, 3, 4}, 3, 6],
    [{1, 2, 3, 4}, 4, 8],
    [{1, 2, 3, 4}, 5, 0],
    [{1, 2, 3, 4}, 6, 0],
])
def test_perform(points: Set[int], value: int, expected: int):
    def fx(x: int) -> float:
        return x * 2

    cls = TDat()
    [cls.append(k, fx) for k in points]

    assert cls.perform(value) == expected


def test_clear():
    def fx(x: int) -> float:
        return x * 2

    cls = TDat()
    [cls.append(k, fx) for k in range(10)]

    cls.clear()

    assert len(cls.points) == 0
