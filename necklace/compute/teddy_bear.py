from . import mickey_mouse
from ..core import ArithmeticObject
from ..environ import Environment
from ..structures import MickeyMouse, TeddyBear


def cos_dihedral_angle(
    t: TeddyBear,
    env: Environment,
) -> ArithmeticObject:
    a = t.body
    b = t.head
    c = t.hand0
    d = t.hand1

    cos_a_dc = mickey_mouse.cos_angle(MickeyMouse(a, d, c), env)
    cos_a_db = mickey_mouse.cos_angle(MickeyMouse(a, d, b), env)
    cos_a_bc = mickey_mouse.cos_angle(MickeyMouse(a, b, c), env)

    ang_a_db = mickey_mouse.angle(MickeyMouse(a, d, b), env)
    ang_a_bc = mickey_mouse.angle(MickeyMouse(a, b, c), env)

    sin_a_db = env.sin(ang_a_db)
    sin_a_bc = env.sin(ang_a_bc)

    cos_dihed = (cos_a_dc - cos_a_db * cos_a_bc) / (sin_a_db * sin_a_bc)
    return cos_dihed


def dihedral_angle(
    t: TeddyBear,
    env: Environment,
) -> ArithmeticObject:
    cos_ang = cos_dihedral_angle(t, env)
    return env.acos(cos_ang)
