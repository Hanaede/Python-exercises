"""
Author: Enrique Mariño Jiménez
"""
from __future__ import annotations
from typeguard import typechecked


@typechecked
class Terminal:
    __terminals_created = []
    __INITIAL_NUMBERS = ['6', '7', '9']

    def __init__(self, number: (int, str)):
        self.__minutes_spoken = 0

        if isinstance(number, int):
            Terminal.raise_if_not_ok_number(str(number))
            self.__number = str(number)
            Terminal.__terminals_created.append(str(number))
        else:
            Terminal.raise_if_not_ok_number(number)
            self.__number = number
            Terminal.__terminals_created.append(number)

    @property
    def number(self):
        return self.__number

    @property
    def minutes_spoken(self):
        return self.__minutes_spoken

    @staticmethod
    def raise_if_not_ok_number(number: str):
        int(number)
        if (number in Terminal.__terminals_created or len(number) != 9
                or not number[0] in Terminal.__INITIAL_NUMBERS):
            raise ValueError('El número no es válido.')

    def call_terminal(self, other: Terminal, duration: int):
        if duration < 0:
            raise ValueError('El tiempo que habla no puede ser negativo')
        if self.number == other.number:
            raise ValueError('No puede llamar al número con el que está llamando')
        self.__minutes_spoken += duration
        other.__minutes_spoken += duration

    def __str__(self):
        return f'Nº {self.number} - {self.minutes_spoken}s de conversación'
