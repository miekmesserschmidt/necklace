from typing import cast

from . import teddy_bear

from . import tripod
from ..core import ArithmeticObject
from ..environ import Environment
from ..structures import Necklace


def dihedral_angle_sum(
    n: Necklace,
    env: Environment,
) -> ArithmeticObject:
    result = 0
    result = cast(ArithmeticObject, result)

    for b in n.teddy_bear_sequence():
        result = teddy_bear.dihedral_angle(b, env) + result

    return result


def solid_angle_on_body(
    n: Necklace,
    env: Environment,
) -> ArithmeticObject:
    result = 0
    result = cast(ArithmeticObject, result)

    for t in n.body_apex_tripods():
        result = tripod.solid_angle(t, env) + result

    return result
