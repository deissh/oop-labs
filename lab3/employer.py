from functools import singledispatchmethod
from typing import List, Optional

from person import Person


class Employer(Person):
    _num: int

    def __init__(self):
        super(Employer, self).__init__()

    @singledispatchmethod
    def create(self, raw: List[str]):
        super(Employer, self).create(raw)

    @create.register
    def _create(self, first_name: str, second_name: str, last_name: str, num: int):
        super(Employer, self).create(first_name, second_name, last_name)
        self._num = num
        return self

    @property
    def num(self):
        return self._num

    @property
    def to_string(self):
        return super(Employer, self).to_string + f' {self._num}'

    def read(self, raw: List[str]):
        try:
            super(Employer, self).read(raw)
            self._num = int(raw[3])
        except Exception:
            raise ValueError("invalid person format")
