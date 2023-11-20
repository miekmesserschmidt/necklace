from typing import Set
from ..core import ArithmeticObject, SymbolMap
from ..environ import Environment
from ..structures import MickeyMouse


# def cos_angle(
#     m: MickeyMouse,
#     env: Environment,
# ) -> ArithmeticObject:
#     c = env.symbol_map(m.head)
#     a = env.symbol_map(m.ear0)
#     b = env.symbol_map(m.ear1)

#     return ((c + a) ** 2 + (c + b) ** 2 - (a + b) ** 2) / (2 * (c + a) * (c + b))


# def angle(
#     m: MickeyMouse,
#     env: Environment,
# ) -> ArithmeticObject:
#     cos_ang = cos_angle(m, env)
#     return env.acos(cos_ang)


def equation(m: MickeyMouse, env: Environment) -> ArithmeticObject:
    c = env.symbol_map(m.head)
    a = env.symbol_map(m.ear0)
    b = env.symbol_map(m.ear1)

    ang = env.symbol_map(m)

    left = 2 * (c + a) * (c + b) * env.cos(ang)
    right = (c + a) ** 2 + (c + b) ** 2 - (a + b) ** 2
    return left - right
