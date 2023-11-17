from dataclasses import dataclass
from typing import Protocol

from .core import ArithmeticFuncObject, ArithmeticObject, Label, MathFunc, SymbolMap


class Environment(Protocol):
    symbol_map: SymbolMap

    cos: MathFunc | ArithmeticFuncObject
    sin: MathFunc | ArithmeticFuncObject
    acos: MathFunc | ArithmeticFuncObject
    asin: MathFunc | ArithmeticFuncObject
    pi: ArithmeticObject


@dataclass
class ConcreteEnvironment(Environment):
    symbol_map: SymbolMap

    cos: MathFunc | ArithmeticFuncObject
    sin: MathFunc | ArithmeticFuncObject
    acos: MathFunc | ArithmeticFuncObject
    asin: MathFunc | ArithmeticFuncObject
    pi: ArithmeticObject
