from dataclasses import dataclass
from typing import Generic, Sequence

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
