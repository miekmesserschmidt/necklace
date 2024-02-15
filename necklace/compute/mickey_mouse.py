from itertools import combinations, product
from typing import Iterable, List, Set
from ..core import ArithmeticObject, SymbolMap
from ..environ import Environment
from ..structures import (
    Label,
    MickeyMouse,
    MickeyMouseAngle,
    MickeyMouseComplex,
    MickeyMouseComplexMultiplier,
)


def all_mickey_mouses_heads_ears(
    heads: List[Label], ears: List[Label]
) -> Iterable[MickeyMouse]:
    for h, ear in product(heads, ears):
        yield MickeyMouse(h, ear, ear).canonical()

    ears_combinations = list(combinations(ears, 2))
    for h, ears_comb in product(heads, ears_combinations):
        yield MickeyMouse(h, *ears_comb).canonical()


def all_mickey_mouses(symbols: List[Label]) -> Iterable[MickeyMouse]:
    yield from all_mickey_mouses_heads_ears(symbols, symbols)


def cos_angle(
    m: MickeyMouse,
    env: Environment,
) -> ArithmeticObject:
    c = env.symbol_map(m.head)
    a = env.symbol_map(m.ear0)
    b = env.symbol_map(m.ear1)

    return ((c + a) ** 2 + (c + b) ** 2 - (a + b) ** 2) / (2 * (c + a) * (c + b))


def angle(
    m: MickeyMouse,
    env: Environment,
) -> ArithmeticObject:
    mma = MickeyMouseAngle(m)
    return env.symbol_map(mma)


def complex_(
    m: MickeyMouse,
    env: Environment,
) -> ArithmeticObject:
    mmc = MickeyMouseComplex(m)
    return env.symbol_map(mmc)


def complex_multiplier(
    m: MickeyMouse,
    env: Environment,
) -> ArithmeticObject:
    mmc = MickeyMouseComplexMultiplier(m)
    return env.symbol_map(mmc)


def complex_multiplier_equation(m: MickeyMouse, env: Environment) -> ArithmeticObject:
    z = complex_multiplier(m, env)
    w = complex_(m, env)

    c = env.symbol_map(m.head)
    a = env.symbol_map(m.ear0)
    b = env.symbol_map(m.ear1)

    return z * (c + a) - w * (c + b)


def on_complex_unit_circle_equation(
    m: MickeyMouse, env: Environment
) -> ArithmeticObject:
    w = complex_(m, env)
    a = angle(m, env)

    cos_a = env.cos(a)

    left = w**2 + 1
    right = 2 * w * cos_a
    return left - right


def cosine_rule_equation(m: MickeyMouse, env: Environment) -> ArithmeticObject:
    c = env.symbol_map(m.head)
    a = env.symbol_map(m.ear0)
    b = env.symbol_map(m.ear1)

    ang = angle(m, env)

    left = 2 * (c + a) * (c + b) * env.cos(ang)
    right = (c + a) ** 2 + (c + b) ** 2 - (a + b) ** 2
    return left - right
