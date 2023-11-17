from necklace.tools import all_rotations


def test_all_rotations():
    s = (0, 1, 2, 3)

    L = list(all_rotations(s))

    assert L == [
        (0, 1, 2, 3),
        (3, 0, 1, 2),
        (2, 3, 0, 1),
        (1, 2, 3, 0),
    ]
