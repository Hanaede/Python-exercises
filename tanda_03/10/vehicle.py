"""
Author: Enrique Mariño Jiménez
"""
from abc import ABC
from typeguard import typechecked


@typechecked
class Vehicle(ABC):
    __vehicles_created = 0
    __total_kilometers = 0

    def __init__(self):
        self.__kilometers_traveled = 0
        Vehicle.__vehicles_created += 1

    def travel(self, distance_travaled: float):
        if distance_travaled < 0:
            raise ValueError('Debe recorrer una cantidad de kilómetros positivos')
        Vehicle.__total_kilometers += distance_travaled
        self.__kilometers_traveled += distance_travaled

    @property
    def kilometers_traveled(self):
        return self.__kilometers_traveled

    @classmethod
    def total_kilometers(cls):
        return cls.__total_kilometers

    @classmethod
    def vehicles_created(cls):
        return cls.__vehicles_created
