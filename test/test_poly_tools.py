import sympy
from necklace.poly.tools import (
    ensure_square_of_sub_expression,
    ensure_square_of_sub_expressions,
    filter_even_powers_of_subexpr,
    filter_odd_powers_of_subexpr,
    filter_zero_powers_of_subexpr,
    has_odd_power,
)


def test_filter_even_powers():
    a = sympy.symbols("a")

    expr = 4 * a**4 + 3 * a**3 + 2 * a**2 + a + 1

    ev = filter_even_powers_of_subexpr(expr, a)

    assert (ev - (4 * a**4 + 2 * a**2)).simplify() == 0
    # assert (odd - (3 * a**3 + 1 * a)).simplify() == 0
    # assert (zero - (1)).simplify() == 0


def test_filter_odd_powers():
    a = sympy.symbols("a")

    expr = 4 * a**4 + 3 * a**3 + 2 * a**2 + a + 1

    odd = filter_odd_powers_of_subexpr(expr, a)

    # assert (ev - (4 * a**4 + 2 * a**2)).simplify() == 0
    assert (odd - (3 * a**3 + 1 * a)).simplify() == 0
    # assert (zero - (1)).simplify() == 0


def test_filter_zero_powers():
    a = sympy.symbols("a")

    expr = 4 * a**4 + 3 * a**3 + 2 * a**2 + a + 5

    zero = filter_zero_powers_of_subexpr(expr, a)

    # assert (ev - (4 * a**4 + 2 * a**2)).simplify() == 0
    # assert (odd - (3 * a**3 + 1 * a)).simplify() == 0
    assert (zero - (5)).simplify() == 0


def test_has_odd_power():
    a = sympy.symbols("a")

    expr = 4 * a**4 + 3 * a**3 + 2 * a**2 + a + 1

    assert has_odd_power(expr, a)


def test_has_no_odd_power():
    a = sympy.symbols("a")

    expr = 4 * a**4 + +2 * a**2 + 1

    assert not has_odd_power(expr, a)


def test_ensure_square_of_sub_expr():
    a = sympy.symbols("a")

    expr = 4 * a**4 + 3 * a**3 + 2 * a**2 + a + 1
    out = ensure_square_of_sub_expression(expr, a)

    expected = (3 * a**3 + a) ** 2 - (4 * a**4 + 2 * a**2 + 1) ** 2

    assert (expected - out).simplify() == 0


def test_ensure_square_of_sub_exprs():
    a, b = sympy.symbols("a,b")

    expr = 4 * a**4 + 3 * a**3 + 2 * a**2 + a + 1 + b
    out = ensure_square_of_sub_expressions(expr, {a, b})

    expected = (
        -256 * a**16
        - 224 * a**14
        - 241 * a**12
        - 180 * a**10
        + 32 * a**8 * b**2
        - 110 * a**8
        + 50 * a**6 * b**2
        - 50 * a**6
        + 36 * a**4 * b**2
        - 21 * a**4
        + 10 * a**2 * b**2
        - 6 * a**2
        - b**4
        + 2 * b**2
        - 1
    )

    assert (expected - out).simplify() == 0
