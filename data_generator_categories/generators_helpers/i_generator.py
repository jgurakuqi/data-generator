from abc import ABC, abstractmethod


class iGenerator(ABC):

    @classmethod
    @abstractmethod
    def generate(cls, max_attempts: int):
        pass
