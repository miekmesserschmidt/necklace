from ..environ import Environment

from ..core import ArithmeticObject


def sin_cos_identity(ang: ArithmeticObject, env: Environment) -> ArithmeticObject:
    return env.cos(ang) ** 2 + env.sin(ang) ** 2 - 1


def cos_pi_over_3_identity(ang: ArithmeticObject, env: Environment) -> ArithmeticObject:
    return 2 * env.cos(ang) - 1
