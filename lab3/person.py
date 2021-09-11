from typing import IO

from functools import singledispatchmethod
from interfaces import Writable, Readable


class Person(Writable, Readable):
    _first_name: str
    _second_name: str
    _last_name: str

    @singledispatchmethod
    def create(self, file: IO):
        self.read(file)
        return self

    @create.register
    def _create(self, first_name: str, second_name: str, last_name: str):
        self._first_name = first_name
        self._second_name = second_name
        self._last_name = last_name
        return self

    @property
    def first_name(self):
        return self._first_name

    @property
    def second_name(self):
        return self.second_name

    @property
    def last_name(self):
        return self.last_name

    @property
    def to_string(self):
        return f'{self._first_name} {self._second_name} {self._last_name}'

    def write(self, file):
        file.write(self.to_string + '\n')

    def read(self, file):
        raw = file.readline().split(' ')

        try:
            self._first_name = raw[0]
            self._second_name = raw[1]
            self._last_name = raw[2]
        except Exception:
            raise ValueError("invalid person format")
