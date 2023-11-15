from typing import cast
import sympy

from ..core import MathFunc, SymbolMap
from ..environ import Environment, ConcreteEnvironment


Expr = sympy.core.expr.Expr


def default_symbol_map(label: int) -> Expr:
    return sympy.symbols(f"r_{label}", positive=True)


default_symbol_map = cast(SymbolMap[int], default_symbol_map)


def sympy_env(smap: SymbolMap[int] = default_symbol_map) -> ConcreteEnvironment:
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
