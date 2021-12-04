import pytest
from rpn_calc import rpn_calc


@pytest.mark.parametrize("exp,result", [
    ("1 1 +", 2.),
    ("1 1 -", .0),
    ("4 2 /", 2.),
    ("45 9 * 13 - 2 ^", 153664.),
    ("999 3 / 7 /", 999 / 3 / 7),
])
def test_rpn_calc(exp: str, result: float):
    assert rpn_calc(exp) == result
