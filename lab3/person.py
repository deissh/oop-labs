from typing import IO

from functools import singledispatchmethod
from interfaces import Writable, Readable


class Person(Writable, Readable):
    first_name: str
    second_name: str
    last_name: str

    @singledispatchmethod
    def create(self, file: IO):
        self.read(file)
        return self

    @create.register
    def _create(self, first_name: str, second_name: str, last_name: str):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        return self

    @property
    def fio(self):
        return f'{self.first_name} {self.second_name} {self.last_name}'

    def write(self, file):
        file.write(self.fio + '\n')

    def read(self, file):
        raw = file.readline().split(' ')

        try:
            self.first_name = raw[0]
            self.second_name = raw[1]
            self.last_name = raw[1]
        except Exception:
            raise ValueError("invalid person format")
