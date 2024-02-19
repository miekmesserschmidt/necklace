from typing import List
from necklace.tools import all_rotations, dict_dot, sum_


def test_all_rotations():
    s = (0, 1, 2, 3)

    L = list(all_rotations(s))

    assert L == [
        (0, 1, 2, 3),
        (3, 0, 1, 2),
        (2, 3, 0, 1),
        (1, 2, 3, 0),
    ]


def test_sum_():
    s: List[int] = [0, 1, 2, 3]

    out = sum_(s)
    expected = 1 + 2 + 3

    assert out == expected


def test_dict_dot():
    a = {0: 1, 1: 2}
    b = {1: 3, 2: 4}

    assert dict_dot(a, b) == 6
