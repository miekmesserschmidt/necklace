from collections import Counter, deque
from itertools import chain
import itertools
from typing import Dict, Iterable, List

from .structures import Corona, Label, MickeyMouse


def _count_ear_in_mickey_mouse(mm: MickeyMouse, ear) -> int:
    return len([i for i in [mm.ear0, mm.ear1] if i == ear])


def _count_ear_occurrences_in_mickey_mouse_dict(
    mm_dict: Dict[MickeyMouse, int], ear: Label
) -> int:
    return sum(
        count * _count_ear_in_mickey_mouse(mm, ear) for mm, count in mm_dict.items()
    )


def mod2_ears_ok(mm_dict: Dict[MickeyMouse, int]) -> bool:
    ears = set(chain.from_iterable([m.ear0, m.ear1] for m in mm_dict.keys()))
    return all(
        _count_ear_occurrences_in_mickey_mouse_dict(mm_dict, ear) % 2 == 0
        for ear in ears
    )


def coronas_from_mickey_mouse_dict(mm_dict: Dict[MickeyMouse, int]) -> Iterable[Corona]:

    all_heads = set(mm.head for mm in mm_dict.keys())
    assert len(all_heads) == 1
    assert mod2_ears_ok(mm_dict)

    length = sum(n for n in mm_dict.values())

    (center,) = all_heads
    ears = set(itertools.chain.from_iterable((m.ear0, m.ear1) for m in mm_dict.keys()))

    def extend(partial_seq: List[Label]):

        if len(partial_seq) == length:
            s = deque(partial_seq)
            t = s.copy()
            t.rotate(-1)
            mm_list = [MickeyMouse(center, a, b).canonical() for a, b in zip(s, t)]
            mm_count = Counter(mm_list)
            if mm_count == mm_dict:
                yield Corona(center, tuple(partial_seq))

        elif len(partial_seq) < length:

            for new_s in ears:
                s = list(partial_seq) + [new_s]
                t = s[1:]

                mm_list = [MickeyMouse(center, a, b).canonical() for a, b in zip(s, t)]
                mm_count: Counter = Counter(mm_list)

                if all(v <= mm_dict[k] for k, v in mm_count.items()):
                    yield from extend(s)

    return extend([])
