from itertools import combinations
from typing import Iterable, List, cast
from psutil import AccessDenied

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
    M = sympy.Matrix.zeros(1, len(mickey_mouse_columns))
    for m in t.mickey_mouse_sequence():
        i = mickey_mouse_columns.index(m)
        M[0, i] += 1

    # M[0, -1] = sympy.pi
    return M


def complex_angle_sum_equation(t: Triangle, env: Environment):
    A = MickeyMouse(t.a, t.b, t.c).canonical()
    B = MickeyMouse(t.b, t.a, t.c).canonical()
    C = MickeyMouse(t.c, t.b, t.a).canonical()

    w0 = mickey_mouse.complex_(A, env)
    w1 = mickey_mouse.complex_(B, env)
    w2 = mickey_mouse.complex_(C, env)

    return w0 * w1 * w2 + 1


def real_angle_sum_equation(t: Triangle, env: Environment):
    A = MickeyMouse(t.a, t.b, t.c).canonical()
    B = MickeyMouse(t.b, t.a, t.c).canonical()
    C = MickeyMouse(t.c, t.b, t.a).canonical()

    a0 = mickey_mouse.angle(A, env)
    a1 = mickey_mouse.angle(B, env)
    a2 = mickey_mouse.angle(C, env)

    return a0 + a1 + a2 - env.pi
