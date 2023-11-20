from typing import Any, cast
import sympy

from ..structures import MickeyMouse, TeddyBear, Tripod

from ..core import MathFunc, SymbolMap

from ..environ import ConcreteEnvironment

Expr = sympy.core.expr.Expr


m = sympy.Function("m")
t = sympy.Function("t")
p = sympy.Function("p")


def default_symbol_map(obj: Any) -> Expr:
    match obj:
        case int() as i:
            return sympy.symbols(f"r_{i}", positive=True)

        case MickeyMouse(c, a, b):
            return m(c, a, b)

        case TeddyBear(b, h, h0, h1):
            return t(b, h, h0, h1)

        case Tripod(a, u, v, w):
            return p(a, u, v, w)

        case _:
            raise ValueError(f"{obj} unrecognized")


default_symbol_map = cast(SymbolMap, default_symbol_map)


def sympy_env(smap: SymbolMap = default_symbol_map) -> ConcreteEnvironment:
    cos = cast(MathFunc, sympy.cos)
    sin = cast(MathFunc, sympy.sin)
    acos = cast(MathFunc, sympy.acos)
    asin = cast(MathFunc, sympy.asin)

    return ConcreteEnvironment(
        smap,
        cos=cos,
        sin=sin,
        acos=acos,
        asin=asin,
        pi=sympy.pi,
    )


env = sympy_env()
