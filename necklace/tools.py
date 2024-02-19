import math
from typing import Any, Iterable, List, Tuple
from collections import deque
from functools import reduce
from typing import Dict, Iterable, Protocol, Self, Sequence, Tuple


class SupportsAdd(Protocol):
    def __add__(self, other) -> Self: ...


class SupportsMul(Protocol):
    def __mul__(self, other) -> Self: ...


class SupportsRMul[T](Protocol):
    def __rmul__(self, other) -> T: ...


def all_rotations[T](s: Sequence[T]) -> Iterable[Tuple[T, ...]]:
    s = list(s)
    N = len(s)

    d = deque(s)

    yield tuple(d)

    for _ in range(N - 1):
        d.rotate()
        yield tuple(d)


def sum_[T: SupportsAdd](items: Iterable[T]) -> T:
    return reduce(lambda a, b: a + b, items)


def dict_dot[T, W, U, V: SupportsRMul](a: Dict[T, U], b: Dict[T, V]) -> W:
    domain = set(a.keys()) & set(b.keys())
    return sum_(a[k] * b[k] for k in domain)


def weighted_range(weight: Any, max_val: Any) -> Iterable[int]:
    top = math.ceil(max_val / weight)

    if max_val % weight == 0:
        top += 1

    return range(0, top)
