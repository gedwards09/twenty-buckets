import math
from IStrategy import IStrategy
from random import randint

class BinsGame:
    
    def __init__(self, n: int, maxValue: int, strategy: IStrategy):
        self._n = n
        self._maxValue = maxValue
        self._strategy = strategy
        self.newGame()
    
    def newGame(self):
        self._gameState = [-1 for i in range(self._n)]
        self._drawn = {}

    # sample without replacement
    def generate(self):
        n = randint(1, self._maxValue)
        while n in self._drawn:
            n = randint(1, self._maxValue)
        self._drawn[n] = 1
        return n
    
    def put(self, val: int):
        putIndex = self._strategy.execute(val, self._gameState)
        if putIndex < 0:
            return 1
        self._gameState[putIndex] = val
        return 0
    
    def play(self):
        self.newGame()
        done = 0
        turns = 0
        while done != 1:
            k = self.generate()
            done = self.put(k)
            turns += 1
            if turns == 20:
                break
        return turns

    def toString(self):
        str(self._gameState)
