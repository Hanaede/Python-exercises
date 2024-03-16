"""
Author: Enrique Mariño Jiménez
"""
from typing import List
from typeguard import typechecked
from card import Card


@typechecked
class CardPlayer:

    def __init__(self, name: str):
        self.__name = name
        self.__cards = []

    @property
    def name(self):
        return self.__name

    @property
    def cards(self):
        return self.__cards.copy()

    def draw(self):
        self.__cards += self.__cards[-1]

    def delete(self):
        self.__cards.pop()

    def receives(self, cards: List[Card]):
        self.__cards.extend(cards)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name}, cards={self.__cards})"