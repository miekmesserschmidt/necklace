from collections import deque
from dataclasses import dataclass
from typing import Generic, Iterable, Sequence, Tuple

from .core import Label


@dataclass
class MickeyMouse(Generic[Label]):
    """
    An arrangement representing three mutually tangent circles called head, ear0, ear1.
    Connecting the center of the head with the centers of the ears and angle is formed.
    """

    head: Label
    ear0: Label
    ear1: Label


@dataclass
class TeddyBear(Generic[Label]):
    """
    An arrangement representing four mutually tangent spheres called body, head, ear0, ear1.
    Connecting the centers a dihedral angle is formed on the line segment connecting bode and head.
    """

    body: Label
    head: Label
    hand0: Label
    hand1: Label


@dataclass
class Tripod(Generic[Label]):
    """
    An arrangement representing four mutually tangent spheres called apex, leg0, leg1, leg2.
    A solid angle is formed on the surface of the apex by leg0, leg1 and leg2.
    """

    apex: Label
    leg0: Label
    leg1: Label
    leg2: Label


@dataclass
class Pooh(Generic[Label]):
    """
    An arrangement representing spheres body, head and hand0, hunny, hand1.

    body, head, hand0, hunny are mutually tangent,
    body, head, hunny, hand1 are mutually tangent,

    hand0, hand1 should not be tangent.
    """

    body: Label
    head: Label

    hand0: Label
    hunny: Label
    hand1: Label

    def teddy_bears(self) -> Tuple[TeddyBear, TeddyBear]:
        return (
            TeddyBear(self.body, self.head, self.hand0, self.hunny),
            TeddyBear(self.body, self.head, self.hunny, self.hand1),
        )


@dataclass
class Necklace(Generic[Label]):
    body: Label
    head: Label
    beads: Sequence[Label]

    def teddy_bear_sequence(self) -> Iterable[TeddyBear[Label]]:
        beads0 = deque(self.beads)
        beads1 = beads0.copy()
        beads1.rotate()

        for a, b in zip(beads0, beads1):
            yield TeddyBear(self.body, self.head, a, b)

    def body_apex_tripods(self) -> Iterable[Tripod[Label]]:
        for b in self.teddy_bear_sequence():
            apex = b.body
            l0, l1, l2 = b.head, b.hand0, b.hand1
            yield Tripod(apex, l0, l1, l2)
