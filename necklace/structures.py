from collections import deque
from dataclasses import dataclass
from itertools import chain, permutations
from typing import Any, Dict, Generic, Iterable, Self, Sequence, Set, Tuple, TypeAlias

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

    def __lt__(self, other: Self) -> bool:
        return (
            self.canonical().head,
            self.canonical().ear0,
            self.canonical().ear1,
        ) < (
            other.canonical().head,
            other.canonical().ear0,
            other.canonical().ear1,
        )

    @property
    def labels(self) -> Set[Label]:
        return {self.head, self.ear0, self.ear1}

    def canonical(self) -> "MickeyMouse":
        a = max((self.ear0, self.ear1))
        b = min((self.ear0, self.ear1))
        return MickeyMouse(self.head, a, b)

    def triangle(self) -> "Triangle":
        return Triangle(self.head, self.ear0, self.ear1).canonical()


@dataclass(frozen=True)
class MickeyMouseAngle:
    mm: MickeyMouse


@dataclass(frozen=True)
class CosMickeyMouseAngle:
    mm: MickeyMouse


@dataclass(frozen=True)
class MickeyMouseComplex:
    mm: MickeyMouse


@dataclass(frozen=True)
class MickeyMouseComplexMultiplier:
    mm: MickeyMouse


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

    @property
    def labels(self) -> Set[Label]:
        return {self.head, self.head, self.hand0, self.hand1}

    def canonical(self) -> "TeddyBear":
        a = max((self.hand0, self.hand1))
        b = min((self.hand0, self.hand1))
        return TeddyBear(self.body, self.head, a, b)

    def body_mickey_mouses(self) -> Iterable[MickeyMouse]:
        b = self.body
        h = self.head
        h0 = self.hand0
        h1 = self.hand1

        yield MickeyMouse(b, h, h0).canonical()
        yield MickeyMouse(b, h, h1).canonical()
        yield MickeyMouse(b, h0, h1).canonical()


@dataclass(frozen=True)
class TeddyBearDihedralAngle:
    tb: TeddyBear


@dataclass(frozen=True)
class CosTeddyBearDihedralAngle:
    tb: TeddyBear


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

    @property
    def labels(self) -> Set[Label]:
        return {self.apex, self.leg0, self.leg1, self.leg2}

    def canonical(self) -> "Tripod":
        seq = reversed(sorted((self.leg0, self.leg1, self.leg2)))
        return Tripod(self.apex, *seq)

    def teddy_bears(self) -> Iterable[TeddyBear]:
        a, b, c, d = self.apex, self.leg0, self.leg1, self.leg2

        yield TeddyBear(a, b, c, d)
        yield TeddyBear(a, c, b, d)
        yield TeddyBear(a, d, b, c)


@dataclass(frozen=True)
class TripodSolidAngle:
    tripod: Tripod


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

    @property
    def labels(self) -> Set[Label]:
        return {self.body, self.head, self.hand0, self.hunny, self.hand1}

    def teddy_bears(self) -> Tuple[TeddyBear, TeddyBear]:
        return (
            TeddyBear(self.body, self.head, self.hand0, self.hunny).canonical(),
            TeddyBear(self.body, self.head, self.hunny, self.hand1).canonical(),
        )

    def canonical(self) -> "Pooh":
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

    @property
    def labels(self) -> Set[Label]:
        return {self.body, self.head} | set(self.beads)

    def canonical(self) -> "Necklace":
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
            yield TeddyBear(self.body, self.head, a, b).canonical()

    def body_head_mickey_mouses(self) -> Iterable[MickeyMouse]:
        for a in self.beads:
            yield MickeyMouse(self.body, self.head, a).canonical()

    def body_beads_mickey_mouses(self) -> Iterable[MickeyMouse]:
        beads0 = deque(self.beads)
        beads1 = beads0.copy()
        beads1.rotate()

        for a, b in zip(beads0, beads1):
            yield MickeyMouse(self.body, a, b).canonical()

    def body_apex_tripods(self) -> Iterable[Tripod]:
        for b in self.teddy_bear_sequence():
            apex = b.body
            l0, l1, l2 = b.head, b.hand0, b.hand1
            yield Tripod(apex, l0, l1, l2)


@dataclass(frozen=True)
class NecklaceDihedralAngleSum:
    necklace: Necklace


@dataclass(frozen=True)
class NecklaceBodySolidAngleSum:
    necklace: Necklace


@dataclass(frozen=True)
class Corona:
    """
    An arrangement representing discs around a central disc.
    """

    center: Label
    seq: Tuple[Label, ...]

    @property
    def labels(self) -> Set[Label]:
        return {self.center} | set(self.seq)

    def canonical(self) -> "Corona":
        b0 = tuple(self.seq)
        b1 = tuple(reversed(b0))
        canonical_rotation = max(
            chain(
                all_rotations(b0),
                all_rotations(b1),
            )
        )

        return Corona(self.center, canonical_rotation)

    def mickey_mouse_sequence(self, canonical: bool = True) -> Iterable[MickeyMouse]:
        beads0 = deque(self.seq)
        beads1 = beads0.copy()
        beads1.rotate(-1)

        if canonical:
            for a, b in zip(beads0, beads1):
                yield MickeyMouse(self.center, a, b).canonical()

        if not canonical:
            for a, b in zip(beads0, beads1):
                yield MickeyMouse(self.center, a, b)

    def triangle_sequence(self) -> Iterable["Triangle"]:
        for m in self.mickey_mouse_sequence():
            yield Triangle(m.head, m.ear0, m.ear1).canonical()


@dataclass(frozen=True)
class CoronaAngleSum:
    corona: Corona


@dataclass(frozen=True)
class Triangle:
    a: NodeId
    b: NodeId
    c: NodeId

    def __lt__(self, other: Self) -> bool:
        return (self.canonical().a, self.canonical().b, self.canonical().c) < (
            other.canonical().a,
            other.canonical().b,
            other.canonical().c,
        )

    def canonical(self) -> "Triangle":
        sorted_ids = sorted((self.a, self.b, self.c), reverse=True)
        return Triangle(*sorted_ids)

    def mickey_mouse_sequence(self) -> Iterable[MickeyMouse]:
        a, b, c = self.a, self.b, self.c
        yield MickeyMouse(a, b, c).canonical()
        yield MickeyMouse(b, a, c).canonical()
        yield MickeyMouse(c, a, b).canonical()


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

    @property
    def labels(self) -> Set[Label]:
        return {self.center} | set(
            self.label_map[k] for k in self.berry_structure.keys()
        )

    def necklace(self, nid: NodeId) -> Necklace:
        body = self.center
        head = self.label_map[nid]

        beads = tuple(map(lambda n: self.label_map[n], self.berry_structure[nid]))
        return Necklace(body, head, beads).canonical()

    def necklaces(self) -> Iterable[Necklace]:
        for nid in self.berry_structure.keys():
            yield self.necklace(nid).canonical()

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
