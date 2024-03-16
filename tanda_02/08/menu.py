"""
Author: Enrique Mariño Jiménez
"""
from __future__ import annotations
from typeguard import typechecked


@typechecked
class Menu:
    def __init__(self, *options: str, title: str = "Menu"):
        self.__options = list(options)
        self.title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value: str):
        self.__title = value

    def input_option(self, option: str):
        self.__options.append(option)

    def print_menu(self):
        print(self.__title)
        print("*" * len(self.__title))
        for o in range(len(self.__options)):
            print(f"{o + 1}. {self.__options[n]}")

    def choose_option(self):
        while True:
            option = int(input("Introduzca una opción: "))
            if option <= 1 and option <= len(self.__options):
                return option
            print("La opción es incorrecta.")
