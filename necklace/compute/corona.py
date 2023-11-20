from typing import Iterable, cast

from necklace.compute import mickey_mouse
from .core import sin_cos_identity


from ..core import ArithmeticObject
from ..environ import Environment
from ..structures import Corona


def angle_sum(
    c: Corona,
    env: Environment,
) -> ArithmeticObject:
    result = 0
    result = cast(ArithmeticObject, result)

    for m in c.mickey_mouse_sequence():
        result = env.symbol_map(m.canonical()) + result

    return result


def equation(c: Corona, env: Environment) -> ArithmeticObject:
    return env.cos(angle_sum(c, env)) - 1


def system(c: Corona, env: Environment) -> list[ArithmeticObject]:
    eq = equation(c, env)

    mick_eqs = list(mickey_mouse.equation(m, env) for m in c.mickey_mouse_sequence())
    mick_sin_cos_ids = list(
        sin_cos_identity(env.symbol_map(m), env) for m in c.mickey_mouse_sequence()
    )

    return [eq] + mick_eqs + mick_sin_cos_ids
