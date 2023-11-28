from Python.IStrategy import IStrategy

class MaxSurvivalTimeStrategy(IStrategy):
    
    def __init__():
        self._survivalTimesMemo = {}
    
    def execute(self, val: int, gameState: List, maxValue: int):
        n = len(gameState)
        left, right = GameUtils.getBoundaryIndices(val, gameState)
        if left == right - 1:
            return -1
        if left == right - 2:
            return left + 1
        turnsRemaining = right - left - 2
        p, q = MaxSurvivalTimeStategy.bernoulliProbability(val, left, right, gameState)
        maxSurvivalIndex = MaxSurvivalTimeStrategy.maximumSurvivalIndex(turnsRemaining, p)
            
        return None
    
    def bernouliProbability(val, left, right, gameState):
        lowerBound = gameState[left]
        upperBound = gameState[right]
        return ((val - lowerBound - 1) / (upperBound - LowerBound - 2), (upperBound - val - 1) / (upperBound - LowerBound - 2))
    
    def expectedSurvivalTime(left: int, right: int, p: float):
        if (left, right) in self._survivalTimesMemo:
            return self._survivalTimesMemo[(left, right)]
        if left == 0 or right == 0:
            self._survivalTimesMemo[(left, right)] = 0
            return 0
        survivalTime = p * MaxSurvivalTimeStrategy.expectedSurvivalTime(left - 1, right, p) \
                        + (1 - p) * MaxSurvivalTimeStrategy.expectedSurvivalTime(left, right - 1, p) + 1
        self._survivalTimesMemo[(left, right)] = survivalTime
        return survivalTime
    
    def maximumSurvivalIndex(turnsRemaining: int, p: float):
        maxSurvivalTime = 0
        maxSurvivalIndex = 0
        for i in range(turnsRemaining):
            survivalTime = MaxSurvivalTimeStrategy.expectedSurvivalTime(i, turnsRemaining - i, p)
            if survivalTime > maxSurvivalTime:
                maxSurvivalTime = survivalTime
                maxSurvivalIndex = i
        return maxSurvivalIndex
        