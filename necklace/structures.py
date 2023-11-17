from collections import deque
from dataclasses import dataclass
from itertools import chain
from typing import Generic, Iterable, Self, Sequence, Tuple

from .tools import all_rotations

from .core import Label


@dataclass(frozen=True)
class MickeyMouse(Generic[Label]):
    """
    An arrangement representing three mutually tangent circles called head, ear0, ear1.
    Connecting the center of the head with the centers of the ears and angle is formed.
    """

    head: Label
    ear0: Label
    ear1: Label


@dataclass(frozen=True)
class TeddyBear(Generic[Label]):
    """
    An arrangement representing four mutually tangent spheres called body, head, ear0, ear1.
    Connecting the centers a dihedral angle is formed on the line segment connecting bode and head.
    """

    body: Label
    head: Label
    hand0: Label
    hand1: Label


@dataclass(frozen=True)
class Tripod(Generic[Label]):
    """
    An arrangement representing four mutually tangent spheres called apex, leg0, leg1, leg2.
    A solid angle is formed on the surface of the apex by leg0, leg1 and leg2.
    """

    apex: Label
    leg0: Label
    leg1: Label
    leg2: Label


@dataclass(frozen=True)
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


@dataclass(frozen=True)
class Necklace(Generic[Label]):
    """
    An arrangement of spheres as though a snowman with body and head is wearing a necklace.
    """

    body: Label
    head: Label
    beads: Tuple[Label, ...]

    def canonical(self) -> Self:
        b0 = tuple(self.beads)
        b1 = tuple(reversed(b0))
        canonical_rotation = max(
            chain(
                all_rotations(b0),
                all_rotations(b1),
            )
        )

        return Necklace(self.body, self.head, canonical_rotation)

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


@dataclass(frozen=True)
class Corona(Generic[Label]):
    """
    An arrangement representing discs around a central disc.
    """

    center: Label
    seq: Tuple[Label, ...]

    def canonical(self) -> Self:
        b0 = tuple(self.seq)
        b1 = tuple(reversed(b0))
        canonical_rotation = max(
            chain(
                all_rotations(b0),
                all_rotations(b1),
            )
        )

        return Corona(self.center, canonical_rotation)

    def mickey_mouse_sequence(self) -> Iterable[MickeyMouse[Label]]:
        beads0 = deque(self.seq)
        beads1 = beads0.copy()
        beads1.rotate()

        for a, b in zip(beads0, beads1):
            yield MickeyMouse(self.center, a, b)
