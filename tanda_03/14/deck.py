"""
Author: Enrique Mariño Jiménez
"""
from typing import List
from typeguard import typechecked
from card import Card


@typechecked
class Deck:
    def __init__(self, cards: List[Card]):
        self.__cards = cards.copy()

    @property
    def size(self):
        return len(self.__cards)

    def deal(self, player, num_cards: int):
        self.__check_deal(num_cards)
        cards_to_deal = self.__cards[:num_cards]
        player.receives(cards_to_deal)
        self.__cards = self.__cards[num_cards:]

    def __check_deal(self, number):
        if number < 0:
            raise ValueError("Tiene que repartir un número positivo de cartas")
        if number > len(self.__cards):
            raise ValueError("Demasiadas cartas para repartir")
