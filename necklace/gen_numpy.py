from itertools import product
from typing import Any
import numpy as np

from .tools import weighted_range


def coefficients_below_value(lower_vec: np.ndarray, value: Any) -> np.ndarray:
    ranges = [weighted_range(w, value) for w in lower_vec]
    return np.array([*product(*ranges)])


def coefficients_lower_upper_between_value(
    coefficients: np.ndarray,
    lower_vec: np.ndarray,
    upper_vec: np.ndarray,
    value: Any,
) -> np.ndarray:
    lower_vals = (coefficients * lower_vec).sum(axis=1)
    upper_vals = (coefficients * upper_vec).sum(axis=1)

    filter_ = (lower_vals <= value) & (value <= upper_vals)
    return coefficients[filter_]


def coefficients(
    lower_vec: np.ndarray,
    upper_vec: np.ndarray,
    value: Any,
) -> np.ndarray:

    coeffs = coefficients_below_value(lower_vec, value)
    return coefficients_lower_upper_between_value(
        coeffs,
        lower_vec,
        upper_vec,
        value,
    )
