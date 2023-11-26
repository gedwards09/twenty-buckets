from IStrategy import IStrategy
from typing import List

class GameStrategy(IStrategy):
    
    def __init__(self, maxValue: int = 1000):
        self._maxValue = maxValue
            
    def getBoundaryIndices(val: int, gameState: List):
        n = len(gameState)
        left = -1
        right = n
        for i in range(n):
            if gameState[i] == -1:
                continue
            elif gameState[i] < val:
                left = i
            elif gameState[i] > val and right == n:
                right = i
        return (left, right)