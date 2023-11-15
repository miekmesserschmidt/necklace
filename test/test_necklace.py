import sympy
from necklace.necklace import Expr, Necklace, necklace_expression


def smap(index: int) -> Expr:
    return sympy.symbols(f"r_{index}", positive=True)


def test_necklace():
    n = Necklace("a", "b", "abc")


def test_necklace_expr():
    n = Necklace(0, 1, (2, 2, 2, 2))

    expr = necklace_expression(n, smap)
    print(expr)


def test_necklace_expr_solve():
    n = Necklace(
        0,
        0,
        (
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
        ),
    )

    expr = necklace_expression(n, smap)

    expr_subs = expr.subs(
        {
            smap(0): 1,
        }
    )
    print(expr_subs)
    s = sympy.solve(expr_subs - 2 * sympy.pi, smap(2))
    print(s)


def test_necklace_expr_solve_mismatch():
    n = Necklace(
        0,
        1,
        (
            2,
            2,
            2,
            2,
            2,
            2,
        ),
    )

    expr = necklace_expression(n, smap)

    expr_subs = expr.subs(
        {
            smap(0): 1,
            smap(1): 1,
        }
    )
    print(expr_subs)
    s = sympy.solve(expr_subs - 2 * sympy.pi, smap(2))
    print(s)
