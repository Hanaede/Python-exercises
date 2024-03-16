"""
Author: Enrique Mariño Jiménez
"""
from typeguard import typechecked
from vehicle import Vehicle


@typechecked
class Car(Vehicle):
    __LITRE_PER_KM = 0.1
    __MAX_CAPACITY = 50

    def __init__(self):
        super().__init__()
        self.__deposit = 0

    def refuel(self):
        self.__deposit = self.__MAX_CAPACITY

    @property
    def deposit(self):
        return self.__deposit

    def burnout(self):
        if self.deposit == 0:
            print('No hay gasolina')
        else:
            print("  _    _             /'_'_/.-''/                             _______\n"
                  + "  \\`../ |o_..__     / /__   / /  -= WORLD CHAMPIONSHIP =-   _\\=.o.=/_\n"
                  + "`.,(_)______(_).>  / ___/  / /                             |_|_____|_|\n"
                  + "~~~~~~~~~~~~~~~~~~/_/~~~~~/_/~~~~~~~~~~~~~~1DAW~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            self.__deposit -= 1

    def travel(self, distance: float):
        if self.deposit == 0:
            print('No puedes viajar sin gasolina')
            return
        travel_distance = distance
        gasoline_need = travel_distance * self.__LITRE_PER_KM
        if gasoline_need > self.deposit:
            travel_distance = self.deposit / self.__LITRE_PER_KM
            self.__deposit = 0
        else:
            self.__deposit -= gasoline_need
        super().travel(travel_distance)
