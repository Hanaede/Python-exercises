"""
Autor: Enrique Mariño Jiménez
"""
from __future__ import annotations
import math
from typeguard import typechecked


@typechecked
class Fraction:

    def __init__(self, num: int, den: int):
        if den == 0:
            raise ZeroDivisionError("No puede usar el 0 como denominador.")
        mcd = math.gcd(num, den)
        self.__num = num // mcd
        self.__den = den // mcd

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    def __str__(self):
        return f"{self.__num} | {self.__den}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__num, self.__den})"

    def result(self):
        return self.__num / self.__den

    def __mul__(self, other: (int, Fraction)):
        if isinstance(other, int):
            return Fraction(self.__num * other, self.__den)
        return Fraction(self.__num * other.__num, self.__den * other.__den)

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return self * (-1)

    def __add__(self, other: Fraction):
        return Fraction(self.__num * other.__den + self.__den * other.__num, self.__den * other.__den)

    def __sub__(self, other: Fraction):
        return self + (-other)

    def __truediv__(self, other: Fraction):
        return Fraction(self.__num * other.__den, self.__den * other.__num)

    def __eq__(self, other: Fraction):
        return (self.__num, self.__den) == (other.__num, other.__den)

    def __ne__(self, other: Fraction):
        return self != other

    def __lt__(self, other: Fraction):
        return self.__num * other.__den < other.__num * self.__den

    def __le__(self, other: Fraction):
        return self <= other

    def __gt__(self, other: Fraction):
        return self > other

    def __ge__(self, other: Fraction):
        return self >= other
