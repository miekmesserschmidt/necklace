from functools import reduce
from typing import cast

from .teddy_bear import teddy_bear_dihedral_angle

from .tripod import tripod_solid_angle
from ..core import ArithmeticObject
from ..environ import Environment
from ..structures import Necklace, Pooh, TeddyBear, Tripod
from necklace.compute import teddy_bear


def pooh_left_solid_angle(
    p: Pooh,
    env: Environment,
) -> ArithmeticObject:
    t = Tripod(p.body, p.head, p.hand0, p.hunny)
    return tripod_solid_angle(t, env)


def pooh_right_solid_angle(
    p: Pooh,
    env: Environment,
) -> ArithmeticObject:
    t = Tripod(p.body, p.head, p.hunny, p.hand1)
    return tripod_solid_angle(t, env)


def pooh_left_dihedral_angle(p: Pooh, env: Environment) -> ArithmeticObject:
    t = TeddyBear(p.body, p.head, p.hand0, p.hunny)
    return teddy_bear_dihedral_angle(t, env)


def pooh_right_dihedral_angle(p: Pooh, env: Environment) -> ArithmeticObject:
    t = TeddyBear(p.body, p.head, p.hunny, p.hand1)
    return teddy_bear_dihedral_angle(t, env)


def pooh_hands_dihedral_angle(p: Pooh, env: Environment) -> ArithmeticObject:
    t = TeddyBear(p.body, p.head, p.hand0, p.hand1)
    return teddy_bear_dihedral_angle(t, env)


def pooh_descartes_theorem(p: Pooh, env: Environment) -> ArithmeticObject:
    dim = 3

    five = (p.body, p.head, p.hand0, p.hunny, p.hand1)

    curvatures = tuple(1 / env.symbol_map(i) for i in five)

    left = reduce(lambda a, b: a + b, (c for c in curvatures)) ** 2
    right = dim * reduce(lambda a, b: a + b, (c**2 for c in curvatures))

    return left - right
