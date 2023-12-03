from necklace.compute import corona
from necklace.compute.mickey_mouse import all_mickey_mouses, angle
from necklace.poly.tools import ensure_square_of_sub_expressions
from necklace.structures import (
    Corona,
    MickeyMouse,
)


def test_all_mickey_mouses():
    out = list(all_mickey_mouses([0, 1, 2]))
    out.sort()

    print(out)

    assert out == [
        MickeyMouse(0, 0, 0),
        MickeyMouse(0, 1, 0),
        MickeyMouse(0, 1, 1),
        MickeyMouse(0, 2, 0),
        MickeyMouse(0, 2, 1),
        MickeyMouse(0, 2, 2),
        #
        MickeyMouse(1, 0, 0),
        MickeyMouse(1, 1, 0),
        MickeyMouse(1, 1, 1),
        MickeyMouse(1, 2, 0),
        MickeyMouse(1, 2, 1),
        MickeyMouse(1, 2, 2),
        #
        MickeyMouse(2, 0, 0),
        MickeyMouse(2, 1, 0),
        MickeyMouse(2, 1, 1),
        MickeyMouse(2, 2, 0),
        MickeyMouse(2, 2, 1),
        MickeyMouse(2, 2, 2),
    ]
