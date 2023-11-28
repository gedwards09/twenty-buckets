import math
from Python.IStrategy import IStrategy
from Python.GameUtils import GameUtils
from typing import List

class MaximumLikelihoodStrategy(IStrategy):
    
    def execute(self, val: int, gameState: List, maxValue: int) -> int:
        n = len(gameState)
        left, right = GameUtils.getBoundaryIndices(val, gameState)
        if left == right - 1:
            return -1
        if left == right - 2:
            return left + 1
        if left < 0:
            nleft = 0
        else:
            nleft = gameState[left]
        if right >= n:
            nright = maxValue + 1
        else:
            nright = gameState[right]
        # optimal assuming sample w/o replacement
        threshold = (right - left - 1) * (val - nleft - 1)/(nright - nleft - 2)
        if threshold == 0:
            putIndex = left + 1
        elif threshold == right - left:
            putIndex = right - 1
        else:
            putIndex = left + math.ceil(threshold)
        if putIndex < 0 or putIndex >= n or putIndex == left or putIndex == right:
            print(val, left, putIndex, right, gameState)
        return putIndex
        
        
    