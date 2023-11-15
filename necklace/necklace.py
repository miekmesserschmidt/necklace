# from collections import deque
# from dataclasses import dataclass
# from typing import Callable, Generic, Sequence, TypeAlias, TypeVar
# import sympy

# Expr = sympy.Expr


# Label = TypeVar("Label")
# SymbolMap: TypeAlias = Callable[[Label], Expr]


# @dataclass
# class Necklace(Generic[Label]):
#     head: Label
#     body: Label
#     beads: Sequence[Label]


# def cosang(c: Expr, a: Expr, b: Expr) -> Expr:
#     return ((c + a) ** 2 + (c + b) ** 2 - (a + b) ** 2) / (2 * (c + a) * (c + b))


# def ang(c: Expr, a: Expr, b: Expr, acos=sympy.acos):
#     return acos(cosang(c, a, b))


# def cos_dihedral_angle(body: Expr, head: Expr, hand0: Expr, hand1: Expr) -> Expr:
#     cos = sympy.cos
#     sin = sympy.sin

#     a = body
#     b = head
#     c = hand0
#     d = hand1

#     cos_dihed = (cos(ang(a, d, c)) - cos(ang(a, d, b)) * cos(ang(a, b, c))) / (
#         sin(ang(a, d, b)) * sin(ang(a, b, c))
#     )
#     return cos_dihed


# def dihedral_angle(body, head, hand0, hand1, acos=sympy.acos) -> Expr:
#     return acos(cos_dihedral_angle(body, head, hand0, hand1))


# def necklace_expression(necklace: Necklace, smap: SymbolMap) -> Expr:
#     bod = smap(necklace.body)
#     hed = smap(necklace.head)

#     beads0 = deque(map(smap, necklace.beads))
#     beads1 = beads0.copy()
#     beads1.rotate()

#     gen = (dihedral_angle(bod, hed, a, b) for a, b in zip(beads0, beads1))
#     result: Expr = 0
#     for d in gen:
#         result += d
#     return result
