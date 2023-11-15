import sympy

from ..core import SymbolMap
from ..environ import Environment, ConcreteEnvironment


Expr = sympy.core.expr.Expr


def default_symbol_map(label: int) -> Expr:
    return sympy.symbols(f"r_{label}", positive=True)


def sympy_env(smap: SymbolMap[int] = default_symbol_map) -> Environment:
    return ConcreteEnvironment(
        smap,
        cos=sympy.cos,
        sin=sympy.sin,
        acos=sympy.acos,
        asin=sympy.asin,
        pi=sympy.pi,
    )


env = sympy_env()
