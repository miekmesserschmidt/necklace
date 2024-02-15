from functools import reduce
from typing import Any, cast
import sympy

from ..core import ArithmeticFuncObject, ArithmeticObject

from ..structures import (
    CoronaAngleSum,
    CosMickeyMouseAngle,
    CosTeddyBearDihedralAngle,
    MickeyMouse,
    MickeyMouseAngle,
    NecklaceBodySolidAngleSum,
    NecklaceDihedralAngleSum,
    TeddyBearDihedralAngle,
    TripodSolidAngle,
)


cos: ArithmeticFuncObject = cast(ArithmeticFuncObject, sympy.cos)
sin: ArithmeticFuncObject = cast(ArithmeticFuncObject, sympy.sin)
acos: ArithmeticFuncObject = cast(ArithmeticFuncObject, sympy.acos)
asin: ArithmeticFuncObject = cast(ArithmeticFuncObject, sympy.asin)
pi: ArithmeticObject = sympy.pi


def symbol(index: int) -> ArithmeticObject:
    return sympy.symbols(f"r_{index}", positive=True)


def evaluate(obj: Any) -> ArithmeticObject:
    match obj:
        case int() as i:
            return symbol(i)

        case CosMickeyMouseAngle(mm):
            rc = evaluate(mm.head)
            ra = evaluate(mm.ear0)
            rb = evaluate(mm.ear1)

            cos_ang: ArithmeticObject = (
                (rc + ra) ** 2 + (rc + rb) ** 2 - (ra + rb) ** 2
            ) / (2 * (rc + ra) * (rc + rb))
            return cos_ang

        case MickeyMouseAngle(mm):
            cos_ang = evaluate(CosMickeyMouseAngle(mm))
            return acos(cos_ang)

        case CosTeddyBearDihedralAngle(tb):
            a, b = tb.body, tb.head
            c, d = tb.hand0, tb.hand1

            cos_ang_a_dc = evaluate(CosMickeyMouseAngle(MickeyMouse(a, d, c)))
            cos_ang_a_db = evaluate(CosMickeyMouseAngle(MickeyMouse(a, d, b)))
            cos_ang_a_bc = evaluate(CosMickeyMouseAngle(MickeyMouse(a, b, c)))

            # ang_a_dc = evaluate(MickeyMouseAngle(MickeyMouse(a, d, c)))
            ang_a_db = evaluate(MickeyMouseAngle(MickeyMouse(a, d, b)))
            ang_a_bc = evaluate(MickeyMouseAngle(MickeyMouse(a, b, c)))

            cos_dihed = (cos_ang_a_dc - cos_ang_a_db * cos_ang_a_bc) / (
                sin(ang_a_db) * sin(ang_a_bc)
            )
            return cos_dihed

        case TeddyBearDihedralAngle(tb):
            cos_ang = evaluate(CosTeddyBearDihedralAngle(tb))
            return acos(cos_ang)

        case TripodSolidAngle(tp):
            solid_ang_sum = reduce(
                lambda a, b: a + b,
                (evaluate(TeddyBearDihedralAngle(tb)) for tb in tp.teddy_bears()),
            )
            return solid_ang_sum - pi

        case NecklaceDihedralAngleSum(n):
            solid_ang_sum = reduce(
                lambda a, b: a + b,
                (
                    evaluate(TeddyBearDihedralAngle(tb))
                    for tb in n.teddy_bear_sequence()
                ),
            )
            return solid_ang_sum

        case NecklaceBodySolidAngleSum(n):
            solid_ang_sum = reduce(
                lambda a, b: a + b,
                (evaluate(TripodSolidAngle(tp)) for tp in n.body_apex_tripods()),
            )
            return solid_ang_sum

        case CoronaAngleSum(cor):
            ang_sum = reduce(
                lambda a, b: a + b,
                (evaluate(MickeyMouseAngle(mm)) for mm in cor.mickey_mouse_sequence()),
            )
            return ang_sum

        case _:
            raise ValueError(f"Cannot evaluate {obj}")
