"""
Author: Enrique Mariño Jiménez
"""
from typeguard import typechecked


@typechecked
class Card:
    def __init__(self, palo: str, value: str):
        self.__palo = palo
        self.__value = value

    @property
    def palo(self):
        return self.__palo

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return f"Palo: {self.__palo}, \n Value: {self.__value}"


if __name__ == "__main__":
    card1 = Card("As de Basto", "5")
    print(card1)
