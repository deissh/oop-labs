from functools import singledispatchmethod
from typing import List

from person import Person


class Student(Person):
    _group: str
    _course: int

    def __init__(self):
        super(Student, self).__init__()

    @singledispatchmethod
    def create(self, raw: List[str]):
        super(Student, self).create(raw)

    @create.register
    def _create(self, first_name: str, second_name: str, last_name: str, group: str, course: int):
        super(Student, self).create(first_name, second_name, last_name)
        self.group = group
        self.course = course
        return self

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value: str):
        self._group = value

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value: int):
        if value > 5 or value < 1:
            raise ValueError('value must be in range 1..5')

        self._course = value

    @property
    def to_string(self):
        return super(Student, self).to_string + f' {self._group} {self._course}'

    def read(self, raw: List[str]):
        try:
            super(Student, self).read(raw)
            self.group = raw[3]
            self.course = int(raw[4])
        except Exception:
            raise ValueError("invalid person format")
