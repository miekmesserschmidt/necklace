from typing import cast
import sympy
from necklace.compute import necklace


from necklace.structures import Necklace
from necklace.environs.sympy_env import env


def test_necklace():
    n = Necklace(0, 1, (0, 1, 2))


def test_necklace_expr():
    n = Necklace(0, 1, (2, 2, 2, 2))

    expr = necklace.dihedral_angle_sum(n, env)
    print(expr)


def test_necklace_expr_solve():
    n = Necklace(
        0,
        0,
        (2, 2, 2, 2, 2, 2),
    )

    expr = necklace.dihedral_angle_sum(n, env)
    expr = cast(sympy.Expr, expr)
    expr_subs = expr.subs(
        {
            env.symbol_map(0): 1,
        }
    )
    print(expr_subs)
    s = sympy.solve(expr_subs - 2 * sympy.pi, env.symbol_map(2))
    print(s)


def test_necklace_expr_solve_mismatch():
    n = Necklace(
        0,
        1,
        (2, 2, 2, 2, 2, 2),
    )

    expr = necklace.dihedral_angle_sum(n, env)
    expr = cast(sympy.Expr, expr)

    expr_subs = expr.subs(
        {
            env.symbol_map(0): 1,
            env.symbol_map(1): 1,
        }
    )
    print(expr_subs)
    s = sympy.solve(expr_subs - 2 * sympy.pi, env.symbol_map(2))
    print(s)
