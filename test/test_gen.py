from necklace.gen import coronas_from_mickey_mouse_dict
from necklace.structures import Corona, CoronaAngleSum


def test_coronas_from_mm_dict():
    c = Corona(1, (0, 0, 1, 1, 0, 1, 0, 2))
    mm_dict = CoronaAngleSum(c).mickey_mouse_counts()

    A = list(coronas_from_mickey_mouse_dict(mm_dict))

    assert c in A
    assert all(CoronaAngleSum(d).mickey_mouse_counts() == mm_dict for d in A)
