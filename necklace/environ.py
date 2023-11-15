from dataclasses import dataclass
from typing import Generic, Protocol, cast

from .core import ArithmeticFuncObject, ArithmeticObject, Label, MathFunc, SymbolMap


from .structures import MickeyMouse, Necklace, TeddyBear, Tripod


class Environment(Protocol):
    def cos_mickey_mouse_angle(self, m: MickeyMouse) -> ArithmeticObject:
        ...

    def mickey_mouse_angle(self, m: MickeyMouse) -> ArithmeticObject:
        ...

    ##
    def cos_teddy_bear_dihedral_angle(self, t: TeddyBear) -> ArithmeticObject:
        ...

    def teddy_bear_dihedral_angle(self, t: TeddyBear) -> ArithmeticObject:
        ...

    ##
    def tripod_solid_angle(self, t: Tripod) -> ArithmeticObject:
        ...

    def necklace_dihedral_angle_sum(self, n: Necklace) -> ArithmeticObject:
        ...


@dataclass
class ConcreteEnvironment(Environment, Generic[Label]):
    symbol_map: SymbolMap[Label]

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
    def cos_teddy_bear_dihedral_angle(self, t: TeddyBear) -> ArithmeticObject:
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

    def teddy_bear_dihedral_angle(self, t: TeddyBear) -> ArithmeticObject:
        cos_ang = self.cos_teddy_bear_dihedral_angle(t)
        return self.acos(cos_ang)

    ##
    def tripod_solid_angle(self, t: Tripod) -> ArithmeticObject:
        a, b, c = t.leg0, t.leg1, t.leg2

        bear0 = TeddyBear(t.apex, a, b, c)
        bear1 = TeddyBear(t.apex, b, a, c)
        bear2 = TeddyBear(t.apex, c, a, b)

        ang0 = self.teddy_bear_dihedral_angle(bear0)
        ang1 = self.teddy_bear_dihedral_angle(bear1)
        ang2 = self.teddy_bear_dihedral_angle(bear2)

        return ang0 + ang1 + ang2 - self.pi

    def necklace_dihedral_angle_sum(self, n: Necklace) -> ArithmeticObject:
        result = 0
        result = cast(ArithmeticObject, result)

        for b in n.teddy_bear_sequence():
            result = self.teddy_bear_dihedral_angle(b) + result

        return result

    def necklace_area_on_body(self, n: Necklace) -> ArithmeticObject:
        result = 0
        result = cast(ArithmeticObject, result)

        for t in n.body_apex_tripods():
            result = self.tripod_solid_angle(t) + result

        return result
