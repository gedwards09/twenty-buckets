import math
from IStrategy import IStrategy
from random import randint

class BinsGame:
    
    def __init__(self, n: int, max_val: int, strategy: IStrategy):
        self._n = n
        self._max_val = max_val
        self._strategy = strategy
        self.new_game()
    
    def new_game(self):
        self._game_state = [-1 for i in range(self._n)]
        self._drawn = {}

    # sample without replacement
    def generate(self):
        n = randint(1, self._max_val)
        while n in self._drawn:
            n = randint(1, self._max_val)
        self._drawn[n] = 1
        return n
    
    def put(self, val: int):
        put_index = self._strategy.execute(val, self._game_state)
        if put_index < 0:
            return 1
        self._game_state[put_index] = val
        return 0
    
    def play(self):
        self.new_game()
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
        str(self._game_state)
