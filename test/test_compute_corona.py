from necklace.compute import corona
from necklace.compute import mickey_mouse
from necklace.compute.mickey_mouse import angle
from necklace.poly.tools import ensure_square_of_sub_expressions
from necklace.structures import (
    Corona,
    MickeyMouse,
    MickeyMouseAngle,
)

from typing import cast
import sympy
from necklace.compute import necklace


from necklace.structures import Necklace
from necklace.environs.sympy_env import env


def test_corona_eq():
    c = Corona(0, (1, 2, 3, 4))

    eq = corona.equation(c, env)

    s = env.symbol_map
    expected = (
        env.cos(
            s(MickeyMouseAngle(MickeyMouse(0, 1, 2).canonical()))
            + s(MickeyMouseAngle(MickeyMouse(0, 2, 3).canonical()))
            + s(MickeyMouseAngle(MickeyMouse(0, 3, 4).canonical()))
            + s(MickeyMouseAngle(MickeyMouse(0, 4, 1).canonical()))
        )
        - 1
    )

    assert eq - expected == 0


def test_matrix():
    c = Corona(0, (1, 1, 1, 1))
    mms = sorted(set(mickey_mouse.all_mickey_mouses([0, 1])))

    M = corona.matrix(c, mms)
    print(M)

    assert M == sympy.Matrix([[0, 0, 4, 0, 0, 0]])


def test_whole_matrix():
    c = Corona(0, (1, 1, 1, 1))
    mms = sorted(set(mickey_mouse.all_mickey_mouses([0, 1])))

    M = corona.whole_matrix(c, mms)

    print(M)

    assert M == sympy.Matrix(
        [
            [0, 0, 4, 0, 0, 0],
            [3, 0, 0, 0, 0, 0],
            [0, 2, 0, 1, 0, 0],
            [0, 0, 1, 0, 2, 0],
            [0, 0, 0, 0, 0, 3],
        ]
    )


def test_whole_matrix2():
    c = Corona(0, (0, 0, 1, 1))
    mms = sorted(set(mickey_mouse.all_mickey_mouses([0, 1])))

    M = corona.whole_matrix(c, mms)

    print(M)

    assert M == sympy.Matrix(
        [
            [1, 2, 1, 0, 0, 0],
            [3, 0, 0, 0, 0, 0],
            [0, 2, 0, 1, 0, 0],
            [0, 0, 1, 0, 2, 0],
            [0, 0, 0, 0, 0, 3],
        ]
    )


def test_corona_complex_system():
    c = Corona(0, (1, 2, 3, 4))
    system = corona.complex_system(c, env)
    print(system)


# def test_corona_system():
#     c = Corona(
#         0,
#         (1, 2, 3, 4),
#     )
#     cos_symbols = list(corona.cos_variables(c, env))
#     sin_symbols = list(corona.sin_variables(c, env))
#     rad_symbols = list(corona.radii_variables(c, env))

#     cos_symbols.sort(key=lambda s: str(s))
#     sin_symbols.sort(key=lambda s: str(s))
#     rad_symbols.sort(key=lambda s: str(s))

#     print(rad_symbols)
#     r0, r1, *rest = rad_symbols

#     rad_symbols.sort(key=lambda s: str(s))
#     cos_symbols.sort(key=lambda s: str(s))
#     sin_symbols.sort(key=lambda s: str(s))

#     subs_dict = {
#         env.symbol_map(m): angle(m, env).expand()
#         for m in set(c.mickey_mouse_sequence())
#     }

#     eq = corona.equation(c, env)
#     print("expand trig")
#     eq = sympy.expand_trig(eq).expand()
#     eq = ensure_square_of_sub_expressions(eq, sin_symbols)

#     print("exp")
#     eq = eq.expand()

#     print("subs")
#     eq = eq.subs(subs_dict)
#     # print("simplify")
#     # eq = eq.simplify()

#     print("together")
#     eq = eq.together()
#     # print("frac_exp")
#     # eq = eq.expand()

#     print("frac num")
#     eq, _ = sympy.fraction(eq)

#     print("expr tree")
#     for a in eq.args:
#         print("\n\n", a.expand(evaluate=False))

#     # eq = eq.expand()

#     # print("expanding")
#     # eq = eq.expand()
#     # print("factoring")
#     # eq = eq.factor()
#     # print(eq)
#     print("groebner")
#     G = sympy.groebner([eq], *rad_symbols)
#     print(G)

#     print(eq.subs({r: r1 for r in rest}).factor())

#     c = Corona(
#         0,
#         (1, 1, 1, 1),
#     )
#     cos_symbols = list(corona.cos_variables(c, env))
#     sin_symbols = list(corona.sin_variables(c, env))
#     rad_symbols = list(corona.radii_variables(c, env))

#     cos_symbols.sort(key=lambda s: str(s))
#     sin_symbols.sort(key=lambda s: str(s))
#     rad_symbols.sort(key=lambda s: str(s))

#     subs_dict = {
#         env.symbol_map(m): angle(m, env) for m in set(c.mickey_mouse_sequence())
#     }

#     eq = corona.equation(c, env)
#     eq = sympy.expand_trig(eq).expand()
#     eq = ensure_square_of_sub_expressions(eq, sin_symbols)
#     eq = eq.subs(subs_dict).together()
#     eq, _ = sympy.fraction(eq)
#     # eq = eq.expand()

#     print("0:111 ", eq.factor())

# symbols_order.reverse()

# count = 0
# N = len(rad_symbols)

# def elim_order(deg_list: list[int]):
#     nonlocal count
#     count += 1

#     rs = deg_list[-N:]
#     rest = deg_list[:-N]

#     out = (
#         sum(rest),
#         tuple(rest),
#         sum(rs),
#         tuple(rs),
#     )
#     if count % 1_000_000 == 0:
#         print(count, out, deg_list, rs, rest)
#     return out

#     # return (sum(rs), tuple(rs), sum(rest), tuple(rest))

# for p in sys:
#     print(p, "\n\n")

# print("GROEBNER:")
# g = sympy.groebner(
#     new_sys,
#     *(sin_symbols + cos_symbols + rad_symbols),
#     domain="ZZ",
#     # domain="ZZ[r_0]",
#     # domain="ZZ[r_0]",
#     # domain=DOM,
#     # order=elim_order,
#     order="lex",
#     # method="f5b",
# )
# for p in g:
#     print(p, "\n\n")
