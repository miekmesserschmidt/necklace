from dataclasses import dataclass
from typing import Any, Protocol, Self

import sympy

from necklace.eval import symp
from .tools import sum_

from .structures import Corona, MickeyMouse, MickeyMouseAngle
from .core import ArithmeticObject


class Bound(Protocol):
    value: ArithmeticObject

    def __add__(self, other: Self) -> Self: ...

    def __rmul__(self, other: int) -> Self: ...


@dataclass
class Equal(Bound):
    value: ArithmeticObject

    def __add__(self, other: Bound) -> Bound:
        match other:
            case Strict(val):
                return Strict(val + self.value)
            case Equal(val):
                return Equal(val + self.value)
            case _:
                raise ValueError(f"Cannot add bounds {self} to {other}")

    def __rmul__(self, other: Any) -> Bound:
        match other:
            case int():
                return Equal(other * self.value)
            case _:
                raise ArithmeticError(f"Cannot multiply {self} with {other}")


@dataclass
class Strict(Bound):
    value: ArithmeticObject

    def __add__(self, other: Bound) -> Bound:
        return Strict(other.value + self.value)

    def __rmul__(self, other: Any) -> Bound:
        match other:
            case int():
                return Strict(other * self.value)
            case _:
                raise ArithmeticError(f"Cannot multiply {self} with {other}")


def normalize(mm: MickeyMouse) -> MickeyMouse:
    c, a, b = mm.head, mm.ear0, mm.ear1

    cnorm = 1
    anorm = 1
    if a < c:
        anorm = 0
    if c < a:
        anorm = 2

    bnorm = 1
    if b < c:
        bnorm = 0
    if c < b:
        bnorm = 2

    return MickeyMouse(cnorm, anorm, bnorm).canonical()


def mickey_mouse_lower_bound(
    mm: MickeyMouse, smallest_r0: ArithmeticObject | None = None
) -> Bound:
    norm_mm = normalize(mm)

    match norm_mm:
        case MickeyMouse(1, 1, 1):
            return Equal(sympy.pi / 3)
        case MickeyMouse(1, 2, 1) | MickeyMouse(1, 2, 2):
            return Strict(sympy.pi / 3)
        case MickeyMouse(1, 1, 0) | MickeyMouse(1, 2, 0) | MickeyMouse(1, 0, 0):
            if smallest_r0 is None:
                raise ValueError(f"Smallest r0 not provided")
            ang = MickeyMouseAngle(norm_mm)
            ang_expr = symp.evaluate(ang)
            ang_val = ang_expr.subs(
                {
                    symp.symbol(0): smallest_r0,
                    symp.symbol(1): 1,
                    symp.symbol(2): 1,
                }
            )
            return Strict(ang_val)
        case _:
            raise ValueError(f"Should not happen {mm=}, {smallest_r0=}")


def mickey_mouse_upper_bound(mm: MickeyMouse) -> Bound:
    norm_mm = normalize(mm)

    match norm_mm:
        case MickeyMouse(1, 1, 1):
            return Equal(symp.pi / 3)
        case MickeyMouse(1, 1, 0) | MickeyMouse(1, 0, 0):
            return Strict(symp.pi / 3)
        case MickeyMouse(1, 2, 0) | MickeyMouse(1, 2, 1):
            return Strict(symp.pi / 2)
        case MickeyMouse(1, 2, 2):
            return Strict(symp.pi)
        case _:
            raise ValueError(f"Should not happen {mm=}")


def corona_lower_bound(
    cor: Corona, smallest_r0: ArithmeticObject | None = None
) -> Bound:
    return sum_(
        mickey_mouse_lower_bound(m, smallest_r0) for m in cor.mickey_mouse_sequence()
    )


def corona_upper_bound(
    cor: Corona, smallest_r0: ArithmeticObject | None = None
) -> Bound:
    return sum_(mickey_mouse_upper_bound(m) for m in cor.mickey_mouse_sequence())
