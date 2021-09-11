import os
from typing import List, Optional

from person import Person
from interfaces import Readable, Writable


class PersonList(Readable, Writable):
    _data: List[Person]
    _filename: str

    def __init__(self, filename='temp.dat'):
        self._data = []
        self._filename = filename

        with open(self._filename) as f:
            self.read(f)

    def __del__(self):
        with open(self._filename, 'w') as f:
            self.write(f)

    @property
    def len(self):
        return len(self._data)

    def add_person(self, data: Person):
        self._data.append(data)

    def rm_person(self, idx: int) -> bool:
        if idx >= len(self._data) or idx < 0:
            return False

        del self._data[idx]
        return True

    def get_person(self, idx: int) -> Optional[Person]:
        if idx >= len(self._data) or idx < 0:
            return None

        return self._data[idx]

    def get_person_str(self, idx: int) -> Optional[str]:
        p = self.get_person(idx)

        return p.to_string if p is not None else None

    def read(self, file):
        while not file.tell() == os.fstat(file.fileno()).st_size:
            p = Person().create(file)
            self._data.append(p)

    def write(self, file):
        for p in self._data:
            p.write(file)

