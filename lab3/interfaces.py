from abc import ABC, abstractmethod
from typing import IO, List


class Writable(ABC):
    @abstractmethod
    def write(self, file: IO):
        raise NotImplementedError


class Readable(ABC):
    @abstractmethod
    def read(self, raw: List[str]):
        raise NotImplementedError
