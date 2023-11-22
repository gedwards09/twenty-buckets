import math
from random import randint

class BinsGame:
    def __init__(self, n, max_val):
        self.n = n
        self.max_val = max_val
        self.new_game()
    
    def new_game(self):
        self.game_state = [-1 for i in range(self.n)]
        self.drawn = {}
        

    # sample without replacement
    def generate(self):
        n = randint(1, self.max_val)
        while n in self.drawn:
            n = randint(1, self.max_val)
        self.drawn[n] = 1
        return n
    
    def put(self, val):
        left, right = self.get_boundary_indices(val)
        if left == right - 1:
            return 1
        if left == right - 2:
            self.game_state[left+1] = val
            return 0
        if left < 0:
            nleft = 0
        else:
            nleft = self.game_state[left]
        if right >= self.n:
            nright = self.max_val+1
        else:
            nright = self.game_state[right]
        # optimal assuming sample w/o replacement
        threshold = (right - left - 1) * (val - nleft - 1)/(nright - nleft - 2)
        if threshold == 0:
            put_index = left + 1
        elif threshold == right - left:
            putindex = right - 1
        else:
            put_index = left + math.ceil(threshold)
        if put_index < 0 or put_index >= self.n or put_index == left or put_index == right:
            print(val, left, put_index, right, self.game_state)
        self.game_state[put_index] = val
        return 0
    
    def get_boundary_indices(self, val):
        left = -1
        right = self.n
        for i in range(self.n):
            if self.game_state[i] == -1:
                continue
            elif self.game_state[i] < val:
                left = i
            elif self.game_state[i] > val and right == self.n:
                right = i
        return (left, right)
    
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
        str(self.game_state)
