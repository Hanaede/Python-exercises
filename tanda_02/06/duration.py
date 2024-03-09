"""
Author: Enrique Mariño Jiménez
"""
from __future__ import annotations
from typeguard import typechecked


@typechecked
class Duration:
    def __init__(self, hours, minutes=None, seconds=None):
        if isinstance(hours, Duration) and (minutes, seconds) == (None, None):
            other = hours
            self.__hours = other.__hours
            self.__minutes = other.__minutes
            self.__seconds = other.__seconds
        elif isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int):
            self.__hours = hours
            self.__minutes = minutes
            self.__seconds = seconds
            self.__normalize()
        else:
            raise TypeError("No se ha utilizado la forma correcta de creación")

    def __normalize(self):
        seconds = self.__total_seconds()
        if seconds < 0:
            raise ValueError("No puede haber duraciones de tiempo negativas")
        self.__hours = seconds // 3600
        self.__minutes = seconds % 3600 // 60
        self.__seconds = seconds % 3600 % 60

    def __total_seconds(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value: int):
        other = Duration(value, self.__minutes, self.__seconds)
        self.__hours, self.__minutes, self.__seconds = other.__hours, other.__minutes, other.__seconds

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value: int):
        other = Duration(self.__hours, value, self.__seconds)
        self.__hours, self.__minutes, self.__seconds = other.__hours, other.__minutes, other.__seconds

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value: int):
        other = Duration(self.hours, self.minutes, value)
        self.__hours, self.__minutes, self.__seconds = other.__hours, other.__minutes, other.__seconds

    def __add__(self, other: Duration):
        return Duration(self.__hours + other.__hours, self.__minutes + other.__minutes, self.__seconds + other.__seconds)

    def __sub__(self, other: Duration):
        return Duration(self.__hours - other.__hours, self.__minutes - other.__minutes, self.__seconds - other.__seconds)

    def add_hours(self, hours: int):
        self.__hours += hours

    def add_minutes(self, minutes: int):
        self.__minutes += minutes

    def add_seconds(self, seconds: int):
        self.__seconds += seconds

    def sub_hours(self, hours: int):
        self.__hours -= hours

    def sub_minutes(self, minutes: int):
        self.__minutes -= minutes

    def sub_seconds(self, seconds: int):
        self.__seconds -= seconds

    def __str__(self):
        return f"{self.__hours}h {self.__minutes}m {self.__seconds}s"
