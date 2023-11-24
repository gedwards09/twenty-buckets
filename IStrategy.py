from abc import ABC, abstractmethod
from typing import List

class IStrategy(ABC):
    @abstractmethod
    def execute(self, val: int, game_state: List):
        pass