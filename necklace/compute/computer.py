from typing import Any, Protocol

from sympy import Expr
import sympy

from ..core import ArithmeticObject

from ..structures import MickeyMouse, Necklace, TeddyBear


class Computer(Protocol):
    def symbol(self, index: int): ...
    def mickey_mouse(self, mm: MickeyMouse): ...
    def teddy_bear(self, tb: TeddyBear): ...
    def necklace(self, n: Necklace): ...

    def compute(self, obj: Any):
        match obj:
            case int() as i:
                return self.symbol(i)

            case MickeyMouse() as mm:
                return self.mickey_mouse(mm)

            case TeddyBear() as tb:
                return self.teddy_bear(tb)

            case Necklace() as n:
                return self.necklace(n)


class DefaultComputer(Computer):

    def symbol(self, index: int):
        return sympy.symbols(f"r_{index}", positive=True)

    def mickey_mouse(self, mm: MickeyMouse):
        rc = self.symbol(mm.head)
        ra = self.symbol(mm.ear0)
        rb = self.symbol(mm.ear1)

        cos_ang = ((rc + ra) ** 2 + (rc + rb) ** 2 - (ra + rb) ** 2) / (
            2 * (rc + ra) * (rc + rb)
        )
        return sympy.acos(cos_ang)

    def teddy_bear(self, tb: TeddyBear):
        a, b = tb.body, tb.head
        c, d = tb.hand0, tb.hand1

        ang_a_dc = self.mickey_mouse(MickeyMouse(a, d, c))
        ang_a_db = self.mickey_mouse(MickeyMouse(a, d, b))
        ang_a_bc = self.mickey_mouse(MickeyMouse(a, b, c))

        cos = sympy.cos
        sin = sympy.sin
        cos_dihed = (cos(ang_a_dc) - cos(ang_a_db) * cos(ang_a_bc)) / (
            sin(ang_a_db) * sin(ang_a_bc)
        )

        return sympy.acos(cos_dihed)

    def necklace(self, n: Necklace):
        return sum(self.teddy_bear(tb) for tb in n.teddy_bear_sequence())
