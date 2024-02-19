from itertools import product
from necklace.gen_numpy import (
    coefficients,
    coefficients_below_value,
    coefficients_lower_upper_between_value,
)
import numpy as np


def test_coefficients_below_value():

    val = 10
    out = coefficients_below_value([1, 2], val)
    out = set(tuple(row) for row in out)

    expected = set(
        (a, b)
        for a, b in product(range(100), repeat=2)
        if (a * 1) <= val and (b * 2) <= val
    )

    assert out == expected


def test_coefficients_lower_upper_between_value():

    val = 10
    coeffs = coefficients_below_value([1, 2], val)

    filtered_coeffs = coefficients_lower_upper_between_value(
        coeffs,
        lower_vec=np.array([1, 2]),
        upper_vec=np.array([1.5, 3]),
        value=val,
    )

    out = set(tuple(row) for row in filtered_coeffs)

    expected = set(
        (a, b)
        for a, b in product(range(100), repeat=2)
        if (a * 1) + (b * 2) <= val and val <= (a * 1.5) + (b * 3)
    )

    assert out == expected


def test_coefficients():

    val = 10
    lower_vec = np.array([1, 2])
    upper_vec = np.array([1.5, 3])
    coeffs = coefficients(lower_vec, upper_vec, val)

    out = set(tuple(row) for row in coeffs)

    expected = set(
        (a, b)
        for a, b in product(range(100), repeat=2)
        if (a * 1) + (b * 2) <= val and val <= (a * 1.5) + (b * 3)
    )

    assert out == expected
