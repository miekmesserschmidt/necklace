from itertools import combinations, product
from typing import Iterable, List, Set
from ..core import ArithmeticObject, SymbolMap
from ..environ import Environment
from ..structures import Label, MickeyMouse


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
    cos_ang = cos_angle(m, env)
    return env.acos(cos_ang)


def equation(m: MickeyMouse, env: Environment) -> ArithmeticObject:
    c = env.symbol_map(m.head)
    a = env.symbol_map(m.ear0)
    b = env.symbol_map(m.ear1)

    ang = env.symbol_map(m)

    left = 2 * (c + a) * (c + b) * env.cos(ang)
    right = (c + a) ** 2 + (c + b) ** 2 - (a + b) ** 2
    return left - right
