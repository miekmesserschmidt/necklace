from necklace.structures import (
    Corona,
    CoronaAngleSum,
    MickeyMouse,
    Necklace,
    Pooh,
    Raspberry,
    TeddyBear,
    Tripod,
    Triangle,
)


def test_mickey_canonical():
    m = MickeyMouse(4, 0, 1).canonical()
    assert m == MickeyMouse(4, 1, 0)


def test_teddy_canonical():
    t = TeddyBear(5, 6, 0, 1).canonical()
    assert t == TeddyBear(5, 6, 1, 0)


def test_tripod_canonical():
    t = Tripod(5, 1, 6, 0).canonical()
    assert t == Tripod(5, 6, 1, 0)


def test_pooh_canonical():
    p = Pooh(5, 1, 6, 14, 8).canonical()
    assert p == Pooh(5, 1, 8, 14, 6)


def test_necklace_canonical():
    n = Necklace(0, 1, (0, 3, 2, 3, 4, 0))
    assert n.canonical() == Necklace(0, 1, (4, 3, 2, 3, 0, 0))


def test_corona_canonical():
    c = Corona(0, (0, 3, 2, 3, 4, 0))
    assert c.canonical() == Corona(0, (4, 3, 2, 3, 0, 0))


def test_corona_angle_sum_mickey_mouse_counts():
    c = Corona(0, (0, 3, 2, 3, 4, 0))
    ang_sum = CoronaAngleSum(c)

    assert ang_sum.mickey_mouse_counts() == {
        MickeyMouse(0, 3, 0): 1,
        MickeyMouse(0, 3, 2): 2,
        MickeyMouse(0, 4, 3): 1,
        MickeyMouse(0, 4, 0): 1,
        MickeyMouse(0, 0, 0): 1,
    }


def test_corona_angle_sum_eq():
    c0 = Corona(0, (3, 2, 3, 4, 0, 0))
    c1 = Corona(0, (2, 3, 4, 0, 0, 3))
    c2 = Corona(0, (2, 3, 4, 0, 0, 5))

    assert c0 != c1
    assert c0 != c2
    assert CoronaAngleSum(c0) == CoronaAngleSum(c1)
    assert CoronaAngleSum(c0) != CoronaAngleSum(c2)


def test_triangle_canonical():
    t = Triangle(1, 2, 0).canonical()
    assert t == Triangle(2, 1, 0)


def test_raspberry():
    r = Raspberry(
        center=0,
        berry_structure={
            0: (1, 2, 3),
            1: (2, 0, 3),
            2: (1, 3, 0),
            3: (1, 0, 2),
        },
        label_map={
            0: 0,
            1: 0,
            2: 0,
            3: 0,
        },
    )


def test_raspberry_necklace():
    r = Raspberry(
        center=4,
        berry_structure={
            0: (1, 2, 3),
            1: (2, 0, 3),
            2: (1, 3, 0),
            3: (1, 0, 2),
        },
        label_map={
            0: 0,
            1: 1,
            2: 2,
            3: 3,
        },
    )

    assert r.necklace(0).canonical() == Necklace(4, 0, (3, 2, 1))


def test_raspberry_necklaces():
    r = Raspberry(
        center=4,
        berry_structure={
            0: (1, 2, 3),
            1: (2, 0, 3),
            2: (1, 3, 0),
            3: (1, 0, 2),
        },
        label_map={
            0: 0,
            1: 1,
            2: 2,
            3: 3,
        },
    )

    N = list(map(lambda n: n.canonical(), r.necklaces()))
    assert N == [
        Necklace(4, 0, (3, 2, 1)),
        Necklace(4, 1, (3, 2, 0)),
        Necklace(4, 2, (3, 1, 0)),
        Necklace(4, 3, (2, 1, 0)),
    ]


def test_raspberry_triangles():
    r = Raspberry(
        center=4,
        berry_structure={
            0: (1, 2, 3),
            1: (2, 0, 3),
            2: (1, 3, 0),
            3: (1, 0, 2),
        },
        label_map={
            0: 0,
            1: 1,
            2: 2,
            3: 3,
        },
    )

    T = set(r.triangles())
    assert T == {
        Triangle(3, 1, 0),
        Triangle(2, 1, 0),
        Triangle(3, 2, 0),
        Triangle(3, 2, 1),
    }


def test_raspberry_tripods():
    r = Raspberry(
        center=4,
        berry_structure={
            0: (1, 2, 3),
            1: (2, 0, 3),
            2: (1, 3, 0),
            3: (1, 0, 2),
        },
        label_map={
            0: 0,
            1: 1,
            2: 2,
            3: 3,
        },
    )

    T = set(r.center_apex_tripods())
    assert T == {
        Tripod(4, 3, 2, 1),  # 0
        Tripod(4, 3, 2, 0),  # 1
        Tripod(4, 3, 1, 0),  # 2
        Tripod(4, 2, 1, 0),  # 3
    }
