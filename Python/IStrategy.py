from abc import ABC, abstractmethod
from typing import List

class IStrategy(ABC):
    @abstractmethod
    def execute(self, val: int, gameState: List, maxValue) -> int:
        pass