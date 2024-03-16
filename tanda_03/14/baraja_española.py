"""
Author: Enrique Mariño Jiménez
"""
from deck import Deck
from card import Card


class SpanishDeck(Deck):
    __POSIBLE_FIGURE = ['Bastos', 'Copas', 'Oros', 'Espadas']
    __POSIBLE_VALUES = ['1', '2', '3', '4', '5', '6', '7', 'Sota', 'Caballo', 'Rey']
    __NUMBER_CARDS = 40

    def __init__(self):
        cards = []
        for club in self.__class__.__POSIBLE_FIGURE:
            for value in self.__class__.__POSIBLE_VALUES:
                card = Card(club, value)
                cards.append(card)
        super().__init__(cards)
