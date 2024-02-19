from typing import List
from necklace.tools import (
    all_rotations,
    dict_dot,
    sum_,
    weighted_range,
)


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


def test_weighted_range_0():
    out = weighted_range(1, 10)
    expected = range(0, 11)

    assert out == expected


def test_weighted_range_2():
    out = weighted_range(2, 10)
    expected = range(0, 6)

    assert out == expected


def test_weighted_range_1_0():
    out = weighted_range(1.0, 10)
    expected = range(0, 11)

    assert out == expected


def test_weighted_range_0_1():
    out = weighted_range(0.1, 10)
    expected = range(0, 100)

    assert out == expected
