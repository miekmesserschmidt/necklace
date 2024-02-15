import sympy
from necklace.compute.computer import DefaultComputer
from necklace.structures import MickeyMouse, Necklace, TeddyBear


def test_mm():
    c = DefaultComputer()
    m = MickeyMouse(0, 1, 2)

    cmm = c.mickey_mouse(m)

    rc, ra, rb = sympy.symbols("r_0, r_1, r_2", positive=True)
    expected = sympy.acos(
        ((rc + ra) ** 2 + (rc + rb) ** 2 - (rb + ra) ** 2) / (2 * (rc + ra) * (rc + rb))
    )

    assert sympy.simplify(cmm - expected) == 0


def test_teddy():
    comp = DefaultComputer()
    t = TeddyBear(0, 1, 2, 3)

    a, b, c, d = t.body, t.head, t.hand0, t.hand1

    ra, rb, rc, rd = sympy.symbols("r_0, r_1, r_2, r3", positive=True)

    ang_a_dc = comp.mickey_mouse(MickeyMouse(a, d, c))
    ang_a_db = comp.mickey_mouse(MickeyMouse(a, d, b))
    ang_a_bc = comp.mickey_mouse(MickeyMouse(a, b, c))

    cos = sympy.cos
    sin = sympy.sin

    expected = sympy.acos(
        (cos(ang_a_dc) - cos(ang_a_db) * cos(ang_a_bc))
        / (sin(ang_a_db) * sin(ang_a_bc))
    )

    ct = comp.teddy_bear(t)
    sympy.pretty_print(expected)
    sympy.pretty_print(ct)

    assert sympy.simplify(ct - expected) == 0


def test_necklace():
    comp = DefaultComputer()

    n = Necklace(0, 1, (2, 3, 4, 5))

    t0 = TeddyBear(0, 1, 2, 3)
    t1 = TeddyBear(0, 1, 3, 4)
    t2 = TeddyBear(0, 1, 4, 5)
    t3 = TeddyBear(0, 1, 5, 2)

    expected = sum(comp.teddy_bear(t) for t in (t0, t1, t2, t3))

    ncomp = comp.necklace(n)

    assert sympy.simplify(ncomp - expected) == 0
