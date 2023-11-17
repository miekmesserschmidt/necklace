from collections import deque
from dataclasses import dataclass
from itertools import chain
from typing import Dict, Generic, Iterable, Self, Sequence, Tuple, TypeAlias

from .tools import all_rotations


Label: TypeAlias = int
NodeId: TypeAlias = int


@dataclass(frozen=True)
class MickeyMouse:
    """
    An arrangement representing three mutually tangent circles called head, ear0, ear1.
    Connecting the center of the head with the centers of the ears and angle is formed.
    """

    head: Label
    ear0: Label
    ear1: Label

    def canonical(self) -> Self:
        a = max((self.ear0, self.ear1))
        b = min((self.ear0, self.ear1))
        return MickeyMouse(self.head, a, b)


@dataclass(frozen=True)
class TeddyBear:
    """
    An arrangement representing four mutually tangent spheres called body, head, ear0, ear1.
    Connecting the centers a dihedral angle is formed on the line segment connecting bode and head.
    """

    body: Label
    head: Label
    hand0: Label
    hand1: Label

    def canonical(self) -> Self:
        a = max((self.hand0, self.hand1))
        b = min((self.hand0, self.hand1))
        return TeddyBear(self.body, self.head, a, b)


@dataclass(frozen=True)
class Tripod:
    """
    An arrangement representing four mutually tangent spheres called apex, leg0, leg1, leg2.
    A solid angle is formed on the surface of the apex by leg0, leg1 and leg2.
    """

    apex: Label
    leg0: Label
    leg1: Label
    leg2: Label

    def canonical(self) -> Self:
        seq = reversed(sorted((self.leg0, self.leg1, self.leg2)))
        return Tripod(self.apex, *seq)


@dataclass(frozen=True)
class Pooh:
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

    def canonical(self) -> Self:
        a = max(self.hand0, self.hand1)
        b = min(self.hand0, self.hand1)
        return Pooh(self.body, self.head, a, self.hunny, b)


@dataclass(frozen=True)
class Necklace:
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

    def teddy_bear_sequence(self) -> Iterable[TeddyBear]:
        beads0 = deque(self.beads)
        beads1 = beads0.copy()
        beads1.rotate()

        for a, b in zip(beads0, beads1):
            yield TeddyBear(self.body, self.head, a, b)

    def body_apex_tripods(self) -> Iterable[Tripod]:
        for b in self.teddy_bear_sequence():
            apex = b.body
            l0, l1, l2 = b.head, b.hand0, b.hand1
            yield Tripod(apex, l0, l1, l2)


@dataclass(frozen=True)
class Corona:
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

    def mickey_mouse_sequence(self) -> Iterable[MickeyMouse]:
        beads0 = deque(self.seq)
        beads1 = beads0.copy()
        beads1.rotate()

        for a, b in zip(beads0, beads1):
            yield MickeyMouse(self.center, a, b)


@dataclass(frozen=True)
class Triangle:
    a: NodeId
    b: NodeId
    c: NodeId

    def canonical(self) -> Self:
        sorted_ids = sorted((self.a, self.b, self.c), reverse=True)
        return Triangle(*sorted_ids)


@dataclass(frozen=True)
class Raspberry:
    """
    Labelled planar triangulation with a central label.

    berry_structure is a dict of node ids to tuples of node ids in clockwise order.

    label_map is a dict assigning a label to each node.

    """

    center: Label

    berry_structure: Dict[NodeId, Tuple[NodeId, ...]]
    label_map: Dict[NodeId, Label]

    def necklace(self, nid: NodeId) -> Necklace:
        body = self.center
        head = self.label_map[nid]

        beads = tuple(map(lambda n: self.label_map[n], self.berry_structure[nid]))
        return Necklace(body, head, beads)

    def necklaces(self) -> Iterable[Necklace]:
        for nid in self.berry_structure.keys():
            yield self.necklace(nid)

    def triangles(self) -> Iterable[Triangle]:
        seen = set()
        for nid in self.berry_structure.keys():
            s0 = deque(self.berry_structure[nid])
            s1 = s0.copy()
            s1.rotate()
            for a, b in zip(s0, s1):
                t = Triangle(nid, a, b).canonical()
                if t in seen:
                    continue

                seen.add(t)
                yield t

    def center_apex_tripods(self) -> Iterable[Tripod]:
        for t in self.triangles():
            a, b, c = map(lambda nid: self.label_map[nid], (t.a, t.b, t.c))
            yield Tripod(self.center, a, b, c).canonical()
