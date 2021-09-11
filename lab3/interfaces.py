from abc import ABC, abstractmethod
from typing import IO


class Writable(ABC):
    @abstractmethod
    def write(self, file: IO):
        raise NotImplementedError


class Readable(ABC):
    @abstractmethod
    def read(self, file: IO):
        raise NotImplementedError
