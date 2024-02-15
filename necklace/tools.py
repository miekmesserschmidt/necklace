from collections import deque
from functools import reduce
from typing import Iterable, Sequence, Tuple, TypeVar

from .core import ArithmeticObject


def all_rotations[T](s: Sequence[T]) -> Iterable[Tuple[T, ...]]:
    s = list(s)
    N = len(s)

    d = deque(s)

    yield tuple(d)

    for _ in range(N - 1):
        d.rotate()
        yield tuple(d)


def sum_[T: ArithmeticObject](items: Iterable[T]) -> T:
    return reduce(lambda a, b: a + b, items)
