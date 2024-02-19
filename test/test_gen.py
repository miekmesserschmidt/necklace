from collections import defaultdict
from necklace.gen import gen_coronas, gen_all_mickey_mouses
from necklace.structures import Corona, CoronaAngleSum, MickeyMouse


def test_gen_cor():

    G = gen_coronas(Corona(0, tuple()), {0, 1})

    results = defaultdict(list)
    for cor in G:
        results[CoronaAngleSum(cor.canonical())].append(cor)

    assert len(results) == 11


def test_gen_mickey_mouses():
    centers = {0, 1}
    ears = {2, 3}

    out = set(gen_all_mickey_mouses(centers, ears))

    assert out == {
        MickeyMouse(0, 2, 2),
        MickeyMouse(0, 2, 3),
        MickeyMouse(0, 3, 2),
        MickeyMouse(0, 3, 3),
        MickeyMouse(1, 2, 2),
        MickeyMouse(1, 2, 3),
        MickeyMouse(1, 3, 2),
        MickeyMouse(1, 3, 3),
    }
