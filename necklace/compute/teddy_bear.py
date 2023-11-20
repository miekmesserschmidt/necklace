from typing import Iterable, Set
from . import mickey_mouse
from ..core import ArithmeticObject
from ..environ import Environment
from ..structures import MickeyMouse, TeddyBear


def equation(
    t: TeddyBear,
    env: Environment,
) -> ArithmeticObject:
    a = t.body
    b = t.head
    c = t.hand0
    d = t.hand1

    dihed = env.symbol_map(t)
    cos_dhed = env.cos(dihed)

    ang_a_db = env.symbol_map(MickeyMouse(a, d, b).canonical())
    ang_a_bc = env.symbol_map(MickeyMouse(a, b, c).canonical())
    ang_a_dc = env.symbol_map(MickeyMouse(a, d, c).canonical())

    cos_a_dc = env.cos(ang_a_dc)
    cos_a_db = env.cos(ang_a_db)
    cos_a_bc = env.cos(ang_a_bc)

    sin_a_db = env.sin(ang_a_db)
    sin_a_bc = env.sin(ang_a_bc)

    return cos_dhed * (sin_a_db * sin_a_bc) - (cos_a_dc - cos_a_db * cos_a_bc)
