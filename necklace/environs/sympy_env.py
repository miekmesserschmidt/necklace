from functools import cache
from typing import Any, cast
import sympy
from sympy.core.backend import Symbol, Function

from ..structures import (
    MickeyMouse,
    MickeyMouseAngle,
    MickeyMouseComplex,
    TeddyBear,
    Tripod,
)

from ..core import MathFunc, SymbolMap

from ..environ import ConcreteEnvironment

Expr = sympy.core.expr.Expr


m = Function("m")
mm_angle = Function("a")
mm_complex = Function("w")

t = Function("t")
p = Function("p")


def default_symbol_map(obj: Any) -> Expr:
    match obj:
        case int() as i:
            return Symbol(f"r_{i}", positive=True)

        case MickeyMouse(c, a, b):
            return m(c, a, b)

        case MickeyMouseAngle(MickeyMouse(c, a, b)):
            return mm_angle(c, a, b)

        case MickeyMouseComplex(MickeyMouse(c, a, b)):
            return mm_complex(c, a, b)

        case TeddyBear(b, h, h0, h1):
            return t(b, h, h0, h1)

        case Tripod(a, u, v, w):
            return p(a, u, v, w)

        case _:
            raise ValueError(f"{obj} unrecognized")


default_symbol_map = cast(SymbolMap, default_symbol_map)


def sympy_env(smap: SymbolMap = default_symbol_map) -> ConcreteEnvironment:
    import sympy.core.backend as symeng

    cos = cast(MathFunc, symeng.cos)
    sin = cast(MathFunc, symeng.sin)
    acos = cast(MathFunc, symeng.acos)
    asin = cast(MathFunc, symeng.asin)

    return ConcreteEnvironment(
        smap,
        cos=cos,
        sin=sin,
        acos=acos,
        asin=asin,
        pi=symeng.pi,
    )


env = sympy_env()
