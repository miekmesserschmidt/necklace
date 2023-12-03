import sympy
from sympy.core.power import Pow


def filter_even_powers_of_subexpr(expr, sub_expr):
    collected = sympy.collect(sympy.expand(expr), sub_expr, evaluate=False)

    zero_powers = collected.pop(1, 0)
    even_powers = []
    odd_powers = [collected.pop(sub_expr, 0) * sub_expr]

    for k, v in collected.items():
        if not isinstance(k, Pow):
            raise ValueError(f"{k} is not a power...")

        base, exponent = k.args
        if exponent % 2 == 1:
            odd_powers.append(k * v)
        else:
            even_powers.append(k * v)

    return sum(even_powers)


def filter_odd_powers_of_subexpr(expr, sub_expr):
    collected = sympy.collect(sympy.expand(expr), sub_expr, evaluate=False)

    zero_powers = collected.pop(1, 0)
    even_powers = []
    odd_powers = [collected.pop(sub_expr, 0) * sub_expr]

    for k, v in collected.items():
        if not isinstance(k, Pow):
            raise ValueError(f"{k} is not a power...")

        base, exponent = k.args
        if exponent % 2 == 1:
            odd_powers.append(k * v)

    return sum(odd_powers)


def filter_zero_powers_of_subexpr(expr, sub_expr):
    collected = sympy.collect(sympy.expand(expr), sub_expr, evaluate=False)
    zero_powers = collected.pop(1, 0)
    return zero_powers


def has_odd_power(expr, sub_expr):
    return bool(filter_odd_powers_of_subexpr(expr, sub_expr))


def ensure_square_of_sub_expression(expression, sub_expr):
    even = filter_even_powers_of_subexpr(expression, sub_expr)
    odd = filter_odd_powers_of_subexpr(expression, sub_expr)
    zero = filter_zero_powers_of_subexpr(expression, sub_expr)
    assert sympy.simplify(odd + even + zero - expression) == 0
    if odd:
        return sympy.expand(odd**2 - (even + zero) ** 2)
    else:
        return expression


def ensure_square_of_sub_expressions(expression, sub_expressions):
    expr = expression
    for sub_expr in sub_expressions:
        if has_odd_power(expr, sub_expr):
            expr = ensure_square_of_sub_expression(expr, sub_expr).expand()

    return expr
