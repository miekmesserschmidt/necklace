from collections import deque
from dataclasses import dataclass
from typing import Callable, Generic, Protocol, Self, Sequence, TypeAlias, TypeVar
import sympy


from .structures import MickeyMouse, Label, TeddyBear, Tripod

Expr = sympy.Expr


class ArithmeticObject(Protocol):
    def __add__(self, other) -> Self:
        ...

    def __sub__(self, other) -> Self:
        ...

    def __mul__(self, other) -> Self:
        ...

    def __rmul__(self, other) -> Self:
        ...

    def __truediv__(self, other) -> Self:
        ...

    def __pow__(self, other) -> Self:
        ...


class ArithmeticFuncObject(Protocol):
    def __add__(self, other) -> Self:
        ...

    def __sub__(self, other) -> Self:
        ...

    def __mul__(self, other) -> Self:
        ...

    def __rmul__(self, other) -> Self:
        ...

    def __div__(self, other) -> Self:
        ...

    def __pow__(self, other) -> Self:
        ...

    def __call__(self, *args, **kwargs) -> ArithmeticObject:
        ...


SymbolMap: TypeAlias = Callable[[Label], ArithmeticObject]
MathFunc: TypeAlias = Callable[[ArithmeticObject], ArithmeticObject]


class Environment(Protocol, Generic[Label]):
    def cos_mickey_mouse_angle(self, m: MickeyMouse[Label]) -> ArithmeticObject:
        ...

    def mickey_mouse_angle(self, m: MickeyMouse[Label]) -> ArithmeticObject:
        ...

    ##
    def cos_teddy_bear_angle(self, t: TeddyBear[Label]) -> ArithmeticObject:
        ...

    def teddy_bear_angle(self, t: TeddyBear[Label]) -> ArithmeticObject:
        ...

    ##
    def tripod_angle(self, t: Tripod[Label]) -> ArithmeticObject:
        ...


@dataclass
class ConcreteEnvironment(Environment):
    symbol_map: SymbolMap

    cos: MathFunc | ArithmeticFuncObject
    sin: MathFunc | ArithmeticFuncObject
    acos: MathFunc | ArithmeticFuncObject
    asin: MathFunc | ArithmeticFuncObject
    pi: ArithmeticObject

    def cos_mickey_mouse_angle(self, m: MickeyMouse) -> ArithmeticObject:
        c = self.symbol_map(m.head)
        a = self.symbol_map(m.ear0)
        b = self.symbol_map(m.ear1)

        return ((c + a) ** 2 + (c + b) ** 2 - (a + b) ** 2) / (2 * (c + a) * (c + b))

    def mickey_mouse_angle(self, m: MickeyMouse) -> ArithmeticObject:
        cos_ang = self.cos_mickey_mouse_angle(m)
        return self.acos(cos_ang)

    ##
    def cos_teddy_bear_angle(self, t: TeddyBear) -> ArithmeticObject:
        a = t.body
        b = t.head
        c = t.hand0
        d = t.hand1

        cos_a_dc = self.cos_mickey_mouse_angle(MickeyMouse(a, d, c))
        cos_a_db = self.cos_mickey_mouse_angle(MickeyMouse(a, d, b))
        cos_a_bc = self.cos_mickey_mouse_angle(MickeyMouse(a, b, c))

        ang_a_db = self.mickey_mouse_angle(MickeyMouse(a, d, b))
        ang_a_bc = self.mickey_mouse_angle(MickeyMouse(a, b, c))

        sin_a_db = self.sin(ang_a_db)
        sin_a_bc = self.sin(ang_a_bc)

        cos_dihed = (cos_a_dc - cos_a_db * cos_a_bc) / (sin_a_db * sin_a_bc)
        return cos_dihed

    def teddy_bear_angle(self, t: TeddyBear) -> ArithmeticObject:
        cos_ang = self.cos_teddy_bear_angle(t)
        return self.acos(cos_ang)

    ##
    def tripod_angle(self, t: Tripod) -> ArithmeticObject:
        a, b, c = t.leg0, t.leg1, t.leg2

        bear0 = TeddyBear(t.apex, a, b, c)
        bear1 = TeddyBear(t.apex, b, a, c)
        bear2 = TeddyBear(t.apex, c, a, b)

        ang0 = self.teddy_bear_angle(bear0)
        ang1 = self.teddy_bear_angle(bear1)
        ang2 = self.teddy_bear_angle(bear2)

        return ang0 + ang1 + ang2 - self.pi


def default_symbol_map(label: int) -> Expr:
    return sympy.symbols(f"r_{label}", positive=True)


def sympy_env(smap: SymbolMap[Label] = default_symbol_map) -> Environment:
    return ConcreteEnvironment(
        smap,
        cos=sympy.cos,
        sin=sympy.sin,
        acos=sympy.acos,
        asin=sympy.asin,
        pi=sympy.pi,
    )
