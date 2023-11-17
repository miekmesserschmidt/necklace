from typing import cast

from .teddy_bear import teddy_bear_dihedral_angle

from .tripod import tripod_solid_angle
from ..core import ArithmeticObject
from ..environ import Environment
from ..structures import Necklace


def necklace_dihedral_angle_sum(
    n: Necklace,
    env: Environment,
) -> ArithmeticObject:
    result = 0
    result = cast(ArithmeticObject, result)

    for b in n.teddy_bear_sequence():
        result = teddy_bear_dihedral_angle(b, env) + result

    return result


def necklace_solid_angle_on_body(
    n: Necklace,
    env: Environment,
) -> ArithmeticObject:
    result = 0
    result = cast(ArithmeticObject, result)

    for t in n.body_apex_tripods():
        result = tripod_solid_angle(t, env) + result

    return result
