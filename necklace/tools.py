from collections import deque
from typing import Iterable, Sequence, Tuple, TypeVar


T = TypeVar("T")


def all_rotations(s: Sequence[T]) -> Iterable[Tuple[T, ...]]:
    s = list(s)
    N = len(s)

    d = deque(s)

    yield tuple(d)

    for _ in range(N - 1):
        d.rotate()
        yield tuple(d)
