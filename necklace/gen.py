from itertools import product
from typing import Callable, Dict, Iterable, Set, TypeAlias

import sympy

from .tools import dict_dot

from .core import ArithmeticObject

from .compare import (
    Bound,
    Equal,
    Strict,
    corona_lower_bound,
    corona_upper_bound,
)
from .structures import Corona, Label, MickeyMouse


Acceptor: TypeAlias = Callable[[Corona], bool]
Continue: TypeAlias = Callable[[Corona], bool]
BoundComputer: TypeAlias = Callable[[Corona], Bound]


def lower_ok(bound: Bound) -> bool:
    match bound:
        case Equal(val):
            return val <= 2 * sympy.pi
        case Strict(val):
            return val < 2 * sympy.pi
        case _:
            raise ValueError("wat?")


def upper_ok(bound: Bound) -> bool:
    match bound:
        case Equal(val):
            return 2 * sympy.pi <= val
        case Strict(val):
            return 2 * sympy.pi < val
        case _:
            raise ValueError("wat?")


def gen_coronas(
    starter: Corona,
    symbols: Set[Label],
    lower_bound_computer: BoundComputer = corona_lower_bound,
    upper_bound_computer: BoundComputer = corona_upper_bound,
) -> Iterable[Corona]:

    c = starter.center
    seq = list(starter.seq)

    for s in symbols:
        new_cor = Corona(c, seq=tuple(seq + [s]))

        lower_b = lower_bound_computer(new_cor)
        upper_b = upper_bound_computer(new_cor)

        # accept the corona
        if lower_ok(lower_b) and upper_ok(upper_b):
            yield new_cor

        # continue generating
        if lower_b.value <= 2 * sympy.pi:
            yield from gen_coronas(
                new_cor,
                symbols,
                lower_bound_computer=lower_bound_computer,
                upper_bound_computer=upper_bound_computer,
            )


def gen_all_mickey_mouses(
    centers: Set[Label], ears: Set[Label]
) -> Iterable[MickeyMouse]:
    for c, a, b in product(centers, ears, ears):
        yield MickeyMouse(c, a, b)


def gen_mickey_mouse_dicts(
    start_dict: Dict[MickeyMouse, int],
    mickey_mouse_set: Set[MickeyMouse],
    lower_vec: Dict[MickeyMouse, Bound],
    upper_vec: Dict[MickeyMouse, Bound],
):

    if start_dict:
        lower_bound = dict_dot(start_dict, lower_vec)
        upper_bound = dict_dot(start_dict, upper_vec)

        if lower_ok(lower_bound) and upper_ok(upper_bound):
            yield start_dict

    if (not start_dict) or (lower_bound.value <= 2 * sympy.pi):
        for mm in mickey_mouse_set:
            new_dict = start_dict.copy()
            new_dict[mm] += 1

            yield from gen_mickey_mouse_dicts(
                new_dict, mickey_mouse_set, lower_vec, upper_vec
            )


def gen_coronas(mickey_mouse_dict: Dict[MickeyMouse, int]) -> Iterable[Corona]: ...
