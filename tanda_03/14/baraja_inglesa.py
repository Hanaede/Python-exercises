"""
Author: Enrique Mariño Jiménez
"""
from deck import Deck
from card import Card


class EnglishDeck(Deck):
    __POSIBLE_FIGURE = ['Picas', 'Corazones', 'Diamantes', 'Tréboles']
    __POSIBLE_VALUES = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    __NUMBER_CARDS = 52

    def __init__(self):
        cards = []
        for club in self.__class__.__POSIBLE_FIGURE:
            for value in self.__class__.__POSIBLE_VALUES:
                card = Card(club, value)
                cards.append(card)
        super().__init__(cards)
