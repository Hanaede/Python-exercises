"""
Author: Enrique Mariño Jiménez
"""
from terminal import Terminal
from typeguard import typechecked


@typechecked
class Mobile(Terminal):
    __RAT_PRICE = 0.06
    __MONKEY_PRICE = 0.12
    __BISONTE_PRICE = 0.30
    __FEES = ["rata", "mono", "bisonte"]

    def __init__(self, number: (int, str), fee: str):
        super().__init__(number)
        self.fee = fee
        self.__priced = 0

    @property
    def fee(self):
        return self.__fee

    @fee.setter
    def fee(self, value: str):
        if value not in self.__FEES:
            raise ValueError('Tarifa incorrecta')
        self.__fee = value

    def call_terminal(self, other: Terminal, duration: int):
        super().call_terminal(other, duration)
        price = Mobile.price(duration, self.fee)
        self.__priced += price

    @staticmethod
    def price(self, duration: int, fee: str):
        if fee == "rata":
            price_per_second = self.__RAT_PRICE
        elif fee == "mono":
            price_per_second = self.__MONKEY_PRICE
        else:
            price_per_second = self.__BISONTE_PRICE
        price_cents = price_per_second * duration
        price = price_cents / 100
        return price

    def __str__(self):
        return (f'No {self.number[:3]} {self.number[3:5]} {self.number[5:7]} {self.number[7:]} - '
                f'{self.minutes_spoken}s de conversación - tarifados {self.__priced:.2f} euros')
