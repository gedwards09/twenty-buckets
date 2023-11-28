import math
from Python.IStrategy import IStrategy
from Python.GameUtils import GameUtils
from typing import List

class NaiveStrategy(IStrategy):
        
    def execute(self, val: int, gameState: List, maxValue: int) -> int:
        naiveIndex = math.floor(len(gameState) * (val - 1) / maxValue)
        left, right = GameUtils.getBoundaryIndices(val, gameState)
        if left + 1 == right:
            return -1
        elif naiveIndex <= left:
            return left + 1
        elif naiveIndex >= right:
            return right - 1
        else:
            return naiveIndex
        
        