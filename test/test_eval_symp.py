from typing import cast
import sympy
from necklace.compute.computer import DefaultComputer
from necklace.core import ArithmeticFuncObject, ArithmeticObject
from necklace.structures import (
    Corona,
    CoronaAngleSum,
    MickeyMouse,
    MickeyMouseAngle,
    Necklace,
    NecklaceBodySolidAngleSum,
    NecklaceDihedralAngleSum,
    TeddyBear,
    TeddyBearDihedralAngle,
    Tripod,
    TripodSolidAngle,
)

from necklace.eval import symp
from necklace.tools import sum_


cos: ArithmeticFuncObject = cast(ArithmeticFuncObject, sympy.cos)
sin: ArithmeticFuncObject = cast(ArithmeticFuncObject, sympy.sin)
acos: ArithmeticFuncObject = cast(ArithmeticFuncObject, sympy.acos)
asin: ArithmeticFuncObject = cast(ArithmeticFuncObject, sympy.asin)
pi: ArithmeticObject = sympy.pi


def test_mickey_mouse():
    m = MickeyMouse(0, 1, 2)

    out = symp.evaluate(MickeyMouseAngle(m))

    rc, ra, rb = sympy.symbols("r_0, r_1, r_2", positive=True)
    expected = acos(
        ((rc + ra) ** 2 + (rc + rb) ** 2 - (rb + ra) ** 2) / (2 * (rc + ra) * (rc + rb))
    )

    assert sympy.simplify(out - expected) == 0


def test_corona():
    cor = Corona(0, (1, 2, 3, 4))

    out = symp.evaluate(CoronaAngleSum(cor))

    mms = (
        MickeyMouse(0, 1, 2),
        MickeyMouse(0, 2, 3),
        MickeyMouse(0, 3, 4),
        MickeyMouse(0, 4, 1),
    )

    expected = sum_(symp.evaluate(MickeyMouseAngle(m)) for m in mms)

    assert sympy.simplify(out - expected) == 0


def test_teddy():
    t = TeddyBear(0, 1, 2, 3)

    a, b, c, d = t.body, t.head, t.hand0, t.hand1

    ra, rb, rc, rd = sympy.symbols("r_0, r_1, r_2, r3", positive=True)

    ang_a_dc = symp.evaluate(MickeyMouseAngle(MickeyMouse(a, d, c)))
    ang_a_db = symp.evaluate(MickeyMouseAngle(MickeyMouse(a, d, b)))
    ang_a_bc = symp.evaluate(MickeyMouseAngle(MickeyMouse(a, b, c)))

    expected = sympy.acos(
        (cos(ang_a_dc) - cos(ang_a_db) * cos(ang_a_bc))
        / (sin(ang_a_db) * sin(ang_a_bc))
    )

    out = symp.evaluate(TeddyBearDihedralAngle(t))

    assert sympy.simplify(out - expected) == 0


def test_necklace_dihedral_ang_sum():
    n = Necklace(0, 1, (2, 3, 4, 5))

    t0 = TeddyBear(0, 1, 2, 3)
    t1 = TeddyBear(0, 1, 3, 4)
    t2 = TeddyBear(0, 1, 4, 5)
    t3 = TeddyBear(0, 1, 5, 2)

    expected = sum_(symp.evaluate(TeddyBearDihedralAngle(t)) for t in (t0, t1, t2, t3))

    out = symp.evaluate(NecklaceDihedralAngleSum(n))

    assert sympy.simplify(out - expected) == 0


def test_tripod():
    a, b, c, d = 0, 1, 2, 3
    tr = Tripod(a, b, c, d)

    t0 = TeddyBear(a, b, c, d)
    t1 = TeddyBear(a, c, b, d)
    t2 = TeddyBear(a, d, b, c)

    expected = (
        sum_(symp.evaluate(TeddyBearDihedralAngle(t)) for t in (t0, t1, t2)) - sympy.pi
    )

    out = symp.evaluate(TripodSolidAngle(tr))

    assert sympy.simplify(out - expected) == 0


def test_necklace_solid_ang_sum():
    n = Necklace(0, 1, (2, 3, 4, 5))

    tr0 = Tripod(0, 1, 2, 3)
    tr1 = Tripod(0, 1, 3, 4)
    tr2 = Tripod(0, 1, 4, 5)
    tr3 = Tripod(0, 1, 5, 2)

    expected = sum_(symp.evaluate(TripodSolidAngle(t)) for t in (tr0, tr1, tr2, tr3))

    out = symp.evaluate(NecklaceBodySolidAngleSum(n))

    assert sympy.simplify(out - expected) == 0
