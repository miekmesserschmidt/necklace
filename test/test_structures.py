from necklace.structures import Corona, Necklace


def test_corona_canonical():
    c = Corona(0, (0, 3, 2, 3, 4, 0))
    assert c.canonical() == Corona(0, (4, 3, 2, 3, 0, 0))


def test_necklace_canonical():
    n = Necklace(0, 1, (0, 3, 2, 3, 4, 0))
    assert n.canonical() == Necklace(0, 1, (4, 3, 2, 3, 0, 0))
