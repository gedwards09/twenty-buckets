from IStrategy import IStrategy
import math
from typing import List

class MaximumLikelihoodStrategy(IStrategy):
    
    def __init__(self, max_value: int = 1000):
        self._max_value = max_value
    
    def execute(self, val: int, game_state: List) -> None:
        left, right = MaximumLikelihoodStrategy.get_boundary_indices(val, game_state)
        if left == right - 1:
            return 1
        if left == right - 2:
            game_state[left+1] = val
            return 0
        if left < 0:
            nleft = 0
        else:
            nleft = game_state[left]
        if right >= len(game_state):
            nright = self._max_value + 1
        else:
            nright = game_state[right]
        # optimal assuming sample w/o replacement
        threshold = (right - left - 1) * (val - nleft - 1)/(nright - nleft - 2)
        if threshold == 0:
            put_index = left + 1
        elif threshold == right - left:
            putindex = right - 1
        else:
            put_index = left + math.ceil(threshold)
        if put_index < 0 or put_index >= self.n or put_index == left or put_index == right:
            print(val, left, put_index, right, game_state)
            
    def get_boundary_indices(val: int, game_state: List):
        left = -1
        right = len(game_state)
        for i in range(len(game_state)):
            if game_state[i] == -1:
                continue
            elif game_state[i] < val:
                left = i
            elif game_state[i] > val and right == len(game_state):
                right = i
        return (left, right)
        
        
    