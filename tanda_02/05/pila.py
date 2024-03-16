"""
Author: Enrique Mariño Jiménez
"""
from __future__ import annotations
from typeguard import typechecked


@typechecked
class Stack:
    def __init__(self, *values: int):
        self.__values = list(values)

    @classmethod
    def from_pila(cls, value: Stack):
        new_stack = cls()
        new_stack.__values = value.__values.copy()
        return new_stack

    @property
    def value(self):
        return self.__values

    def size(self):
        return len(self.__values)

    def empty(self):
        return self.size() == 0

    def clear(self):
        self.__values = 0

    def push(self, element: int):
        self.__values.insert(0, element)

    def pop(self):
        return self.__values.pop(0)

    def top(self):
        return self.__values[0]

    def __str__(self):
        return f"{self.__values}"
