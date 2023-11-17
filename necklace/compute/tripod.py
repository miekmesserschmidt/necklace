from typing import cast

from .teddy_bear import teddy_bear_dihedral_angle
from ..core import ArithmeticObject
from ..environ import Environment
from ..structures import TeddyBear, Tripod


def tripod_solid_angle(
    t: Tripod,
    env: Environment,
) -> ArithmeticObject:
    a, b, c = t.leg0, t.leg1, t.leg2

    bear0 = TeddyBear(t.apex, a, b, c)
    bear1 = TeddyBear(t.apex, b, a, c)
    bear2 = TeddyBear(t.apex, c, a, b)

    ang0 = teddy_bear_dihedral_angle(bear0, env)
    ang1 = teddy_bear_dihedral_angle(bear1, env)
    ang2 = teddy_bear_dihedral_angle(bear2, env)

    return ang0 + ang1 + ang2 - env.pi
