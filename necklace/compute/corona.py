from itertools import chain
from typing import Iterable, List, cast

import sympy

from necklace.compute import mickey_mouse
from .triangle import all_triangles
from .core import cos_pi_over_3_identity, sin_cos_identity


from ..core import ArithmeticObject
from ..environ import Environment
from ..structures import (
    Corona,
    MickeyMouse,
    MickeyMouseAngle,
    MickeyMouseComplex,
    Triangle,
)
from necklace.compute import triangle


def angle_sum(
    c: Corona,
    env: Environment,
) -> ArithmeticObject:
    result = 0
    result = cast(ArithmeticObject, result)

    for m in c.mickey_mouse_sequence():
        result = env.symbol_map(MickeyMouseAngle(m.canonical())) + result

    return result


def matrix(c: Corona, mickey_mouse_columns: List[MickeyMouse]):
    M = sympy.Matrix.zeros(1, len(mickey_mouse_columns))
    for m in c.mickey_mouse_sequence():
        i = mickey_mouse_columns.index(m)
        M[0, i] += 1

    return M


def whole_matrix(c: Corona, mickey_mouse_columns: List[MickeyMouse]):
    triangles = sorted(all_triangles(c.labels))

    M = sympy.Matrix.zeros(1 + len(triangles), len(mickey_mouse_columns))

    M[0, :] = matrix(c, mickey_mouse_columns)[0, :]

    for i, t in enumerate(triangles, start=1):
        M[i, :] = triangle.matrix(t, mickey_mouse_columns)

    return M


def triangle_matrix(mickey_mouse_columns: List[MickeyMouse]):
    labels = set(chain.from_iterable(m.labels for m in mickey_mouse_columns))
    labels = list(labels)

    triangles = sorted(all_triangles(labels))

    M = sympy.Matrix.zeros(len(triangles), len(mickey_mouse_columns) + 1)

    for i, t in enumerate(triangles):
        M[i, :] = triangle.matrix(t, mickey_mouse_columns)

    return M


def equation(c: Corona, env: Environment) -> ArithmeticObject:
    return env.cos(angle_sum(c, env)) - 1


def sin_equation(c: Corona, env: Environment) -> ArithmeticObject:
    return env.sin(angle_sum(c, env))


def system(c: Corona, env: Environment) -> Iterable[ArithmeticObject]:
    eq = equation(c, env)
    yield eq

    for m in set(c.mickey_mouse_sequence()):
        yield mickey_mouse.equation(m, env)

        ang = env.symbol_map(m)
        yield sin_cos_identity(ang, env)

        if m.head == m.ear0 == m.ear1:
            yield cos_pi_over_3_identity(ang, env)


# def sin_variables(c: Corona, env: Environment) -> Iterable[ArithmeticObject]:
#     symb = env.symbol_map
#     sin = env.sin
#     yield from {sin(symb(MickeyMouseAngle(m))) for m in set(c.mickey_mouse_sequence())}


# def cos_variables(c: Corona, env: Environment) -> Iterable[ArithmeticObject]:
#     # symb = env.symbol_map
#     cos = env.cos
#     yield from {cos(a) for a in angle_variables(c, env)}
#     # yield from {cos(symb(MickeyMouseAngle(m))) for m in set(c.mickey_mouse_sequence())}


def complex_variables(c: Corona, env: Environment) -> Iterable[ArithmeticObject]:
    symb = env.symbol_map
    M = list(set(c.mickey_mouse_sequence()))
    M.sort()
    yield from {symb(MickeyMouseComplex(m)) for m in M}


def angle_variables(c: Corona, env: Environment) -> Iterable[ArithmeticObject]:
    symb = env.symbol_map
    M = list(set(c.mickey_mouse_sequence()))
    M.sort()
    yield from {symb(MickeyMouseAngle(m)) for m in M}


def complex_equation(c: Corona, env: Environment) -> ArithmeticObject:
    result: ArithmeticObject = 1
    for m in c.mickey_mouse_sequence():
        w = mickey_mouse.complex_(m, env)
        result *= w

    return result - 1


def mickey_mouse_complex_system(c: Corona, env: Environment) -> List[ArithmeticObject]:
    M = list(set(c.mickey_mouse_sequence()))
    M.sort()
    return [mickey_mouse.complex_equation(m, env) for m in M]


def complex_system(c: Corona, env: Environment) -> List[ArithmeticObject]:
    M = list(set(c.mickey_mouse_sequence()))
    M.sort()
    return mickey_mouse_complex_system(c, env) + [complex_equation(c, env)]


def radii_variables(c: Corona, env: Environment) -> Iterable[ArithmeticObject]:
    yield from {env.symbol_map(l) for l in c.labels}


def variables(c: Corona, env: Environment) -> Iterable[ArithmeticObject]:
    yield from sin_variables(c, env)
    yield from cos_variables(c, env)
    yield from radii_variables(c, env)
