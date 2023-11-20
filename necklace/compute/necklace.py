from typing import cast


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
        result = env.symbol_map(b.canonical()) + result

    return result


def solid_angle_on_body(
    n: Necklace,
    env: Environment,
) -> ArithmeticObject:
    result = 0
    result = cast(ArithmeticObject, result)

    for t in n.body_apex_tripods():
        result = env.symbol_map(t.canonical()) + result

    return result


def equation(n: Necklace, env: Environment) -> ArithmeticObject:
    return env.cos(dihedral_angle_sum(n, env)) - 1
