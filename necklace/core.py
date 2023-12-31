from typing import Any, Callable, Protocol, Self, TypeAlias, TypeVar


class Comparable(Protocol):
    def __lt__(self, other) -> bool:
        ...

    def __gt__(self, other) -> bool:
        ...


Label = TypeVar("Label")


class ArithmeticObject(Protocol):
    def __add__(self, other) -> Self:
        ...

    def __sub__(self, other) -> Self:
        ...

    def __mul__(self, other) -> Self:
        ...

    def __rmul__(self, other) -> Self:
        ...

    def __truediv__(self, other) -> Self:
        ...

    def __rtruediv__(self, other) -> Self:
        ...

    def __pow__(self, other) -> Self:
        ...


class ArithmeticFuncObject(Protocol):
    def __add__(self, other) -> Self:
        ...

    def __sub__(self, other) -> Self:
        ...

    def __mul__(self, other) -> Self:
        ...

    def __rmul__(self, other) -> Self:
        ...

    def __div__(self, other) -> Self:
        ...

    def __pow__(self, other) -> Self:
        ...

    def __call__(self, *args, **kwargs) -> ArithmeticObject:
        ...


SymbolMap: TypeAlias = Callable[[Any], ArithmeticObject]
MathFunc: TypeAlias = Callable[[ArithmeticObject], ArithmeticObject]
