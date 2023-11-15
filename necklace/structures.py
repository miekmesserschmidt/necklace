from collections import deque
from dataclasses import dataclass
from typing import Generic, Iterable, Sequence

from .core import Label


@dataclass
class MickeyMouse(Generic[Label]):
    head: Label
    ear0: Label
    ear1: Label


@dataclass
class TeddyBear(Generic[Label]):
    body: Label
    head: Label
    hand0: Label
    hand1: Label


@dataclass
class Tripod(Generic[Label]):
    apex: Label
    leg0: Label
    leg1: Label
    leg2: Label


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
