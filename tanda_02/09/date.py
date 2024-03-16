"""
Author = Enrique Mariño Jiménez
"""
from __future__ import annotations
from typeguard import typechecked

DAYS_MONTHS = [[31, 'Enero'], [28, 'Febrero'], [31, 'Marzo'], [30, 'Abril'], [31, 'Mayo'],
               [30, 'Junio'], [31, 'Julio'], [31, 'Agosto'], [30, 'Septiembre'], [31, 'Octubre'],
               [30, 'Noviembre'], [31, 'Diciembre']]
DAYS_MONTHS_LEAPYEAR = [[31, 'Enero'], [29, 'Febrero'], [31, 'Marzo'], [30, 'Abril'], [31, 'Mayo'],
                        [30, 'Junio'], [31, 'Julio'], [31, 'Agosto'], [30, 'Septiembre'], [31, 'Octubre'],
                        [30, 'Noviembre'], [31, 'Diciembre']]
DAYS_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


@typechecked
class Date:
    def __init__(self, day: int, month: int, year: int):

        Date.__ok_date(day, month, year)
        self.__day = day
        self.__month = month
        self.__year = year

    @staticmethod
    def __ok_date(day, month, year):
        if 1 > year > 9999:
            raise ValueError('El año introducido no es correcto. Por favor, indique un año del 1 al 9999.')
        if 12 < month < 1:
            raise ValueError('El mes introducido no es correcto. Por favor, indique un mes del q al 13.')
        if 1 > day < Date.__days_per_month(month, year):
            raise ValueError('El día es erróneo.')

    @classmethod
    def from_date(cls, other: Date):
        return cls(other.day, other.month, other.year)

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value: int):
        Date.__ok_date(value, self.month, self.year)
        self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        Date.__ok_date(self.day, value, self.year)
        self.__month = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value: int):
        Date.__ok_date(self.day, self.month, value)
        self.__year = value

    @staticmethod
    def __days_per_month(month, year):
        if month == 2 and Date.leap_year(year):
            return DAYS_MONTHS_LEAPYEAR[month - 1][0]
        return DAYS_MONTHS[month - 1][0]

    @staticmethod
    def leap_year(year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        return False

    def __add__(self, days: int):
        other = Date(self.day, self.month, self.year)
        for _ in range(days):
            other.next_day()
        return other

    def __radd__(self, other: int):
        return self + other

    def next_day(self):
        if self.day == Date.__days_per_month(self.month, self.year):
            if self.month == 12:
                self.day = 1
                self.month = 1
                self.year += 1
            else:
                self.day = 1
                self.month += 1
        else:
            self.day += 1

    def yesterday(self):
        if self.day == 1:
            if self.month == 1:
                self.day = 31
                self.month = 12
                self.year -= 1
            elif Date.leap_year(self.year) and self.month == 3:
                self.day = 29
                self.month -= 1
            else:
                self.month -= 1
                self.day = DAYS_MONTHS[self.month - 1][0]
        else:
            self.day -= 1

    # La parte de Restar fechas no he conseguido que me salga bien

    @property
    def to_str(self):
        return f'{self.year}{self.month}{self.day}'

    def __eq__(self, other: Date):
        return self.to_str == other.to_str

    def __gt__(self, other: Date):
        return self.to_str > other.to_str

    def __lt__(self, other: Date):
        return self.to_str < other.to_str

    def __str__(self):
        return f'{self.day} de {DAYS_MONTHS[self.month - 1][1]} de {self.year}'
