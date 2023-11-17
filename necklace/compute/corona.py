from typing import cast

from . import mickey_mouse

from ..core import ArithmeticObject
from ..environ import Environment
from ..structures import Corona


def angle_sum(
    c: Corona,
    env: Environment,
) -> ArithmeticObject:
    result = 0
    result = cast(ArithmeticObject, result)

    for m in c.mickey_mouse_sequence():
        result = mickey_mouse.angle(m, env) + result

    return result
