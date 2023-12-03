from itertools import combinations
from typing import Iterable, List, cast

import sympy

from necklace.compute import mickey_mouse
from .core import cos_pi_over_3_identity, sin_cos_identity


from ..core import ArithmeticObject, Label
from ..environ import Environment
from ..structures import Corona, MickeyMouse, NodeId, Triangle


def all_triangles(symbols: List[NodeId]) -> Iterable[Triangle]:
    for s in symbols:
        yield Triangle(s, s, s).canonical()

    for a, b in combinations(symbols, 2):
        yield Triangle(a, b, b).canonical()
        yield Triangle(b, a, a).canonical()

    for a, b, c in combinations(symbols, 3):
        yield Triangle(a, b, c).canonical()


def matrix(t: Triangle, mickey_mouse_columns: List[MickeyMouse]):
    M = sympy.Matrix.zeros(1, len(mickey_mouse_columns) + 1)
    for m in t.mickey_mouse_sequence():
        i = mickey_mouse_columns.index(m)
        M[0, i] += 1

    M[0, -1] = sympy.pi
    return M
