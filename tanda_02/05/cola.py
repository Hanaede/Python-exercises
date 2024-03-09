"""
Author: Enrique Mariño Jiménez
"""
from __future__ import annotations
from typeguard import typechecked


@typechecked
class Queue:
    def __init__(self, *values):
        self.__values = list(values)

    @classmethod
    def other_enqueue(cls, value: Queue):
        new_enqueue = cls()
        new_enqueue.__values = value.__values.copy()
        return new_enqueue

    @property
    def value(self):
        return self.__values

    def size(self):
        return len(self.__values)

    def empty(self):
        return self.size() == 0

    def clear(self):
        self.__values = 0

    def add(self, element):
        self.__values.append(element)

    def front(self):
        return self.__values[0]
