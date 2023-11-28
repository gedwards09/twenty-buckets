import math
from Python.IStrategy import IStrategy
from typing import List

class NaiveStrategy(IStrategy):
        
    def execute(self, val: int, gameState: List) -> int:
        naiveIndex = Math.floor(len(gameState) * (val - 1) / maxValue)
        left, right = GameStrategy.getBoundaryIndices(val, gameState)
        if left + 1 == right:
            return -1
        elif naiveIndex <= left:
            return left + 1
        elif naiveIndex >= right:
            return right - 1
        else:
            return naiveIndex
        
        